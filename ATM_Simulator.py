Balance= 1000

while True:

    print(f"""

  -------------ATM MENU---------------
  1.Check Balance
  2.Deposit Money
  3.Withdraw Money
  4.Exit
  
  """)

    choice=int(input("Enter a choice (1,2,3,4):"))

    if choice==1:
        print(f"Current balance:{Balance}")
    elif choice==2:
        amount=int(input("Enter deposit amount:"))
        if amount > 0:
            Balance=Balance+amount
            print(f"{amount} amount deposited successfully!! ")
            print(f"current balance:{Balance}")
        else:
            print("invalid amount")

    elif choice==3:
        amount=int(input("Enter withdrawal amount:"))
        
        if amount<=0:
            print("invalid amount")
        elif amount > Balance:
             print("insufficient balance")
        else:    
            Balance = Balance - amount
            print(f"{amount} withdraw successfullt!!")
            print(f"current balance:{Balance}")
      
    elif choice==4:
        print("Thank you for using the ATM!")
        break
    else:
        print("Invalid choice!!")


