#FILTER FUCTION EXERCISE

# Easy: No Negativity Allowed
# Task: Use filter() to remove all negative numbers from a list, keeping only zero and positive numbers.
# Input: numbers = [-5, 2, -3, 0, 9, -1]
# Expected Output: [2, 0, 9]

numbers = [-5, 2, -3, 0, 9, -1]
function=filter(lambda num: num>=0 , numbers)
print(list(function))

# Medium: Palindrome Finder
# Task: A palindrome is a word that reads the same forwards and backwards. Use filter() to extract only the palindromes from a list of words. (Hint: In Python, you can reverse a string using slicing: word[::-1]).
# Input: words = ["radar", "python", "level", "world", "racecar"]
# Expected Output: ['radar', 'level', 'racecar']

words = ["radar", "python", "level", "world", "racecar"]
filtered_words=filter(lambda word: word==word[::-1],words) #word==word[::-1] is the condition to check if the word is a palindrome or not.
print(list(filtered_words))

# Hard: The HR Filter
# Task: You have a list of employee dictionaries. Use filter() to find employees who meet two conditions: They must be in the "Engineering" department, AND their salary must be strictly greater than 70,000.
# Input: ```python
# employees = [
# {"name": "Alice", "dept": "Engineering", "salary": 80000},
# {"name": "Bob", "dept": "HR", "salary": 60000},
# {"name": "Charlie", "dept": "Engineering", "salary": 65000},
# {"name": "Diana", "dept": "Engineering", "salary": 95000}
# ]
# Expected Output: [{'name': 'Alice', 'dept': 'Engineering', 'salary': 80000}, {'name': 'Diana', 'dept': 'Engineering', 'salary': 95000}]

employees = [
{"name": "Alice", "dept": "Engineering", "salary": 80000},
{"name": "Bob", "dept": "HR", "salary": 60000},
{"name": "Charlie", "dept": "Engineering", "salary": 65000},
{"name": "Diana", "dept": "Engineering", "salary": 95000}
]
filtered_employees=filter(lambda emp: emp["dept"]=="Engineering" and emp["salary"]>70000, employees)
print(list(filtered_employees))