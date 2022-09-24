n=int(input("Enter the number of numbers to be inserted: "))
Condition=True
while True:
    input_string=input("Enter the list of numbers: ")
    list1=list(int(x) for x in input_string.split(","))
    r=len(list1)
    if r==n:
        print(list1, "are the numbers you inserted in the list.")
        break
    else:
        print("Enter", n, "numbers only.")
        Condition=False

print(f" {max(list1)} is the highest number in the list")
print(min(list1), "is the lowest number in the list")
print(sum(list1), "is the sum of all numbers in the list")
print(sum(list1)/n, "is the avg of all numbers in the list")
