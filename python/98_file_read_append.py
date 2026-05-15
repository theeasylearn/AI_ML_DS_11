filename_1 = "numbers.txt"
mode_1 = 'r'

filename_2 = 'even.txt'
filename_3 = 'odd.txt'

file2 = open(filename_2,'w')
file3 = open(filename_3,'w')

#file read 
with open(filename_1,mode_1) as file1:
    for line in file1:
        print(line.strip()) 
        number = int(line)
        reminder = number % 2
        if reminder == 0:
            file2.write(line)
        else:
            file3.write(line)
file2.close()
file3.close()            
print('files has been created')