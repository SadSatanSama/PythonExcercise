# Dictionary containing the student names and marks
student = {
    "Alice": 85,
    "Bob": 90,
    "William": 82
}

# Ask the user for a student's name to run a search query
user_input = input("Enter a student's name to get their marks: ").title() #.title() used to generalize the letters

# using membership operator to see if the name exists
if user_input in student:
    print(f"{user_input}'s marks: {student[user_input]}") 
else:
    print("Student not found.")
