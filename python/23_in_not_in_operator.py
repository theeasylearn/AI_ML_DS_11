countries = "afghanistan, armenia, azerbaijan, bahrain, bangladesh, bhutan, brunei, cambodia, china, cyprus, georgia, india, indonesia, iran, iraq, israel, japan, jordan, kazakhstan, kuwait"

word = "india"
result = word in countries 
print(result)

result = word not in countries 
print(result)

word = "sri lanka"
result = word in countries 
print(result)

result = word not in countries 
print(result)

fruits = ["apple", "banana", "orange", "mango", "grapes", "pineapple", "papaya", "watermelon", "strawberry", "cherry"]

item = "banana"

print(item in fruits)
print(item not in fruits)

places = ("varanasi", "haridwar", "rishikesh", "kedarnath", "badrinath", "tirupati", "dwarka", "jagannath puri", "mathura", "ayodhya")

location = "ayodhya"
print(location in places)
print(location not in places)