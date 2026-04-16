import math # Importing the math module to access mathematical functions

# Number Input
num = float(input("Enter a number: ")) 
    
# Square Root
# Square root needs 0 or positive numbers
if num >= 0: 
    sqrt = math.sqrt(num)
    print(f"Square root: {sqrt}")
else:
    print("Cannot calculate the real square root of a negative number.")
        
# Natural Logarithm
# Logarithm strictly needs numbers greater than 0
if num > 0: 
    log = math.log(num)
    print(f"Logarithm: {log}")
else:
    print("Cannot calculate the real logarithm of zero or a negative number.")

# Sine in Radians
sin = math.sin(num)
print(f"Sine: {sin}")   
    