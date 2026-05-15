filename = input("Enter file name to read") #states.txt
mode = 'r' 
#file open
file = open(filename,mode) 
content = file.read()
print(content)
file.close() 
