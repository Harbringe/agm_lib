a = [1, 23, 42, 52, 53, 64, 75, 76, 81, 101]

element = int(input("Enter an element you would want to find in the array: "))

def binary_search(a, element):
    found = False
    first = 0 
    last = len(a) - 1
    
    while(first <= last and not found):
        mid = (first + last) // 2

        if element == a[mid]:
            found = True
            print(mid) 
            print("Element Found")
        else:
            if element < a[mid]:
                last = mid
            else: 
                first = mid
    
binary_search(a, element)
