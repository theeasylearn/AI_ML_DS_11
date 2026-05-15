tuple = ("Ram",100,3.14,True,False)
small_tuple = ("Sita",25)
print(tuple)
print(small_tuple)

print(tuple[0]) #Ram 
print(tuple[1:3]) # 100 3.14
print(tuple[2:]) #3.14 True False

# tuple[0] = "Ram raghav"
# del tuple[0]
print(tuple.count("ram"))
print(tuple.index(3.14))