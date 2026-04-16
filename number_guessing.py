corr_num=69
for i in range(1,11):
    num=int(input("Please Guess the correct number: "))
    if num==corr_num:
        print("Your guess is right!! Game Over!!")
        break
    else:
        print("You guessed it wrong. Please try again")