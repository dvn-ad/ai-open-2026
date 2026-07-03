from typing import Dict, Any, List
from .schema import ExtractedDocuments
from .rule_engine import PermendagRuleEngine
from .cross_document import CrossDocumentValidator
from .ml_scoring import RiskScorer

class ConfidenceEngine:
    def __init__(self):
        self.rule_engine = PermendagRuleEngine()
        self.cross_doc_validator = CrossDocumentValidator()
        self.risk_scorer = RiskScorer()

    def process_declaration(self, docs: ExtractedDocuments) -> Dict[str, Any]:
        # 1. Evaluate Permendag Rules
        rule_results = self.rule_engine.evaluate(docs)
        compliance_score = self.rule_engine.get_compliance_score(rule_results)
        
        # 2. Evaluate Cross-Document Validation
        cross_doc_results = self.cross_doc_validator.validate(docs)
        
        # Calculate Cross-Doc Consistency Score
        cross_doc_score = 100
        for r in cross_doc_results:
            if not r.passed:
                cross_doc_score -= r.risk_weight
        cross_doc_score = max(0, cross_doc_score)
        
        # 3. Calculate Overall OCR Quality (mean of field level scores)
        ocr_scores = []
        if docs.commercial_invoice:
            ocr_scores.extend(docs.commercial_invoice.confidence_scores.values())
        if docs.packing_list:
            ocr_scores.extend(docs.packing_list.confidence_scores.values())
        if docs.bill_of_lading:
            ocr_scores.extend(docs.bill_of_lading.confidence_scores.values())
        if docs.pib:
            ocr_scores.extend(docs.pib.confidence_scores.values())
        if docs.form_e:
            ocr_scores.extend(docs.form_e.confidence_scores.values())
            
        mean_ocr_confidence = sum(ocr_scores)/len(ocr_scores) if ocr_scores else 100.0
        
        # 4. Extract ML Features
        missing_mandatory_fields_count = sum(1 for r in rule_results if r.rule_type == 'mandatory_field' and not r.passed)
        hs_code_invalid_flag = 1 if any(r.rule_type == 'hs_code_restriction' and not r.passed for r in rule_results) else 0
        missing_permit_flag = 1 if any('Missing' in r.message for r in rule_results if not r.passed) else 0
        
        weight_mismatch_flag = 1 if any(r.rule_type in ['cross_doc_weight', 'cross_doc_pib_gross_weight', 'cross_doc_pib_bl_weight'] and not r.passed for r in cross_doc_results) else 0
        quantity_mismatch_flag = 1 if any(r.rule_type == 'cross_doc_quantity' and not r.passed for r in cross_doc_results) else 0
        
        # 5. Predict ML Risk
        ml_features = {
            "mean_ocr_confidence": mean_ocr_confidence,
            "uncertain_tokens_count": sum(1 for s in ocr_scores if s < 80.0),
            "missing_mandatory_fields_count": missing_mandatory_fields_count,
            "hs_code_invalid_flag": hs_code_invalid_flag,
            "missing_permit_flag": missing_permit_flag,
            "weight_mismatch_flag": weight_mismatch_flag,
            "quantity_mismatch_flag": quantity_mismatch_flag,
            "desc_similarity_score": 1.0 # default if no mismatch found
        }
        
        for r in cross_doc_results:
            if r.rule_type == 'cross_doc_description' and 'Sim:' in r.message:
                try:
                    sim_str = r.message.split('Sim: ')[1].split(')')[0]
                    ml_features["desc_similarity_score"] = float(sim_str)
                except:
                    pass
                break
                
        ml_result = self.risk_scorer.predict_risk(ml_features)
        
        # 6. Final Confidence Score Formula
        # Confidence Score = (0.2 * OCR_Quality) + (0.3 * Cross_Doc_Consistency) + (0.3 * Compliance_Score) + (0.2 * (100 - ML_Risk_Probability))
        ml_risk_probability = ml_result["high_risk_probability"] * 100
        
        final_score = (0.2 * mean_ocr_confidence) + \
                      (0.3 * cross_doc_score) + \
                      (0.3 * compliance_score) + \
                      (0.2 * (100 - ml_risk_probability))
                      
        risk_level = "Low"
        if final_score < 50 or ml_risk_probability > 60:
            risk_level = "High"
        elif final_score < 75 or ml_risk_probability > 30:
            risk_level = "Medium"
            
        # Helper to map ValidationResult to structured warning
        def map_warning(r) -> Dict[str, Any]:
            severity = "medium"
            rule_id = r.rule_type.upper()
            suggested_fix = "Please verify the document data."
            affected_fields = []
            
            if r.rule_type == "mandatory_field":
                severity = "high"
                if "Tax ID" in r.message:
                    affected_fields = ["commercial_invoice.importer_tax_id"]
                    suggested_fix = "Ensure Importer Tax ID (NPWP) is provided on the Commercial Invoice."
                elif "Importer Name" in r.message:
                    affected_fields = ["commercial_invoice.importer_name"]
                    suggested_fix = "Ensure Importer Name is provided on the Commercial Invoice."
                elif "Currency" in r.message:
                    affected_fields = ["commercial_invoice.currency"]
                    suggested_fix = "Ensure Currency is specified on the Commercial Invoice."
                elif "Packing List total gross weight" in r.message:
                    affected_fields = ["packing_list.total_gross_weight"]
                    suggested_fix = "Provide total gross weight on the Packing List."
                elif "Bill of Lading total gross weight" in r.message:
                    affected_fields = ["bill_of_lading.total_gross_weight"]
                    suggested_fix = "Provide total gross weight on the Bill of Lading."
                else:
                    affected_fields = ["commercial_invoice"]
                    suggested_fix = "Provide the missing mandatory field."
                    
            elif r.rule_type == "hs_code_restriction":
                severity = "high"
                affected_fields = ["commercial_invoice.items[0].hs_code"]
                if "PI_Besi_Baja" in r.message:
                    rule_id = "PI_BESI_BAJA"
                    suggested_fix = "Attach PI_Besi_Baja document or update HS code."
                elif "LS_Tekstil" in r.message:
                    rule_id = "LS_TEKSTIL"
                    suggested_fix = "Attach LS_Tekstil document or update HS code."
                elif "PI_Kendaraan" in r.message:
                    rule_id = "PI_KENDARAAN"
                    suggested_fix = "Attach PI_Kendaraan document or update HS code."
                    
            elif r.rule_type == "cross_doc_weight":
                severity = "medium"
                affected_fields = ["packing_list.total_gross_weight", "bill_of_lading.total_gross_weight"]
                suggested_fix = "Reconcile gross weight values between Packing List and Bill of Lading."
                
            elif r.rule_type == "cross_doc_quantity":
                severity = "medium"
                affected_fields = ["commercial_invoice.items", "packing_list.items"]
                suggested_fix = "Reconcile item quantities between Commercial Invoice and Packing List."
                
            elif r.rule_type == "cross_doc_description":
                severity = "low"
                affected_fields = ["commercial_invoice.items", "packing_list.items"]
                suggested_fix = "Align item description text across Commercial Invoice and Packing List."
                
            elif r.rule_type == "cross_doc_missing_item":
                severity = "high"
                affected_fields = ["packing_list.items"]
                suggested_fix = "Add the missing item to the Packing List."

            elif r.rule_type == "cross_doc_pib_invoice":
                severity = "medium"
                affected_fields = ["pib.invoice_number", "commercial_invoice.invoice_number"]
                suggested_fix = "Check and align the invoice number in the PIB and Commercial Invoice."

            elif r.rule_type == "cross_doc_pib_tax_id":
                severity = "high"
                affected_fields = ["pib.importer_tax_id", "commercial_invoice.importer_tax_id"]
                suggested_fix = "Align the importer Tax ID (NPWP) across the PIB and Commercial Invoice."

            elif r.rule_type == "cross_doc_pib_gross_weight":
                severity = "medium"
                affected_fields = ["pib.total_gross_weight", "packing_list.total_gross_weight"]
                suggested_fix = "Align the total gross weight in the PIB and Packing List."

            elif r.rule_type == "cross_doc_pib_bl":
                severity = "medium"
                affected_fields = ["pib.bl_number", "bill_of_lading.bl_number"]
                suggested_fix = "Check and align the Bill of Lading number in the PIB and Bill of Lading."

            elif r.rule_type == "cross_doc_pib_bl_weight":
                severity = "medium"
                affected_fields = ["pib.total_gross_weight", "bill_of_lading.total_gross_weight"]
                suggested_fix = "Align the total gross weight in the PIB and Bill of Lading."

            elif r.rule_type == "cross_doc_co_ref":
                severity = "high"
                affected_fields = ["form_e.reference_number", "pib.import_permits"]
                suggested_fix = "Ensure the Certificate of Origin number matches the reference in the PIB."

            elif r.rule_type == "cross_doc_co_invoice":
                severity = "medium"
                affected_fields = ["form_e.invoice_number", "commercial_invoice.invoice_number"]
                suggested_fix = "Align the invoice number in the Form E Certificate of Origin with the Commercial Invoice."

            return {
                "severity": severity,
                "rule_id": rule_id,
                "message": r.message,
                "affected_fields": affected_fields,
                "suggested_fix": suggested_fix
            }

        # Compile warnings
        warnings = []
        for r in rule_results + cross_doc_results:
            if not r.passed:
                warnings.append(map_warning(r))
                
        # Add SHAP explanations if not already present
        for w in ml_result["top_warnings"]:
            if not any(w in existing_w.get("message", "") for existing_w in warnings if isinstance(existing_w, dict)):
                warnings.append({
                    "severity": "low",
                    "rule_id": "ML_EXPLAINER_NOTE",
                    "message": f"AI Explainer Note: {w} contributed to the risk score.",
                    "affected_fields": [],
                    "suggested_fix": "Review ML features contributing to this warning."
                })
                
        return {
            "confidence_score": round(final_score, 2),
            "risk_level": risk_level,
            "compliance_score": compliance_score,
            "ml_risk_probability": round(ml_risk_probability, 2),
            "warnings": warnings,
            "ml_explanations": ml_result["top_warnings"]
        }

