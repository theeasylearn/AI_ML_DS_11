import products as p
import connection as database 
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
        for row in table:
            print(f"{row['item_id']:<10} {row['name']:<60} {row['rate']:<10} {row['quantity']:<10} {row['quantity'] * row['rate']:<12}")
    key = input("Press any key to continue")
while True:
    print("\nPress 1 for Product management")
    print("Press 2 for Bill management")
    print("Press 3 for Report management")
    print("Press 0 for Exit")
    
    choice = int(input("enter your choice: "))
    
    if choice < 0 or choice > 3:
        print("invalid choice")
    else:
        if choice == 1:
            while True:
                # Add, Edit, Delete, View, Search Product 
                print("\nPress 1 to add new product")
                print("Press 2 to edit product")
                print("Press 3 to delete product")
                print("Press 4 to view product")
                print("Press 5 to search product")
                print("Press 0 to exit to main menu")
                
                product_choice = int(input("enter your choice: "))
                
                if product_choice < 0 or product_choice > 5:
                    print("invalid choice")
                else:
                    if product_choice == 1:
                        p.AddProduct()
                    elif product_choice == 2:
                        p.ViewProducts()
                        p.UpdateProduct()
                    elif product_choice == 3:
                        p.ViewProducts()
                        p.DeleteProduct()
                    elif product_choice == 4:
                        p.ViewProducts()
                    elif product_choice == 5:
                        p.SearchProduct()
                    else:
                        print("exit to main menu")
                        break  # break inner loop

        elif choice == 2:
            while True:
                # Add Item, Delete Item, Search Item, Generate Bill, View Bill
                print("\nPress 1 to add item to bill")
                print("Press 2 to delete item from bill")
                print("Press 3 to search item in bill")
                print("Press 4 to generate bill")
                print("Press 5 to view all bill items ")
                print("Press 0 to exit to main menu")
                
                bill_choice = int(input("enter your choice: "))
                
                if bill_choice < 0 or bill_choice > 5:
                    print("invalid choice")
                else:
                    if bill_choice == 1:
                        AddBillItem()
                    elif bill_choice == 2:
                        print("let us delete item from bill")
                    elif bill_choice == 3:
                        print("let us search item in bill")
                    elif bill_choice == 4:
                        print("let us generate bill")
                    elif bill_choice == 5:
                        DisplayBillItem()
                    else:
                        print("exit to main menu")
                        break  # break inner loop

        elif choice == 3:
            while True:
                # Daily, Weekly, Monthly, Product, Sales Reports
                print("\nPress 1 to generate daily report")
                print("Press 2 to generate weekly report")
                print("Press 3 to generate monthly report")
                print("Press 4 to generate product report")
                print("Press 5 to generate sales report")
                print("Press 0 to exit to main menu")
                
                report_choice = int(input("enter your choice: "))
                
                if report_choice < 0 or report_choice > 5:
                    print("invalid choice")
                else:
                    if report_choice == 1:
                        print("let us generate daily report")
                    elif report_choice == 2:
                        print("let us generate weekly report")
                    elif report_choice == 3:
                        print("let us generate monthly report")
                    elif report_choice == 4:
                        print("let us generate product report")
                    elif report_choice == 5:
                        print("let us generate sales report")
                    else:
                        print("exit to main menu")
                        break  # break inner loop

        else:
            print("exit from program")
            break