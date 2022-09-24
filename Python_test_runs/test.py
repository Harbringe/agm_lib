#f2 = open("text.txt" )
#print(f2.read(5))
#it will return the first 5 characters in the file

#print(f2.readline())
# it will return one line of the file 
# by calling readline two times you can read first two lines of the file 
# if you want to return all the contents of the file it can be done by using loop
# close file 
# it is good practice to close the file after opening and performing actions on it 
#f2.close()
# you should always close your file as in somce cases due to buffering changes made to a file may not show until u close the file 

f= open('.\ documents\readme.txt', 'w') 
f.write('readme')
f.close()