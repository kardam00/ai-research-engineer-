import google.generativeai as genai
import json
import re
import os
from tools import search_products, estimate_shipping, apply_discount, compare_prices, get_return_policy

API_KEY = os.getenv("GEMINI_API_KEY")

# Set up Gemini Pro API Key
genai.configure(api_key=API_KEY)

def extract_intent(user_query):
    """Extract structured intent from user query using Google Gemini Pro."""
    
    prompt = f"""
    Extract structured intent from the user query and return ONLY valid JSON format. 
    Do NOT include extra text, explanations, or comments. The response must be a JSON object with one or more of the following keys:
    - "search": {{"product_name": str, "color": str, "size": str, "max_price": int}} 
    - "discount": {{"promo_code": str}} (Example: "SAVE10", "WINTER15")  
    - "shipping": {{"destination": str}} 
    - "comparison": {{"product_name": str}} (Ensure the product name is clear and matches available products)
    - "return_policy": {{"retailer": str}} 

    Example:
    User Query: "Find a red floral skirt under $40 in size S."
    Expected Output: {{"search": {{"product_name": "Floral Skirt", "color": "Red", "size": "S", "max_price": 40}}}}

    Query: "{user_query}"
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    # Extract valid JSON from the response
    try:
        structured_data = json.loads(response.text.strip())
    except json.JSONDecodeError:
        structured_data = {}  # Default to an empty dictionary if parsing fails

    return structured_data

def parse_price(price_str):
    """Helper function to extract numeric price from a string, or return None."""
    match = re.search(r'\d+(\.\d{1,2})?', price_str)
    if match:
        return float(match.group(0))
    return None

def shopping_agent(user_query):
    """General shopping agent to handle a wide variety of queries."""
    response = ""
    extracted_data = extract_intent(user_query)

    global last_searched_product  # Store last searched product
    search_results = []

    # Search for a product if "search" intent is extracted
    if "search" in extracted_data:
        search_details = extracted_data["search"]
        
        product_name = (search_details.get("product_name", "") or "").strip().lower()
        color = (search_details.get("color", "") or "").strip().capitalize()
        size = (search_details.get("size", "") or "").strip().upper()
        max_price = search_details.get("max_price", None)
        
        # Ensure max_price is valid
        max_price = max_price if max_price is not None else float('inf')

        # Attempt to search the product dynamically
        search_results = search_products(product_name, color or None, size or None, max_price)
        response += f"🔍 Searching for: {product_name.capitalize()}, Color: {color}, Size: {size}, Max Price: ${max_price if max_price != float('inf') else 'Any'}\n"

        if search_results:
            last_searched_product = search_results[0]  # Store first found product
            response += f"Found a match: {search_results[0]['name']} from {search_results[0]['site']} for ${search_results[0]['price']}.\n"
        else:
            response += "No matching products found.\n"

    # Apply discount if "discount" intent is extracted and product is found
    if "discount" in extracted_data and last_searched_product:
        promo_code = extracted_data.get("discount", {}).get("promo_code", "").strip()

        if promo_code:
            discounted_price = apply_discount(last_searched_product["price"], promo_code)
            response += f"Applying promo code {promo_code} results in a final price of ${discounted_price} for the last searched item.\n"
        else:
            response += "No valid promo code available.\n"

    # Process shipping estimate if "shipping" intent is extracted
    if "shipping" in extracted_data:
        destination = extracted_data["shipping"].get("destination", "").strip() or "New York"
        shipping_info = estimate_shipping(destination, "Friday")
        response += f"Shipping to {destination}: Delivery in {shipping_info['delivery_days']} days for ${shipping_info['cost']}.\n"

    # Compare prices if "comparison" intent is extracted and product was found
    if "comparison" in extracted_data and last_searched_product:
        product_name = extracted_data.get("comparison", {}).get("product_name", "").strip().lower() or "unknown product"
        price_results = compare_prices(product_name)

        if not price_results:
            response += f"No price comparison found for '{product_name}'.\n"
        else:
            response += "Price comparison results:\n"
            for result in price_results:
                response += f" - {result['site']}: ${result['price']}\n"

    # Process return policy if "return_policy" intent is extracted
    if "return_policy" in extracted_data:
        retailers = extracted_data["return_policy"].get("retailer", "")
        if isinstance(retailers, str):
            retailers = [retailers]  # Convert to list if single retailer
        for site in retailers:
            return_policy = get_return_policy(site)
            response += f"Return policy for {site}: {return_policy}\n"

    # Return the final response if available, else provide a fallback message
    return response if response else "I'm not sure how to help with that."
