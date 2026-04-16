# Using range() to create a list
my_list = list(range(1, 11))

# Using slicing method to extract desired numbers 
extracted_list = my_list[0:5]  

# Using slicing to reverse the extracted list
reversed_list = extracted_list[::-1]   

print(f"Original list: {my_list}")
print(f"Extracted first five elements: {extracted_list}")
print(f"Reversed extracted elements: {reversed_list}")