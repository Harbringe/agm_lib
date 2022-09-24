import math 

n = int(input("Enter a number: "))

print(f"{math.sqrt(n)} is the square root of {n}")
print(f"{pow(n,2)} is the square of {n}")
print(f"{pow(n,3)} is the cube of {n}")

if n > 1: 
    for i in range(2, n):
        if(n % i == 0):
            print(f"{n} is not a prime number.")
            break
    else: 
        print(f"{n} is a prime number.")

print(f"{math.factorial(n)} is the factorial of {n}")

print("Prime factors are: ")
while n % 2 == 0:
    print (2) 
    n = n / 2
for i in range(3,int(math.sqrt(n))+1,2): 
    while n % i== 0:
        print (i) 
        n = n / i 
if n > 2: 
    print (n)