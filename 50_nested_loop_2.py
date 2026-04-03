# print factorial of 1 to 6 in reverse order 
# 6 ! 6 x 5 x 4 x 3 x 2 x 1 =  720
# 5 ! 5 x 4 x 3 x 2 x 1 =  120
# 4 ! 4 x 3 x 2 x 1 =  24
# 3 ! 3 x 2 x 1 =  12
# 2 ! 2 x 1 =  6
# 1 ! 1 =  1
# 720 120 24 12 6 1
count = 6

while count>=1: #outer loop
    number = count 
    result = number 

    while number>1: #inner loop 
        number = number - 1
        result = result * number
    print(result)
    count = count - 1

