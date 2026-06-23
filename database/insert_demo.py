import connection as database 

#create sql statement 
sql = "insert into product (name,price,quantity) values (%s,%s,%s)"
# %s is called placeholder 

#accept input from user 
name = input("Enter Product name")
price = int(input("Enter product price"))
quantity = int(input("Enter quantity"))

#create list whose size must be equal to total placeholder 
values = [name,price,quantity]
#create cursor 
cursor = database.connect.cursor()

#run sql statement 
cursor.execute(sql,values)

#save changes 
database.connect.commit()

print("product inserted")