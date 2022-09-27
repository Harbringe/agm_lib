
# write function for the following
# Aim: wap to store marks of students and compute average highest lowewst and frequency of class

import statistics
class_limit= int(input("Input the the number of students in class: "))
n = int(input("Input the the number of students present at test: "))

Student_list = []

for i in range(1, n+1): 
    Student_list.append(float(input("Input marks: ")))

print(Student_list)



print("The average score of class is: ", sum(Student_list)/n)
print("The highest score in class is: ", max(Student_list), "\nThe least score in class is: ", min(Student_list))
print("The number of student absent for the test: ", class_limit - n)
print("The marks with highest frequency: ", statistics.mode(Student_list))

'''

def average():
    print(average = sum(Student_list)/n)

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

def highest_freq():
    the_num = Student_list[0]
    for a in Student_list:
        freq = Student_list.count(a)
    print(a)

highest_freq()

'''
