from agent import shopping_agent
import time

# Test cases
queries = [
    "Find a red floral skirt under $40 in size S.",
    "What is the shipping cost to New York from Zara?",
    "Can I use the SAVE10 discount on the leather jacket at Nordstrom?",
    "Compare prices for a casual denim jacket.",
    "What is the return policy for Macy's?",
    "Find a black leather jacket under $100 in size M. Can I use the promo code ‘WINTER20’?",
    "I need a pair of running shoes (size 10) under $80. Can they arrive in Texas by Thursday with the SAVE10 discount?",
    "I found a navy blue hoodie for $60 on Nordstrom. Can I get a better price? What’s the return policy on Nordstrom?",
    "Looking for a white summer dress under $50, size S. Can it arrive in California by Saturday with a discount?",
    "I found a ‘graphic t-shirt’ for $25 on Urban Outfitters. Are there better deals elsewhere? Can I apply SAVE10?",
    "Find a pair of black skinny jeans under $60 in size 32. Also, check the return policies.",
    "I need a formal blazer in size L under $150, and it must arrive in New York by Wednesday. Can I use any promo codes from J.Crew?",
    "I want a brown leather belt under $40 from Mango. Find a fast-shipping option to California and compare prices with other brands.",
    "I want a pair of red heels (size 7) under $90, check if Zara has it, apply SUMMER20 if available, and estimate shipping to Texas.",
    "I’m buying a trench coat for $120 from ASOS. Can I use any promo codes? What’s the return policy? How much is shipping to New York?",
    "Find a red plaid shirt under $45 at H&M. Check if competitors like Gap have a better price and see if it can ship to Texas by Friday.",
    "I want to buy from ASOS, Zara, and Mango. What are their return policies?",
    "I found a beige trench coat for $95 on Mango. Check for a better price, apply SUMMER20, and see if it can arrive in New York by Friday.",
    "I need three cotton t-shirts under $30 each. Can I get a bulk discount from Uniqlo? Also, find fast shipping to California.",
    "Looking for a warm winter coat under $120 in size M. Can it ship to New York in 3 days? Any promo codes from Uniqlo? Also, compare prices with competitors like Macy's."
]

for query in queries:
    print(f"User: {query}")
    print("Agent:", shopping_agent(query))
    print("-" * 40)
    time.sleep(3)
  