import connection as database 
def getPrice(id):
    sql = "select price from product where id = %s";
    data = [id]
    cursor = database.connect.cursor(dictionary=True)
    cursor.execute(sql,data)
    table = cursor.fetchall()
    NoofRows = len(table)
    return NoofRows
 
def SearchProduct():
    name = input("Enter product name")
    sql = "select id,name,price,quantity from product where name like %s and is_deleted=0 order by id desc"
    ViewProducts(sql,name)
def AddProduct():
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

def ViewProducts(SQLCommand=None,name=None):
    #create cursor 
    cursor = database.connect.cursor(dictionary=True)
    if SQLCommand == None:
        #create sql statement 
        sql = "select id,name,price,quantity from product where is_deleted=0 order by id desc"
        cursor.execute(sql)
    else:
        sql = SQLCommand
        cursor.execute(sql, (f"%{name}%",))

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
def DeleteProduct():
    #create sql statement 
    sql = "update product set is_deleted=1 where id=%s"

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
def UpdateProduct():
        #create sql statement 
    sql = "update product set name=%s,price=%s,quantity=%s where id=%s"

    #accept input from user 
    id = int(input("enter product id"))
    name = input("Enter product name")
    price = int(input("enter product price"))
    quantity = int(input("enter product quantity"))

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