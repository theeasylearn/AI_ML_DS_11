#dictionary 
book = {} #empty dictionary
print(book)

#add key value pair
book['name'] = "Learning Data Science & ML"
book['chapter'] = [1,2,3,4,5] #chapter is list 
book['topics'] = ('introduction to ML & DS','python','Library','Algorithms','models') # tuples in list 
book['price'] = 1000

print(book)


book['topics'][0] = 'index' #error as topics is tuple 
book['chapter'][0] = 10 #change is possible chapter is list 
del book['price'] #scaler value 

