import json
import logging
from ollama import chat

logger = logging.getLogger(__name__)

def run_ollama(source, layout_results=None, table_results=None):
    """
    Runs Ollama (Qwen2.5-VL model) with rich layout and table context to structure
    the document content matching the ExtractedDocuments schema.
    """
    logger.info("Preparing prompt for Ollama structuring...")
    
    prompt = (
        "You are an expert customs clearance data entry assistant at Cikarang Dryport.\n"
        "Your task is to extract information from the provided trade document image and structure it\n"
        "strictly according to the schema defined below.\n\n"
        "To assist you, we have pre-extracted semantic layouts and table structures from the document:\n"
    )
    
    # 1. Add LayoutLMv3 semantic role context
    if layout_results:
        prompt += "\n--- Spatial & Semantic Layout Annotations (LayoutLMv3) ---\n"
        layout_text_blocks = []
        for item in layout_results:
            role = item.get("semantic_role", "OTHER")
            text = item.get("text", "")
            if role in ["HEADER", "FIELD_NAME", "FIELD_VALUE", "TOTAL"]:
                layout_text_blocks.append(f"Text: \"{text}\" -> Role: {role}")
        
        # Add a snippet (first 150 items) to prevent context bloat while providing core key-value contexts
        prompt += "\n".join(layout_text_blocks[:150]) + "\n"
    
    # 2. Add TableTransformer structured table rows context
    if table_results:
        prompt += "\n--- Detected Tabular Structures (TableTransformer) ---\n"
        for idx, table in enumerate(table_results):
            prompt += f"Table {idx + 1} (Line items):\n"
            for r_idx, row in enumerate(table.get("rows", [])):
                row_str = " | ".join(cell for cell in row)
                prompt += f"  Row {r_idx + 1}: {row_str}\n"
    else:
        prompt += "\n(No tabular grids detected by TableTransformer)\n"

    # 3. Add target schema instructions
    prompt += (
        "\n--- Target JSON Schema ---\n"
        "Extract the document into a JSON object matching this schema structure:\n"
        "{\n"
        "  \"commercial_invoice\": {\n"
        "    \"document_type\": \"Commercial Invoice\",\n"
        "    \"invoice_number\": \"string or null\",\n"
        "    \"importer_name\": \"string or null\",\n"
        "    \"importer_tax_id\": \"string or null\",\n"
        "    \"currency\": \"string or null\",\n"
        "    \"total_value\": float or null,\n"
        "    \"items\": [\n"
        "      {\n"
        "        \"description\": \"string\",\n"
        "        \"quantity\": float,\n"
        "        \"hs_code\": \"string or null\",\n"
        "        \"unit_price\": float or null,\n"
        "        \"total_price\": float or null\n"
        "      }\n"
        "    ]\n"
        "  },\n"
        "  \"packing_list\": {\n"
        "    \"document_type\": \"Packing List\",\n"
        "    \"pl_number\": \"string or null\",\n"
        "    \"total_gross_weight\": float or null,\n"
        "    \"items\": [\n"
        "      {\n"
        "        \"description\": \"string\",\n"
        "        \"quantity\": float,\n"
        "        \"hs_code\": \"string or null\",\n"
        "        \"unit_price\": float or null,\n"
        "        \"total_price\": float or null\n"
        "      }\n"
        "    ]\n"
        "  },\n"
        "  \"bill_of_lading\": {\n"
        "    \"document_type\": \"Bill of Lading\",\n"
        "    \"bl_number\": \"string or null\",\n"
        "    \"shipper_name\": \"string or null\",\n"
        "    \"consignee_name\": \"string or null\",\n"
        "    \"total_gross_weight\": float or null\n"
        "  },\n"
        "  \"pib\": {\n"
        "    \"document_type\": \"PIB\",\n"
        "    \"pib_number\": \"string or null\",\n"
        "    \"invoice_number\": \"string or null\",\n"
        "    \"bl_number\": \"string or null\",\n"
        "    \"importer_name\": \"string or null\",\n"
        "    \"importer_tax_id\": \"string or null\",\n"
        "    \"total_gross_weight\": float or null,\n"
        "    \"total_net_weight\": float or null,\n"
        "    \"items\": [\n"
        "      {\n"
        "        \"description\": \"string\",\n"
        "        \"quantity\": float,\n"
        "        \"hs_code\": \"string or null\",\n"
        "        \"unit_price\": float or null,\n"
        "        \"total_price\": float or null\n"
        "      }\n"
        "    ]\n"
        "  },\n"
        "  \"form_e\": {\n"
        "    \"document_type\": \"Form E Certificate of Origin\",\n"
        "    \"reference_number\": \"string or null\",\n"
        "    \"invoice_number\": \"string or null\",\n"
        "    \"vessel_name\": \"string or null\",\n"
        "    \"departure_date\": \"string or null\",\n"
        "    \"total_gross_weight\": float or null,\n"
        "    \"items\": [\n"
        "      {\n"
        "        \"description\": \"string\",\n"
        "        \"quantity\": float,\n"
        "        \"hs_code\": \"string or null\",\n"
        "        \"unit_price\": float or null,\n"
        "        \"total_price\": float or null\n"
        "      }\n"
        "    ]\n"
        "  },\n"
        "  \"import_permits\": [\"string\"]\n"
        "}\n\n"
        "Rules:\n"
        "1. Identify which document type is loaded and populate only that corresponding document field (e.g. if it is a commercial invoice, only populate commercial_invoice; keep others null).\n"
        "2. Do not hallucinate fields. Only extract what is present in the image and structured context.\n"
        "3. Output valid raw JSON conforming strictly to this format.\n"
    )

    # Find available model or use qwen2.5vl as default
    model_name = "qwen3.5:9b"
    try:
        from ollama import list as ollama_list
        res = ollama_list()
        models_list = getattr(res, 'models', []) or res.get('models', [])
        available_models = []
        for m in models_list:
            name = getattr(m, 'model', None) or getattr(m, 'name', None)
            if not name and isinstance(m, dict):
                name = m.get('model') or m.get('name')
            if name:
                available_models.append(name)
                
        if available_models:
            if model_name not in available_models and "qwen3.5:9b" in available_models:
                model_name = "qwen3.5:9b"
            elif model_name not in available_models:
                model_name = available_models[0]
        logger.info(f"Using Ollama model: {model_name}")
    except Exception as e:
        logger.warning(f"Failed to query available Ollama models: {e}. Defaulting to '{model_name}'.")

    # Check if the model supports vision
    is_vision_model = any(v in model_name.lower() for v in ["vl", "vision", "llava", "minicpm"])
    
    message_content = {
        "role": "user",
        "content": prompt
    }
    if is_vision_model:
        message_content["images"] = [source]
        logger.info(f"Vision model detected. Passing image to Ollama.")
    else:
        logger.info(f"Text model detected. Querying Ollama without image parameter.")
        
    messages = [message_content]

    try:
        logger.info(f"Querying Ollama ({model_name}) with structured prompt...")
        response = chat(
            model=model_name,
            messages=messages,
            format="json",
            think=False
        )
        return response.message.content
    except Exception as e:
        logger.error(f"Error querying Ollama: {e}")
        return None