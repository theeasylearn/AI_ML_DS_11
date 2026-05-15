filename = input("Enter file name to read") #states.txt
mode = 'r' 

#file open
file = open(filename,mode) 

#read text from file line by line 
for line in file:
    print(line.strip()) #remove new line character from both side of line
file.close() 
