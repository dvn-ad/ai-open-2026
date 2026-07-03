import json
import logging
import re
from ollama import chat

logger = logging.getLogger(__name__)

class HSCodePredictor:
    def __init__(self):
        # Default model matching the one used in ollama_module.py
        self.model_name = "qwen3.5:9b"
        self._resolve_model()

    def _resolve_model(self):
        """Resolves the available Ollama model name, similar to ollama_module.py."""
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
                if self.model_name not in available_models and "qwen3.5:9b" in available_models:
                    self.model_name = "qwen3.5:9b"
                elif self.model_name not in available_models:
                    self.model_name = available_models[0]
            logger.info(f"HSCodePredictor using Ollama model: {self.model_name}")
        except Exception as e:
            logger.warning(f"HSCodePredictor failed to query available models: {e}. Using default '{self.model_name}'.")

    def predict(self, item_description: str, country_of_origin: str, unit_of_measure: str = None) -> dict:
        """
        Builds a structured prompt grounded in Chapter 72 and Chapter 61 references,
        queries Ollama, and returns the suggested HS code data structure.
        """
        logger.info(f"Predicting HS code for: {item_description} (Origin: {country_of_origin})")

        prompt = (
            "You are an expert customs classifier specializing in Indonesian trade regulations (Permendag) at Cikarang Dryport.\n"
            "Your task is to predict the correct HS Code (6-10 digits) for the following item based on its description, country of origin, and optionally unit of measure.\n\n"
            "--- Item Details ---\n"
            f"Description: {item_description}\n"
            f"Country of Origin: {country_of_origin}\n"
        )
        if unit_of_measure:
            prompt += f"Unit of Measure: {unit_of_measure}\n"

        prompt += (
            "\n--- Reference Grounding (Indonesian HS Code Classification Guide) ---\n"
            "Use the following official chapters to ground your classification:\n\n"
            "Chapter 72: Iron and Steel (Besi dan Baja)\n"
            "- 7208.10: Flat-rolled products of iron or non-alloy steel, of a width of 600 mm or more, hot-rolled, not clad, plated or coated, in coils (e.g., Besi Baja Coil).\n"
            "- 7208.39: Other flat-rolled products, in coils, hot-rolled, of a thickness of less than 3 mm.\n"
            "- 7214.20: Concrete reinforcing bars (containing indents, ribs, grooves or other deformations produced during the rolling process).\n"
            "- 7225.30: Flat-rolled products of other alloy steel, of a width of 600 mm or more, hot-rolled, not further worked than hot-rolled, in coils.\n\n"
            "Chapter 61: Articles of Apparel and Clothing Accessories, Knitted or Crocheted (Pakaian dan Aksesori Pakaian)\n"
            "- 6109.10: T-shirts, singlets and other vests, knitted or crocheted, of cotton (e.g., Kaos Cotton).\n"
            "- 6104.62: Women's or girls' trousers, bib and brace overalls, breeches and shorts of cotton (knitted/crocheted).\n"
            "- 6115.95: Socks and other hosiery, knitted or crocheted, of cotton.\n\n"
            "Chapter 87: Vehicles Other Than Railway or Tramway Rolling-Stock, and Parts and Accessories Thereof (Kendaraan Bermotor)\n"
            "- 8703.21: Passenger motor cars with spark-ignition internal combustion reciprocating piston engine of a cylinder capacity not exceeding 1,000 cc.\n"
            "- 8708.29: Parts and accessories of bodies (including cabs) of motor vehicles.\n"
            "- 8711.20: Motorcycles with reciprocating internal combustion piston engine of a cylinder capacity exceeding 50 cc but not exceeding 250 cc.\n\n"
            "--- Output Format ---\n"
            "Provide your prediction in raw JSON format matching this schema exactly:\n"
            "{\n"
            "  \"suggested_hs_code\": \"string (6-10 digits without dots)\",\n"
            "  \"confidence\": float (0-100),\n"
            "  \"reasoning\": \"string (1 concise sentence explaining the classification classification based on the grounding references)\",\n"
            "  \"alternative_codes\": [\n"
            "    \"string (first alternative HS code)\",\n"
            "    \"string (second alternative HS code)\"\n"
            "  ]\n"
            "}\n"
        )

        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        fallback_response = {
            "suggested_hs_code": None,
            "confidence": 0.0,
            "reasoning": "Failed to generate prediction due to service error.",
            "alternative_codes": []
        }

        try:
            response = chat(
                model=self.model_name,
                messages=messages,
                format="json",
                think=False
            )
            content = response.message.content
            if content:
                # Clean up any potential markdown decoration
                cleaned = content.strip()
                if cleaned.startswith("```"):
                    cleaned = cleaned.split("\n", 1)[1]
                if cleaned.endswith("```"):
                    cleaned = cleaned.rsplit("\n", 1)[0]
                cleaned = cleaned.strip()
                if cleaned.startswith("json"):
                    cleaned = cleaned[4:].strip()
                try:
                    return json.loads(cleaned)
                except json.JSONDecodeError as je:
                    logger.warning(f"JSON parsing failed: {je}. Attempting regex recovery.")
                    return self._regex_parse_fallback(cleaned, fallback_response)
            return fallback_response
        except Exception as e:
            logger.error(f"Error querying Ollama in HSCodePredictor: {e}")
            return fallback_response

    def _regex_parse_fallback(self, text: str, fallback: dict) -> dict:
        result = {
            "suggested_hs_code": None,
            "confidence": 0.0,
            "reasoning": "Extracted via regex fallback.",
            "alternative_codes": []
        }
        
        # Extract suggested_hs_code
        code_match = re.search(r'"suggested_hs_code"\s*:\s*"([^"]*)"', text)
        if code_match:
            result["suggested_hs_code"] = code_match.group(1)
            
        # Extract confidence
        conf_match = re.search(r'"confidence"\s*:\s*(\d+(?:\.\d+)?)', text)
        if conf_match:
            result["confidence"] = float(conf_match.group(1))
            
        # Extract reasoning
        reasoning_match = re.search(r'"reasoning"\s*:\s*"(.*?)"\s*(?:,|\n|\})', text, re.DOTALL)
        if reasoning_match:
            result["reasoning"] = reasoning_match.group(1)
        else:
            reasoning_match_alt = re.search(r'"reasoning"\s*:\s*"(.*)"', text)
            if reasoning_match_alt:
                result["reasoning"] = reasoning_match_alt.group(1)

        # Extract alternative_codes
        alt_match = re.search(r'"alternative_codes"\s*:\s*\[(.*?)\]', text, re.DOTALL)
        if alt_match:
            codes = re.findall(r'"([^"]*)"', alt_match.group(1))
            result["alternative_codes"] = codes
            
        if result["suggested_hs_code"]:
            return result
        return fallback

def predict_hs_code(item_description: str, country_of_origin: str, unit_of_measure: str = None) -> dict:
    predictor = HSCodePredictor()
    return predictor.predict(item_description, country_of_origin, unit_of_measure)
