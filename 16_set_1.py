fruits = {'apple', 'banana', 'mango', 'orange', 'pineapple', 'apple', 'grape', 'papaya', 'banana', 'strawberry', 'mango', 'kiwi', 'apple', 'orange', 'watermelon', 'grape', 'banana', 'peach', 'mango', 'apple', 'cherry', 'papaya', 'pineapple', 'banana', 'apple'}

print(fruits)

unique_fruits = list(fruits) #convert it into list 
print(unique_fruits)

vegis = ['potato', 'tomato', 'onion', 'carrot', 'cabbage', 'potato', 'spinach', 'brinjal', 'cauliflower', 'tomato', 'capsicum', 'potato', 'peas', 'carrot', 'onion', 'cucumber', 'spinach', 'brinjal', 'potato', 'beans', 'tomato', 'cauliflower', 'onion', 'carrot', 'potato']

print(vegis)

#convert it into set 
unique_vegis = set(vegis)
print(unique_vegis)

set1 = {1, 2, 3, 4, 5}
set2 = {3,4,5,6,7}

print(set1.union(set2)) # each value one time 1,2,3,4,5,6,7
print(set1.intersection(set2)) # each value one time 3,4,5
print(set1.difference(set2)) # each value one time 1 2
set1.add(10)
set1.remove(5)
print(set1)
