import os 

#print current working directory
print(os.getcwd()) 

#check car directory exists or not 
if os.path.exists('car') == True:
    print("car directory already exists....")
else:
    #create directory
    os.mkdir("car")

    print("Car directory created.....")

    #set car as current working directory
    os.chdir('car')
    print("now current working directory is ",os.getcwd()) 

    #delete car directory
    os.mkdir('tata')

    #remove directory tata
    os.rmdir('tata')

print('everything is done')