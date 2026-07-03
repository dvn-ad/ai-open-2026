import difflib
import re
from typing import List, Dict, Any
from .schema import ExtractedDocuments
from .rule_engine import ValidationResult

class CrossDocumentValidator:
    def validate(self, docs: ExtractedDocuments) -> List[ValidationResult]:
        results = []
        
        # 1. Weight Consistency (PL vs BL)
        if docs.packing_list and docs.bill_of_lading:
            pl_weight = docs.packing_list.total_gross_weight
            bl_weight = docs.bill_of_lading.total_gross_weight
            
            if pl_weight is not None and bl_weight is not None:
                if abs(pl_weight - bl_weight) > 0.1: # Allow minor float differences
                    results.append(ValidationResult("cross_doc_weight", False, f"Weight mismatch: PL={pl_weight}, BL={bl_weight}", risk_weight=30))
                else:
                    results.append(ValidationResult("cross_doc_weight", True, "Weight matches between PL and BL.", risk_weight=0))
        
        # 2. Quantity & Description matching (CI vs PL)
        if docs.commercial_invoice and docs.packing_list:
            ci_items = docs.commercial_invoice.items
            pl_items = docs.packing_list.items
            
            # Simple total quantity check
            ci_total_qty = sum(item.quantity for item in ci_items if item.quantity)
            pl_total_qty = sum(item.quantity for item in pl_items if item.quantity)
            
            if abs(ci_total_qty - pl_total_qty) > 0.01:
                results.append(ValidationResult("cross_doc_quantity", False, f"Total quantity mismatch: CI={ci_total_qty}, PL={pl_total_qty}", risk_weight=20))
            else:
                results.append(ValidationResult("cross_doc_quantity", True, "Total quantity matches between CI and PL.", risk_weight=0))
                
            # Item Description Fuzzy Matching
            for i, ci_item in enumerate(ci_items):
                if i < len(pl_items):
                    pl_item = pl_items[i]
                    similarity = difflib.SequenceMatcher(None, ci_item.description.lower(), pl_item.description.lower()).ratio()
                    if similarity < 0.6:
                        results.append(ValidationResult("cross_doc_description", False, f"Item {i+1} description mismatch (Sim: {similarity:.2f}). CI: '{ci_item.description}', PL: '{pl_item.description}'", risk_weight=15))
                    else:
                        results.append(ValidationResult("cross_doc_description", True, f"Item {i+1} description matches well (Sim: {similarity:.2f}).", risk_weight=0))
                else:
                    results.append(ValidationResult("cross_doc_missing_item", False, f"CI item {i+1} not found in PL.", risk_weight=20))

        # 3. PIB cross-document validation
        if docs.pib:
            pib = docs.pib
            # PIB vs Commercial Invoice
            if docs.commercial_invoice:
                if pib.invoice_number and docs.commercial_invoice.invoice_number:
                    # Strip spaces and punctuation for loose matching
                    pib_inv_clean = re.sub(r'[^a-zA-Z0-9]', '', pib.invoice_number).upper()
                    ci_inv_clean = re.sub(r'[^a-zA-Z0-9]', '', docs.commercial_invoice.invoice_number).upper()
                    if pib_inv_clean != ci_inv_clean:
                        results.append(ValidationResult("cross_doc_pib_invoice", False, f"Invoice number mismatch: PIB='{pib.invoice_number}', Invoice='{docs.commercial_invoice.invoice_number}'", risk_weight=20))
                    else:
                        results.append(ValidationResult("cross_doc_pib_invoice", True, "Invoice number matches between PIB and Commercial Invoice.", risk_weight=0))
                
                # Importer Tax ID check
                if pib.importer_tax_id and docs.commercial_invoice.importer_tax_id:
                    pib_tax_clean = re.sub(r'\D', '', pib.importer_tax_id)
                    ci_tax_clean = re.sub(r'\D', '', docs.commercial_invoice.importer_tax_id)
                    if pib_tax_clean != ci_tax_clean:
                        results.append(ValidationResult("cross_doc_pib_tax_id", False, f"Importer Tax ID mismatch: PIB='{pib.importer_tax_id}', Invoice='{docs.commercial_invoice.importer_tax_id}'", risk_weight=25))
                    else:
                        results.append(ValidationResult("cross_doc_pib_tax_id", True, "Importer Tax ID matches between PIB and Commercial Invoice.", risk_weight=0))

            # PIB vs Packing List
            if docs.packing_list:
                if pib.total_gross_weight is not None and docs.packing_list.total_gross_weight is not None:
                    if abs(pib.total_gross_weight - docs.packing_list.total_gross_weight) > 0.1:
                        results.append(ValidationResult("cross_doc_pib_gross_weight", False, f"Gross weight mismatch: PIB={pib.total_gross_weight}, PL={docs.packing_list.total_gross_weight}", risk_weight=20))
                    else:
                        results.append(ValidationResult("cross_doc_pib_gross_weight", True, "Gross weight matches between PIB and Packing List.", risk_weight=0))

            # PIB vs Bill of Lading
            if docs.bill_of_lading:
                if pib.bl_number and docs.bill_of_lading.bl_number:
                    pib_bl_clean = re.sub(r'[^a-zA-Z0-9]', '', pib.bl_number).upper()
                    bl_bl_clean = re.sub(r'[^a-zA-Z0-9]', '', docs.bill_of_lading.bl_number).upper()
                    if pib_bl_clean != bl_bl_clean:
                        results.append(ValidationResult("cross_doc_pib_bl", False, f"Bill of Lading number mismatch: PIB='{pib.bl_number}', BL='{docs.bill_of_lading.bl_number}'", risk_weight=20))
                    else:
                        results.append(ValidationResult("cross_doc_pib_bl", True, "Bill of Lading number matches between PIB and Bill of Lading.", risk_weight=0))
                
                if pib.total_gross_weight is not None and docs.bill_of_lading.total_gross_weight is not None:
                    if abs(pib.total_gross_weight - docs.bill_of_lading.total_gross_weight) > 0.1:
                        results.append(ValidationResult("cross_doc_pib_bl_weight", False, f"Gross weight mismatch: PIB={pib.total_gross_weight}, BL={docs.bill_of_lading.total_gross_weight}", risk_weight=20))
                    else:
                        results.append(ValidationResult("cross_doc_pib_bl_weight", True, "Gross weight matches between PIB and Bill of Lading.", risk_weight=0))

            # Form E validation against PIB
            if docs.form_e:
                form_e = docs.form_e
                if form_e.reference_number:
                    # Extract CO number from PIB import_permits or other places if present
                    co_numbers = [p for p in docs.import_permits if p.startswith("E20") or len(p) > 10]
                    if co_numbers:
                        pib_co = co_numbers[0]
                        if form_e.reference_number != pib_co:
                            results.append(ValidationResult("cross_doc_co_ref", False, f"Certificate of Origin number mismatch: Form E='{form_e.reference_number}', PIB='{pib_co}'", risk_weight=15))
                        else:
                            results.append(ValidationResult("cross_doc_co_ref", True, "Certificate of Origin reference number matches Form E.", risk_weight=0))
                
                if form_e.invoice_number and docs.commercial_invoice and docs.commercial_invoice.invoice_number:
                    fe_inv_clean = re.sub(r'[^a-zA-Z0-9]', '', form_e.invoice_number).upper()
                    ci_inv_clean = re.sub(r'[^a-zA-Z0-9]', '', docs.commercial_invoice.invoice_number).upper()
                    if fe_inv_clean != ci_inv_clean:
                        results.append(ValidationResult("cross_doc_co_invoice", False, f"Invoice number mismatch: Form E='{form_e.invoice_number}', Invoice='{docs.commercial_invoice.invoice_number}'", risk_weight=15))
                    else:
                        results.append(ValidationResult("cross_doc_co_invoice", True, "Invoice number matches between Form E and Commercial Invoice.", risk_weight=0))
                    
        return results

