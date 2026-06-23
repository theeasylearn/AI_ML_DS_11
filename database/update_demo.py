import connection as database 

#create sql statement 
sql = "update product set name=%s,price=%s,quantity=%s where id=%s"

#accept input from user 
name = input("Enter product name")
price = int(input("enter product price"))
quantity = int(input("enter product quantity"))
id = int(input("enter product id"))

#create list 
values = [name,price,quantity,id]

#create cursor 
cursor = database.connect.cursor()

#execute sql 
cursor.execute(sql,values)

#save changes 
database.connect.commit()
if cursor.rowcount !=0:
    print("product updated")
else:
    print("Product not found")

