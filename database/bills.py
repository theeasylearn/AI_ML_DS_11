import connection as database 
import products as p 
def AddBillItem():
    #accept input from user 
    p.ViewProducts()
    id = input("Enter Product id")
    # price = int(input("Enter product price"))
    # fetch price of the given product id 
    result = p.getPrice(id) #get primary method may return 0 or tuple
    #check result is normal variable or tuple
    if isinstance(result,tuple) == False and result == 0: #product not found
        print("Product not found")
    else:
        price, stock = result
        quantity = int(input("Enter quantity"))
        if quantity>stock:
            print(f"sorry, available stock is {stock} unit")
        else:
            #create list whose size must be equal to total placeholder 
            #create sql statement 
            sql = "INSERT INTO `bill_items`(productid,quantity,rate) VALUES (%s,%s,%s)"
            # %s is called placeholder 
            values = [id,quantity,price]
            #create cursor 
            cursor = database.connect.cursor()

            #run sql statement 
            cursor.execute(sql,values)

            #save changes 
            database.connect.commit()

            print("Item inserted")
    key = input("Press any key to continue")
def SearchItemInBill():
    name = input("Enter Item(product) Name")
    sql = "SELECT bi.id 'item_id',name,rate,bi.quantity 'quantity' FROM `bill_items` bi, product p where p.id = productid and billid=0 and name like %s order by bi.id"
    #create cursor 
    cursor = database.connect.cursor(dictionary=True)

    #run sql command 
    cursor.execute(sql, (f"%{name}%",))

    #fetch all records 
    table = cursor.fetchall()
    if len(table) == 0:
        print("No bill item found")
    else:
        print(f"{'item_id':<10} {'name':<60} {'rate':<10} {'quantity':<10} {'total':<12}")
        print("_"*110)
        for row in table:
            print(f"{row['item_id']:<10} {row['name']:<60} {row['rate']:<10} {row['quantity']:<10} {row['quantity'] * row['rate']:<12}")
        print("_"*110)
def DisplayBillItem():
    sql = "SELECT bi.id 'item_id',name,rate,bi.quantity 'quantity' FROM `bill_items` bi, product p where p.id = productid and billid=0 order by bi.id"

    #create cursor 
    cursor = database.connect.cursor(dictionary=True)

    #run sql command 
    cursor.execute(sql)

    #fetch all records 
    table = cursor.fetchall()
    if len(table) == 0:
        print("No bill item found")
    else:
        print(f"{'item_id':<10} {'name':<60} {'rate':<10} {'quantity':<10} {'total':<12}")
        print("_"*110)
        GrandTotal=0
        ItemCount = 0
        for row in table:
            print(f"{row['item_id']:<10} {row['name']:<60} {row['rate']:<10} {row['quantity']:<10} {row['quantity'] * row['rate']:<12}")
            ItemCount+=1
            GrandTotal += (row['quantity'] * row['rate'])
        print("_"*110)
        #display total item and Grand Total
        print(f"No Of Items = {ItemCount:<58} Grand Total {GrandTotal:12}")
    key = input("Press any key to continue")
def DeleteItemFromBill():
    DisplayBillItem()
    itemid = int(input("Enter Bill Item id to delete item from bill"))
    sql = "delete from bill_items where id = %s"
    data = [itemid]

    #create cursor 
    cursor = database.connect.cursor()

    #run sql command
    cursor.execute(sql,data)

    database.connect.commit()
    print("Item Deleted successfully")
def GenerateBill():
    confirm = input("Are you sure? you want to generate bill (press y/Y)")
    if confirm.lower() == 'y':
        # Task 1 check is there any unbilled item / calculate total 
        # Task 2 reduce stock of each and every product added into bill_items 
        # Task 3 accept customer name, email, mobile 
        # Task 4 insert row into bill table
        # Task 4 update bill_item table billid field, use last row id of bill to update it
        
        #Task 1 
        sql = "SELECT sum(rate * quantity) as total FROM `bill_items` where billid=0"
        cursor = database.connect.cursor(dictionary=True)
        cursor.execute(sql)
        row = cursor.fetchone()
        total = row['total']
        if row['total'] == 0:
            print("No item found in bill")
        else:
            #Task 2 
            sql = "select productid, quantity from bill_items where billid=0"
            cursor.execute(sql)
            table = cursor.fetchall()
            for row in table:
                quantity = row['quantity']
                productid = row['productid']
                sql = "update product set quantity = quantity - %s where id = %s"
                data = [quantity,productid]
                cursor.execute(sql,data)
            #Task 3
            name = input("Enter customer name")
            mobile = input("Enter mobile")
            email = input("Enter email")
            paymentmode = input("Enter payment mode (1=cash, 2=credit)")
            sql = "insert into bill (customername,email,mobile,amount,paymentmode) values(%s,%s,%s,%s,%s)"
            data = [name,email,mobile,total,paymentmode]
            cursor.execute(sql,data)
            billid = cursor.lastrowid #get last inserted row id of bill table 
            # Task 4
            sql = "update bill_items set billid=%s where billid=0"
            data = [billid]
            cursor.execute(sql,data)
            print("BILL has been generated successfully")
            database.connect.commit()
    key = input("Press any to continue")
