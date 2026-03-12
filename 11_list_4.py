marks = [50,80,40,90,35,100,90]
print(marks)
position = marks.index(100)
print("position of 100 ",position)

# position = marks.index(99)
# print("position of 99 ",position)

temp = marks.count(90)
print("Count of temp ",temp)

marks.sort()
print(marks)

marks.reverse()
print(marks)

# marks2 = marks #wrong way 
marks2 = marks.copy()

marks2.clear() 
print(marks)
print(marks2)
