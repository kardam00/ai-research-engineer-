def search_products(query, color=None, size=None, max_price=None):
    """Mock function to search for products across multiple sites."""
    mock_data = [
        {"name": "Floral Skirt", "price": 35, "color": "Red", "size": "S", "stock": True, "site": "ShopA"},
        {"name": "Floral Skirt", "price": 38, "color": "Blue", "size": "S", "stock": True, "site": "ShopB"},
        {"name": "Floral Skirt", "price": 50, "color": "Black", "size": "M", "stock": False, "site": "ShopC"},
    ]
    results = [p for p in mock_data if p["price"] <= max_price and p["color"] == color and p["size"] == size]
    return results

def estimate_shipping(destination, desired_date):
    """Mock function to estimate shipping times and costs."""
    mock_shipping = {
        "New York": {"delivery_days": 3, "cost": 5.99},
        "California": {"delivery_days": 5, "cost": 7.99},
        "Texas": {"delivery_days": 4, "cost": 6.50},
    }
    return mock_shipping.get(destination, {"delivery_days": "Unknown", "cost": "N/A"})

def apply_discount(original_price, promo_code):
    """Mock function to apply discounts."""
    discounts = {"SAVE10": 0.10, "SUMMER20": 0.20}
    discount = discounts.get(promo_code, 0)
    final_price = original_price * (1 - discount)
    return {"original_price": original_price, "final_price": final_price, "discount_applied": discount}

def compare_prices(product_name):
    """Mock function to compare prices of a product."""
    competitors = {
        "casual denim jacket": [
            {"site": "ShopA", "price": 75},
            {"site": "ShopB", "price": 80},
            {"site": "ShopC", "price": 70},
        ]
    }
    return competitors.get(product_name.lower(), [])

def get_return_policy(site):
    """Mock function to retrieve return policies."""
    policies = {
        "ShopA": "Returns accepted within 30 days. Refunds processed within 7 days.",
        "ShopB": "Returns accepted within 14 days. Store credit only.",
        "ShopC": "No returns accepted.",
    }
    return policies.get(site, "No information available.")
