n=int(input("enter the length: " ) )
for i in range (n):
    element=float(input("input element: "))
    array.append(element)

for i in range(len(array)-1):
    if array[i]>array[i+1]:
        v=array[i] 
        array[i]=array[i+1]
        array[i+1]=v
print(array)   

def selection_sort(n):
    for i in range(n):
        for j in range (i+1,n):
            if array[j]<array[i]:
                array[j],array[i] = array[i],array[j]
    print(array)
selection_sort(n)
