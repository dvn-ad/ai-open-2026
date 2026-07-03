import os
import sys
import json

# Ensure the root of the project is in the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.module.hs_code_predictor import predict_hs_code

def test_predictions():
    test_cases = [
        {
            "description": "Besi Baja Coil",
            "country_of_origin": "China",
            "unit_of_measure": "Tons"
        },
        {
            "description": "Cotton Knitted T-Shirt",
            "country_of_origin": "Vietnam",
            "unit_of_measure": "Pieces"
        },
        {
            "description": "Motorcycle engine parts 150cc",
            "country_of_origin": "Japan",
            "unit_of_measure": "Boxes"
        }
    ]

    print("Running HS Code AI Predictor test cases...")
    for idx, case in enumerate(test_cases):
        print(f"\n--- Test Case {idx + 1}: {case['description']} ---")
        result = predict_hs_code(
            item_description=case["description"],
            country_of_origin=case["country_of_origin"],
            unit_of_measure=case["unit_of_measure"]
        )
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    test_predictions()
