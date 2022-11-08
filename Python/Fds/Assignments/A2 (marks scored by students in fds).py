# Write a Python program to store marks scored in subject “Fundamental of Data
# Structure” by N students in the class. Write functions to compute following:
# a) The average score of class
# b) Highest score and lowest score of class
# c) Count of students who were absent for the test
# d) Display mark with highest frequency

import statistics
class_limit= int(input("Input the the number of students in class: "))
n = int(input("Input the the number of students present at test: "))

# <--- Input --->  
Student_list = []
for i in range(1, n+1): 
    Student_list.append(float(input("Input marks: ")))

print(Student_list)

# < --- Built-in funtions --- >

# <--- ( a ) ---> 
print("The average score of class is: ", sum(Student_list)/n)

# <--- ( b ) --->
print("The highest score in class is: ", max(Student_list), "\nThe least score in class is: ", min(Student_list))

# <--- ( c ) ---> 
print("The number of student absent for the test: ", class_limit - n)

# <--- ( d ) --->
print("The marks with highest frequency: ", statistics.mode(Student_list))


# < --- User defined Functions --- >
'''

# <--- ( a ) --->
def average():
    print(average = sum(Student_list)/n)

# <--- ( b ) ---> 
def Maximum():
    maximum = 0
    for a in Student_list:
        if a > maximum:
            maximum = a
    print(maximum)

def Minimum():
    minimum = 0
    for a in Student_list:
        if a < minimum:
            minimum = a
    print(minimum)
# <--- ( d ) ---> 
def highest_freq():
    the_num = Student_list[0]
    for a in Student_list:
        freq = Student_list.count(a)
    print(a)

highest_freq()

'''
