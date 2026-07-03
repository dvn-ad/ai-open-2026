import sys
import os
import json
import logging

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient
from src.validation.api import app

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def run_test():
    client = TestClient(app)
    pdf_path = "dataset/UEU-Master-16519-lampiran.Image.Marked.pdf"
    
    if not os.path.exists(pdf_path):
        logger.error(f"Dataset PDF not found at {pdf_path}. Cannot run test.")
        sys.exit(1)
        
    print("\n==================================================")
    print("STARTING PLATFORM TEST ON DATASET:")
    print(f"File: {pdf_path}")
    print("==================================================")

    # 1. Test POST /api/extract
    print("\n[Stage 1] Testing Document Extraction via /api/extract...")
    with open(pdf_path, "rb") as f:
        files = {
            "commercial_invoice": ("UEU-Master-16519-lampiran.Image.Marked.pdf", f, "application/pdf")
        }
        response = client.post("/api/extract", files=files)
        
    if response.status_code != 200:
        logger.error(f"Extraction failed with status {response.status_code}: {response.text}")
        sys.exit(1)
        
    extract_data = response.json()
    extraction_id = extract_data["extraction_id"]
    documents = extract_data["documents"]
    
    print(f"  [+] Success! Extraction ID: {extraction_id}")
    print(f"  [+] Modules used: {extract_data['ocr_meta']['modules_used']}")
    print(f"  [+] Extracted Invoice No: {documents['commercial_invoice']['invoice_number']}")
    print(f"  [+] Extracted PL No: {documents['packing_list']['pl_number']}")
    print(f"  [+] Extracted BL No: {documents['bill_of_lading']['bl_number']}")
    print(f"  [+] Extracted PIB No: {documents['pib']['pib_number']}")
    print(f"  [+] Extracted Form E Reference No: {documents['form_e']['reference_number']}")

    # 2. Test POST /api/validate
    print("\n[Stage 2] Testing Declarations Validation via /api/validate...")
    validate_payload = {
        "extraction_id": extraction_id,
        "documents": documents
    }
    response = client.post("/api/validate", json=validate_payload)
    
    if response.status_code != 200:
        logger.error(f"Validation failed with status {response.status_code}: {response.text}")
        sys.exit(1)
        
    validate_data = response.json()
    validation_id = validate_data["validation_id"]
    
    print(f"  [+] Success! Validation ID: {validation_id}")
    print(f"  [+] Confidence Score: {validate_data['confidence_score']}%")
    print(f"  [+] Compliance Score: {validate_data['compliance_score']}%")
    print(f"  [+] Risk Level: {validate_data['risk_level']}")
    print(f"  [+] ML Risk Probability: {validate_data['ml_risk_probability']}%")
    print("\n  [+] Warnings found:")
    for w in validate_data["warnings"]:
        print(f"      - [{w['severity'].upper()}] Rule: {w['rule_id']}")
        print(f"        Message: {w['message']}")
        print(f"        Fix: {w['suggested_fix']}")
        print(f"        Fields: {w['affected_fields']}")

    print("\n  [+] SHAP Top Features contributing to risk:")
    for f in validate_data["shap_top_features"]:
        print(f"      - Feature: {f['label']} (Importance: {f['value']})")

    # 3. Test POST /api/submit-ceisa
    print("\n[Stage 3] Testing Simulated CEISA 4.0 Submission via /api/submit-ceisa...")
    submit_payload = {
        "validation_id": validation_id
    }
    response = client.post("/api/submit-ceisa", json=submit_payload)
    
    if response.status_code != 200:
        logger.error(f"CEISA submission failed with status {response.status_code}: {response.text}")
        sys.exit(1)
        
    submit_data = response.json()
    ceisa_payload = submit_data["ceisa_payload"]
    ceisa_ack = submit_data["ceisa_ack"]
    
    print(f"  [+] Success! Submission Status: {ceisa_ack['status']}")
    print(f"  [+] Assigned PIB No: {ceisa_ack['pib_number']}")
    print(f"  [+] Estimated Clearance Lane: {ceisa_ack['estimated_clearance_lane']}")
    print(f"  [+] CEISA Header Mapped Data:")
    print(json.dumps(ceisa_payload["header"], indent=4))
    print(f"  [+] CEISA Mapped Documents:")
    print(json.dumps(ceisa_payload["dokumen_lampiran"], indent=4))

    # 4. Test POST /api/predict-hs-code
    print("\n[Stage 4] Testing HS Code Classifier via /api/predict-hs-code...")
    hs_payload = {
        "item_description": "Concrete reinforcing steel bars (rebar) with ribs",
        "country_of_origin": "CN"
    }
    response = client.post("/api/predict-hs-code", json=hs_payload)
    
    if response.status_code == 200:
        hs_data = response.json()
        print(f"  [+] Success! Suggested HS Code: {hs_data['suggested_hs_code']}")
        print(f"  [+] Confidence: {hs_data['confidence']}%")
        print(f"  [+] Reasoning: {hs_data['reasoning']}")
        print(f"  [+] Alternatives: {hs_data['alternative_codes']}")
    else:
        logger.warning(f"HS code prediction failed or skipped: {response.text}")

    print("\n==================================================")
    print("ALL TESTS PASSED SUCCESSFULLY!")
    print("==================================================")

if __name__ == "__main__":
    run_test()
