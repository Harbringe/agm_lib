# Write a Python program that computes the net amount of a bank account based a
# transaction log from console input. The transaction log format is shown as following: D
# 100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for
# withdraw and deposit) D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
#   D 300, D 300 , W 200, D 100 Then, the output should be: 500

# <---Input ---> 
d = float(input("How much would u like to deposit?\n"))
w = float(input("How much would would u like to withdraw?\n"))
choice = input("Do you want to deposit money or transact it?\n")

# <--- deposit --->
if choice == "deposit" or choice == "Deposit" or choice == "d" or choice == "D":
    k = float(input("Enter the amount to be deposited: "))
    d = k + d

# <--- withdrawal --->
elif choice == "Withdraw" or choice == "withdraw" or choice == "w" or choice == "W":
    if d > w:
        d = d - w
        print(f"You successfully withdrew {w}. You have {d} left.")
    else: 
        print(f"Transaction ammount ({w}) is more than your account balance ({d}). You cannot transact the said amount.")
else: 
    print("Enter a valid choice")
