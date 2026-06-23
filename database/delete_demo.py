import connection as database 

#create sql statement 
sql = "delete from product where id=%s"

#accept input 
id = int(input("Enter product id "))
#create list 
values = [id]

#create cursor 
cursor = database.connect.cursor()

#run sql command
cursor.execute(sql,values)

#save changes
database.connect.commit()
if cursor.rowcount!=0:
    print("product deleted")
else:
    print("product not found")

