# genpark-order-weight-calculator-skill

> **GenPark AI Agent Skill** -- Shopping cart shipping weight compiler.

## Quick Start

```python
from client import OrderWeightCalculatorClient
client = OrderWeightCalculatorClient()
res = client.calculate_cart_weight([{"quantity": 2, "unit_weight_lbs": 1.5}])
print(res["gross_weight_lbs"])
```
