bal = int(input("Enter the balance :"))
amt = int(input("Enter amount to withdraw : "))


if(amt < bal):
    if(amt % 10 == 0):
        bal = bal - amt
        print("Withdrawal successful")
        print(bal)
    else:
        print("Amount must be multiple of 10")

else :
     print("Insufficient balance")




