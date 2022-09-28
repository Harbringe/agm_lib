# Write a python program that computes the net amount of a bank account based on the transaction log from console input. 
# The transaction log format is shown as following: 
# d as deposit money
# t as transaction money

# 1. Withdrawal is not allowed if the balance is going negative
# 2. Write a function for withdrawal and deposit

d = float(input("How much would u like to deposit?\n"))
t = float(input("How much would would u like to transact?\n"))
choice = input("Do you want to deposit money or transact it?\n")

# <--- deposit --->
if choice == "deposit" or choice == "Deposit" or choice == "d" or choice == "D":
    k = float(input("Enter the amount to be deposited: "))
    d = k + d

# <--- withdrawal --->
elif choice == "Tran sact" or choice == "transact" or choice == "t" or choice == "T":
    if d > t:
        d = d - t
        print(f"You successfully withdrew {t}. You have {d} left.")
    else: 
        print(f"Transaction ammount ({t}) is more than your account balance ({d}). You cannot transact the said amount.")
else: 
    print("Enter a valid choice")
