#MAP FUNCTION EXERCCISE

# Easy: The Yelling Machine
# Task: You have a list of lowercase words. Use map() to convert all of them to uppercase.
# Input: words = ["apple", "banana", "cherry"]
# Expected Output: ['APPLE', 'BANANA', 'CHERRY']

words = ["apple", "banana", "cherry"]
upper_words=map(lambda x: x.upper(), words)
print(list(upper_words))

# Medium: Domain Extractor
# Task: You have a list of email addresses. Use map() to extract just the domain name (everything after the @ symbol) from each email. (Hint: the string .split() method will be your friend here).
# Input: emails = ["user@example.com", "admin@google.com", "info@python.org"]
# Expected Output: ['example.com', 'google.com', 'python.org']

emails = ["user@example.com", "admin@google.com", "info@python.org"]
domains=map(lambda x: x.split("@")[1], emails)
print(list(domains))

# Hard: Shopping Cart Totals
# Task: You have a list of dictionaries representing items in a shopping cart. Each dictionary has a price and a quantity. Use map() to calculate the total cost for each item line (price multiplied by quantity).
# Input: ```python
# cart = [
# {"item": "apple", "price": 1.20, "qty": 3},
# {"item": "banana", "price": 0.50, "qty": 5},
# {"item": "milk", "price": 3.00, "qty": 1}
# ]
# Expected Output: [3.6, 2.5, 3.0]

cart = [
{"item": "apple", "price": 1.20, "qty": 3},
{"item": "banana", "price": 0.50, "qty": 5},
{"item": "milk", "price": 3.00, "qty": 1}
]
total_amount=map(lambda x: round(x["price"]*x["qty"], 2), cart)
print(list(total_amount))