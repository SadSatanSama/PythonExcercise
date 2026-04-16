#SORTED FUNCTION EXERCISE

# Easy: Sort by Length
# Task: You have a list of words. By default, sorted() will sort them alphabetically. Use a lambda key to sort them by their character length instead, from shortest to longest.
# Input: words = ["apple", "pie", "banana", "kiwi"]
# Expected Output: ['pie', 'kiwi', 'apple', 'banana']

words = ["apple", "pie", "banana", "kiwi"]
sorted_list=sorted(words, key=len)  # instead using sorted(words, key=lambda x: len(x))
print(sorted_list)

# Medium: Leaderboard
# Task: You have a list of tuples, where each tuple contains a player's name and their score. Use sorted() to create a leaderboard, sorting the players by their score in descending order(highest score first).
# Input: scores = [("Alice", 88), ("Bob", 95), ("Charlie", 72), ("Diana", 95)]
# Expected Output: [('Bob', 95), ('Diana', 95), ('Alice', 88), ('Charlie', 72)]

scores = [("Alice", 88), ("Bob", 95), ("Charlie", 72), ("Diana", 95)]
scoreboard=sorted(scores, key=lambda x: x[1], reverse=True)
print(scoreboard)

# Hard: The Double Sort

# Task: You have a list of dictionaries representing products. You need to sort them first by their category (alphabetically). If two items have the same category, you must sort them by price (highest price to lowest price). (Hint: A lambda function can return a tuple containing multiple sorting keys, like lambda x: (key1, key2)).

# Input: ```python
# products = [
# {"name": "Laptop", "category": "Electronics", "price": 1200},
# {"name": "Mouse", "category": "Electronics", "price": 25},
# {"name": "Desk", "category": "Furniture", "price": 300},
# {"name": "Chair", "category": "Furniture", "price": 150},
# {"name": "Monitor", "category": "Electronics", "price": 300}
# ]

# Expected Output: ```python
# [
# # Electronics first (alphabetical), then descending price
# {'name': 'Laptop', 'category': 'Electronics', 'price': 1200},
# {'name': 'Monitor', 'category': 'Electronics', 'price': 300},
# {'name': 'Mouse', 'category': 'Electronics', 'price': 25},
# # Furniture second (alphabetical), then descending price
# {'name': 'Desk', 'category': 'Furniture', 'price': 300},
# {'name': 'Chair', 'category': 'Furniture', 'price': 150}
# ]

products = [
{"name": "Laptop", "category": "Electronics", "price": 1200},
{"name": "Mouse", "category": "Electronics", "price": 25},
{"name": "Desk", "category": "Furniture", "price": 300},
{"name": "Chair", "category": "Furniture", "price": 150},
{"name": "Monitor", "category": "Electronics", "price": 300}
]
sorted_products=sorted(products, key=lambda x: (x["category"], -x["price"]))
print(sorted_products)

#BONUS
#ORGANIZE THE TICKETS ACCORDING TO THEIRR PRIORITY AND AS WELL AS THEIR ALPHABETICAL ORDER

priority_map = {"High": 1, "Medium": 2, "Low": 3}

tasks = [
    {"ticket": "Fix login bug", "priority": "Medium"},
    {"ticket": "Update logo", "priority": "Low"},
    {"ticket": "Server crash", "priority": "High"},
    {"ticket": "Change button color", "priority": "Low"}
]
prioity_output=sorted(tasks, key=lambda x: (priority_map.get(x["priority"]), x["ticket"]))
print(prioity_output)