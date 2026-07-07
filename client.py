"""
order-weight-calculator-skill: Client SDK
Compiles parcel inventory specifications to estimate final shipping logistics gross weights.
"""
from __future__ import annotations
from typing import Optional


class OrderWeightCalculatorClient:
    """
    SDK for compiling package gross dimensions.
    """

    def calculate_cart_weight(
        self,
        items: list[dict],
        tare_box_weight_lbs: float = 0.5,
    ) -> dict:
        net_weight = 0.0

        for item in items:
            qty = int(item.get("quantity", 1))
            unit_w = float(item.get("unit_weight_lbs", 0.0))
            net_weight += qty * unit_w

        gross_weight = net_weight + tare_box_weight_lbs

        return {
            "net_weight_lbs": round(net_weight, 2),
            "gross_weight_lbs": round(gross_weight, 2),
            "item_count": sum(int(item.get("quantity", 1)) for item in items),
        }
