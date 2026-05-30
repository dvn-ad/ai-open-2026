from openai import OpenAI
import json
import os
from .ollama_module import CEISA_PIB_SCHEMA

def run_openai(source_text, model="gpt-4o-mini", api_key=None):
    """
    Extract structured customs information from raw OCR text using OpenAI.
    
    Args:
        source_text (str): The raw text/markdown extracted from the document.
        model (str): OpenAI model to use (e.g. gpt-4o-mini, gpt-4o).
        api_key (str): Optional API key. If not provided, it will load from environment variable OPENAI_API_KEY.
        
    Returns:
        str: Restructured JSON string conforming to the CEISA PIB schema.
    """
    # Load API key from environment if not passed
    openai_api_key = api_key or os.getenv("OPENAI_API_KEY")
    
    if not openai_api_key:
        error_msg = "Error: OPENAI_API_KEY environment variable is not set and no API key was provided."
        print(error_msg)
        return json.dumps({
            "error": "Failed to extract structured data via OpenAI",
            "details": error_msg,
            "solution": "Set the OPENAI_API_KEY environment variable or pass the api_key parameter."
        }, indent=2)
        
    print(f"Running OpenAI restructuring using model: {model}")
    client = OpenAI(api_key=openai_api_key)
    
    system_instruction = (
        "You are an expert customs document data extraction system specializing in Indonesian CEISA PIB (Pemberitahuan Impor Barang) documents.\n"
        "Your task is to parse the raw OCR/Markdown text and extract all required fields into a structured JSON object.\n"
        "Pay extreme attention to numbers, dates, currency, NPWP (tax ID), and nested line items (HS codes, descriptions, weights, CIF values, and tax amounts).\n"
        "You MUST return a JSON object that adheres strictly to this schema:\n"
        f"{json.dumps(CEISA_PIB_SCHEMA, indent=2)}\n\n"
        "Ensure all numeric amounts are parsed as numbers, not strings. Do not hallucinate values. If a field is not found in the text, set it to null or omit it."
    )
    
    prompt = f"Please extract the CEISA customs invoice/PIB details from the following document text:\n\n{source_text}"
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system", 
                    "content": system_instruction
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            response_format={"type": "json_object"},
            temperature=0.1
        )
        
        extracted_content = response.choices[0].message.content
        # Try parsing it to validate it's correct JSON
        json_obj = json.loads(extracted_content)
        return json.dumps(json_obj, indent=2)
        
    except Exception as e:
        print(f"Error during OpenAI extraction: {e}")
        return json.dumps({
            "error": "Failed to extract structured data via OpenAI",
            "details": str(e)
        }, indent=2)
