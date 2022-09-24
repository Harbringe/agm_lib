marklist = {
    "course_1" : 0,
    "course_2" : 0,
    "course_3" : 0,
    "course_4" : 0,
    "course_5" : 0 
}

marklist["course_1"] = float(input("Input marks for course_1: "))
marklist["course_2"] = float(input("Input marks for course_2: "))
marklist["course_3"] = float(input("Input marks for course_3: "))
marklist["course_4"] = float(input("Input marks for course_4: "))
marklist["course_5"] = float(input("Input marks for course_5: "))

print(marklist)
minimum = min(list(marklist.values()))
percent = (sum(list(marklist.values()))/500) * 100

print(f"\nScore: {percent}")

if minimum >= 40: 
    if percent >= 75:
        print("Passed with distinction.")
    elif percent >= 60 and percent < 75: 
        print("Passed with first division.")
    elif percent >= 50 and percent < 60:
        print("Passed with second grade.")
    elif percent >= 40 and percent < 50: 
        print("Passed with third grade.")
    else:
        print("Error")
else:
    print("Failure")
    

