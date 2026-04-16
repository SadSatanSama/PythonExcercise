def add(num):
    return num+1
result=add(5)
print(result)

# def greet(name):
#     print(f"hi there {name}! and a very good morning")
# greet("Arijit")
# greet("Prity")

# def squere(num):
#     return num**2
# num=int(input("Please enter your desired number: "))
# result_1=add(num)
# result_2=squere(result_1)
# print(f"the final output is {result_2}")

#PASSING A FUNCTION UNDER ANOTHER FUNTION AS ARGUMENT!!!
def squere(num):
    return num**2
num=int(input("Please enter your desired number: "))
result=squere(add(num)) #YOU CAN SEE ABOVE THAT add(num) is already an existing funtion which is now called under another funtion squere!!!
print(f"the final output is {result}")