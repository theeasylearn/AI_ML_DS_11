numbers = [1, 2, 3, 4, 5]

#generate square 
#create empty list 
# square =  [] 
# for num in numbers:
#     temp = num * num 
#     square.append(temp)
# or using anonyms lambda 
square = map(lambda num: num * num,numbers)
#map always return iterables which can not be directly print
# print(square)you can not directly print iterables 
print(list(square))

