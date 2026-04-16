# Defining a recursive function to calculate factorial
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# --- Main Program ---
# Number Input
num = int(input("Enter a number to find its factorial: ")) 

# Check for negative numbers to prevent a crash
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")