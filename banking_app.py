def check_balance(balance):
    print(f"Your current balance is: Rs.{balance}")
def deposit(balance):
    input_amount = input("Enter the amount to deposit: ")
    amount = float(input_amount)
    if amount <= 0:
            print("Please enter a positive amount.")
    else:
        balance += amount
        print(f"Rs.{amount} deposited successfully.")
    return balance
        
def withdraw(balance):
    input_amount = input("Enter the amount to withdraw: ")
    amount = float(input_amount)
    if amount <= 0:
            print("Please enter a positive amount.")
    elif amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print(f"Rs.{amount} withdrawn successfully.")
    return balance

balance = 0.00
print("Welcome to the ABC Banking App!")
while True:
    print("\nPlease choose an option:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        check_balance(balance)
    elif choice == 2:
        balance = deposit(balance)
    elif choice == 3:
        balance =  withdraw(balance)
    elif choice == 4:
        print("Thank you for using the Banking App. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")