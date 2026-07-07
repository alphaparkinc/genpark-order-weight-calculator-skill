"""
example_usage.py -- Demonstrates OrderWeightCalculatorClient
"""
from client import OrderWeightCalculatorClient

def main():
    client = OrderWeightCalculatorClient()
    result = client.calculate_cart_weight(
        items=[
            {"sku": "SKU-A", "quantity": 3, "unit_weight_lbs": 1.2},
            {"sku": "SKU-B", "quantity": 1, "unit_weight_lbs": 4.5}
        ],
        tare_box_weight_lbs=0.75
    )
    print("[Cart Weight Compilation]")
    print(f"Net: {result['net_weight_lbs']} lbs")
    print(f"Gross: {result['gross_weight_lbs']} lbs")

if __name__ == "__main__":
    main()
