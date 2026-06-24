import connection as database 

#create sql statement 
sql = "select id,name,price,quantity from product order by id desc"

#create cursor 
cursor = database.connect.cursor(dictionary=True)

#run sql statement 
cursor.execute(sql)

#fetch one row as dictionary
# first = cursor.fetchone()
# print(first)

#fetch and display all rows 
table = cursor.fetchall()

print(f"{'id':<10} {'name':72} {'price':12} {'quantity':12}")
print("-"*110)
count = 0
for row in table:
    print(f"{row['id']:<10} {row['name']:64} {row['price']:12} {row['quantity']:12}")
    count= count + 1
    if count == 25:
        input("press any key")
        count = 0