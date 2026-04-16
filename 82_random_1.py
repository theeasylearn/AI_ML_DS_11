#import module as aliasname
import random as rd 
print("random number between 0 and 1",rd.random())
print("random float number between 10 and 99",rd.uniform(10,99))
print("random integer number between 10 and 99",rd.randint(10,99))
print("random integer number between 10 and 100 divisible by 10 ",rd.randrange(10,100,10))

colors = ['red', 'yellow','green','blue']
#pick any one color randomly 

print("any one color ",rd.choice(colors))
print("any two color ",rd.choices(colors,k=2))

number_list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
print(number_list)

#randomly change all item's position
rd.shuffle(number_list)
print("list after shuffle ",number_list)

countries = ["India", "USA", "Canada", "Australia", "Germany"]
print(countries)

#shuffle and copy countries into list 
new_countries = rd.sample(countries,len(countries))
print(countries,new_countries)