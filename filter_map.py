#LAMBDA FUNCTION
# lambda arguments: expression

add=lambda num:num+1
add.__doc__="""here num is the argument and num+1 is the expression which is executed when the function is called.
"""
result=add(5)
print(result)
print(help(add))

#FILTER FUNCTION

nums=[1,2,3,4,5,6,7,8,9]
func=filter (lambda num: True if num%2==0 else False,nums) #filter function takes two arguments, first is the function and second is the iterable. here we are using lambda function as the first argument and nums as the second argument.
print(list(func)) #filter function returns an iterator, so we need to convert it to a list to see the output.

#MAPS FUNCTION
nums=[1,2,3,4,5,6,7,8,9]
func=map(lambda num: num**2, nums) #map function takes two arguments, first is the function and second is the iterable. here we are using lambda function as the first argument and nums as the second argument.
print(list(func)) #map function returns an iterator, so we need to convert it to a list to see the output.

#SORTED FUNCTION
### SORT THE USERS ACCORDING TO THEIR AGE IN ASCENDING ORDER ###
user=[
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 35}
]
sorted_user=sorted(user, key=lambda x: x["age"])
reversed_sorted_user=sorted(user, key=lambda x: x["age"], reverse=True) #if you want to sort in descending order then you can use reverse=True as the second argument in sorted function.
print(sorted_user) #sorted function takes two arguments, first is the iterable and second is the key. here we are using lambda function as the second argument to sort the users according to their age.
print(reversed_sorted_user)