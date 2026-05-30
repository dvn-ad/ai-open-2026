from ollama import chat
import json

# Define the comprehensive CEISA PIB (Pemberitahuan Impor Barang) JSON Schema
CEISA_PIB_SCHEMA = {
    "type": "object",
    "properties": {
        "header": {
            "type": "object",
            "properties": {
                "customs_office": {"type": "string", "description": "Kantor Pabean pengawas (e.g. KPU Tanjung Priok)"},
                "submission_number": {"type": "string", "description": "Nomor Pengajuan (26 digits)"},
                "registration_number": {"type": "string", "description": "Nomor Pendaftaran PIB"},
                "registration_date": {"type": "string", "description": "Tanggal Pendaftaran PIB"},
                "pib_type": {"type": "string", "description": "Jenis PIB (e.g. Biasa, Berkala)"},
                "import_type": {"type": "string", "description": "Jenis Impor (e.g. Untuk Dipakai)"}
            },
            "required": ["customs_office", "submission_number"]
        },
        "parties": {
            "type": "object",
            "properties": {
                "importer": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Nama Importir"},
                        "npwp": {"type": "string", "description": "NPWP Importir (15 or 16 digits)"},
                        "address": {"type": "string", "description": "Alamat lengkap Importir"}
                    },
                    "required": ["name", "npwp"]
                },
                "exporter": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Nama Penjual / Eksportir"},
                        "address": {"type": "string", "description": "Alamat Eksportir"},
                        "country": {"type": "string", "description": "Negara asal Eksportir"}
                    },
                    "required": ["name"]
                }
            },
            "required": ["importer", "exporter"]
        },
        "transport": {
            "type": "object",
            "properties": {
                "transport_mode": {"type": "string", "description": "Cara Pengangkutan (e.g. Laut, Udara)"},
                "carrier_name": {"type": "string", "description": "Nama Sarana Pengangkut & No Voyage/Flight"},
                "arrival_date": {"type": "string", "description": "Tanggal perkiraan tiba"},
                "loading_port": {"type": "string", "description": "Pelabuhan Muat"},
                "destination_port": {"type": "string", "description": "Pelabuhan Tujuan"}
            }
        },
        "documents": {
            "type": "object",
            "properties": {
                "invoice_number": {"type": "string"},
                "invoice_date": {"type": "string"},
                "packing_list_number": {"type": "string"},
                "packing_list_date": {"type": "string"},
                "bl_awb_number": {"type": "string", "description": "Bill of Lading or Air Waybill number"},
                "bl_awb_date": {"type": "string"}
            }
        },
        "financials": {
            "type": "object",
            "properties": {
                "currency": {"type": "string", "description": "Kode Valuta (e.g. USD, SGD)"},
                "fob_value": {"type": "number", "description": "Nilai FOB"},
                "freight": {"type": "number", "description": "Biaya Freight"},
                "insurance": {"type": "number", "description": "Biaya Asuransi"},
                "cif_value": {"type": "number", "description": "Nilai CIF (FOB + Freight + Insurance)"},
                "ndpbm_rate": {"type": "number", "description": "Kurs pajak/Nilai Dasar Penghitungan Bea Masuk"},
                "cif_idr": {"type": "number", "description": "Nilai CIF dalam Rupiah (CIF * Kurs)"}
            },
            "required": ["currency", "cif_value"]
        },
        "line_items": {
            "type": "array",
            "description": "Daftar barang impor yang tertera di form PIB",
            "items": {
                "type": "object",
                "properties": {
                    "item_number": {"type": "integer"},
                    "hs_code": {"type": "string", "description": "Pos Tarif HS Code (8 digits)"},
                    "description": {"type": "string", "description": "Uraian lengkap barang (jenis, tipe, spesifikasi)"},
                    "country_of_origin": {"type": "string", "description": "Negara asal barang"},
                    "net_weight_kg": {"type": "number", "description": "Berat Bersih (Netto) dalam kg"},
                    "cif_item_value": {"type": "number", "description": "Nilai CIF item ini"},
                    "duties": {
                        "type": "object",
                        "properties": {
                            "import_duty_rate": {"type": "string", "description": "Tarif Bea Masuk (e.g. 5%, 10%)"},
                            "import_duty_amount": {"type": "number", "description": "Nilai Bea Masuk dibayar"},
                            "vat_rate": {"type": "string", "description": "Tarif PPN (e.g. 11%)"},
                            "vat_amount": {"type": "number", "description": "Nilai PPN dibayar"},
                            "income_tax_rate": {"type": "string", "description": "Tarif PPh Pasal 22"},
                            "income_tax_amount": {"type": "number", "description": "Nilai PPh dibayar"}
                        }
                    }
                },
                "required": ["item_number", "hs_code", "description"]
            }
        },
        "totals": {
            "type": "object",
            "properties": {
                "total_import_duty": {"type": "number", "description": "Total Bea Masuk"},
                "total_vat": {"type": "number", "description": "Total PPN"},
                "total_income_tax": {"type": "number", "description": "Total PPh Pasal 22"},
                "total_levies": {"type": "number", "description": "Total seluruh pungutan impor yang harus dibayar"}
            },
            "required": ["total_levies"]
        }
    },
    "required": ["header", "parties", "financials", "line_items", "totals"]
}

def run_ollama(source_text, model="qwen3.5:cloud"):
    """
    Extract structured customs information from raw OCR text using Ollama.
    
    Args:
        source_text (str): The raw text/markdown extracted from the document.
        model (str): Ollama model to use.
        
    Returns:
        str: Restructured JSON string conforming to the CEISA PIB schema.
    """
    print(f"Running Ollama restructuring using model: {model}")
    
    system_instruction = (
        "You are an expert customs document data extraction system specializing in Indonesian CEISA PIB (Pemberitahuan Impor Barang) documents.\n"
        "Your task is to parse the raw OCR/Markdown text and extract all required fields into the strict JSON schema provided.\n"
        "Pay extreme attention to numbers, dates, currency, NPWP (tax ID), and nested line items (HS codes, descriptions, weights, CIF values, and tax amounts).\n"
        "If a specific optional field is not found in the text, omit it or set it to null. Do not hallucinate values. Ensure all numeric amounts are parsed as numbers, not strings."
    )
    
    prompt = f"Please extract the CEISA customs invoice/PIB details from the following document text into the required JSON schema:\n\n{source_text}"

    try:
        response = chat(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": system_instruction
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            format=CEISA_PIB_SCHEMA,
            options={
                "temperature": 0.1,  # Low temperature for highly structured and accurate extraction
            }
        )
        
        # Verify and pretty print JSON output
        extracted_content = response.message.content
        # Try parsing it to validate it's correct JSON
        json_obj = json.loads(extracted_content)
        return json.dumps(json_obj, indent=2)
        
    except Exception as e:
        print(f"Error during Ollama extraction: {e}")
        # Return raw content or error details
        return json.dumps({
            "error": "Failed to extract structured data via Ollama",
            "details": str(e),
            "raw_response": response.message.content if 'response' in locals() else None
        }, indent=2)