# Write a python program to compute following operations on a string
# 1. Display word with longest length 
# 2. To determine the freq of occurance of particular char in a string 
# 3. To check whether the given string is pallindrome 
# 4. To display the index of first appearance of the sub string 
# 5. To count the occurances of each word in given string


s = str(input("Please input a string: "))
list = []


# <--- Word with longest length --->
def longest_word(s):
    list = s.split(" ")
    '''
    longest = 0

    # print("Longest words are: ", end= " ")
    for word in list:
        if len(word) > longest:
            longest = len(word)
    for word in list:
        if longest == len(word):
            print("The longest word is: ", word)
            '''
    print(max(list))
longest_word(s)


# <--- Frequency of occurance of char --->
def freq(s):
    ct = input("Input a character: ")
    print(f"{ct} occured {s.count(ct)} times.")
    
freq(s)

# <--- Is palindrome-->
def pallindrome(s):
    s = s.replace(" ", "")
    rev_s = s[::-1]
    
    if s == rev_s:
        print("The string is a pallindrome")
    else:
        print("The string is not a pallindrome")

pallindrome(s)


# <--- First appearance of sub-string ---> 
def find_freq(s):   
    list = s.split(" ")
    find_word = str(input("Enter the word you want to find: "))
    print("First appearance of sub-string", s.find(find_word))
    print("Frequency of occurance of ", find_word, s.count(find_word))
find_freq(s)

# <--- Occurances of each word --->
def occurance(s):
    list = s.split(" ")
    for word in list:
        occ = list.count(word)
        print(f"{word} occured {occ} times.")

occurance(s)



    
