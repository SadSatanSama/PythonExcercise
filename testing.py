str=input("enter the word: ")

s1=str
if s1==s1[::-1]:
    print("palindrome")
else:
    print("not palindrome")

s = str
reversed_s = ''.join(reversed(s))
if s == reversed_s:
    print("Palindrome")
else:
    print("Not a Palindrome")   
