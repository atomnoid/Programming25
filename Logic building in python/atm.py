print("welcome to atomnoid ATM machine")
pin = int(input("Enter you four digit pin:  "))
available_balance = 30000
print("1. Withdraw cash")
print("2. Balance Inquiry")
print("3. Deposit cash")
print("4. Fast cash")

x = int(input("enter your choice:  "))
if x==1:
    ammount = int(input("Enter the ammount you want to withdraw:  "))
    if ammount <= available_balance:
        print("Transaction successful", ammount)
    else:
        print("Insufficient balance")
elif x==2:
    print("Your available balance is: ", available_balance)
elif x==3:
    deposit = (int(input("Enter the ammmount you want to deposit: ")))
    print("Transaction successful")
    print("Your available balance is: ", available_balance + deposit)
elif x==4:
    print("1.5000")
    print("2.10000")
    print("3.15000")
    print("4.20000")
    option = int(input("enter your choice:  "))
    if (option == 1 and 5000< available_balance):
        print("Transaction successful")
    elif (option == 2 and 10000< available_balance):
        print("Transaction successful")
    elif (option == 3 and 15000< available_balance):
        print("Transaction successful")
    elif (option == 4 and 20000< available_balance):
        print("Transaction successful")
    else:
        print("Wrong choice")
else:
    print("Invalid pin")