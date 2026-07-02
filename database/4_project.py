import products as p
import bills as b 
import connection as database
def SalesReport():
      #generate day wise sales report 
    sql = "SELECT DATE_FORMAT(billdate,'%d-%m-%Y') AS bill_date, DAYNAME(billdate) AS day_name, COUNT(id) AS total_bills, SUM(amount) AS total_sales FROM bill WHERE billdate BETWEEN ? AND ? GROUP BY DATE(billdate), DAYNAME(billdate) ORDER BY DATE(billdate);"

def ProductReport():
    #fetch product wise report 
    sql = "SELECT p.id, p.name, SUM(bi.quantity) AS sold_quantity FROM product p, bill_items bi, bill b WHERE p.id = bi.productid AND bi.billid = b.id AND b.billdate BETWEEN '2026-06-01' AND '2026-06-30' GROUP BY p.id, p.name ORDER BY sold_quantity DESC;"

def MonthlyReport():
     #fetch last 30 days
    sql = "SELECT COUNT(DISTINCT b.id) AS total_bills, COUNT(*) AS total_items, (SELECT SUM(amount) FROM bill WHERE billdate >= CURDATE() - INTERVAL 29 DAY AND billdate < CURDATE() + INTERVAL 1 DAY) AS total_bill_amount FROM bill b, bill_items bi WHERE b.id = bi.billid AND b.billdate >= CURDATE() - INTERVAL 29 DAY AND b.billdate < CURDATE() + INTERVAL 1 DAY;"

    displayReport(sql)

def WeeklyReport():
     #fetch last 7 days 
    sql = "SELECT COUNT(DISTINCT b.id) AS total_bills, COUNT(*) AS total_items, (SELECT SUM(amount) FROM bill WHERE billdate >= CURDATE() - INTERVAL 6 DAY AND billdate < CURDATE() + INTERVAL 1 DAY) AS total_bill_amount FROM bill b, bill_items bi WHERE b.id = bi.billid AND b.billdate >= CURDATE() - INTERVAL 6 DAY AND b.billdate < CURDATE() + INTERVAL 1 DAY;"

    displayReport(sql)

def DailyReport():
    # fetch today data
    sql = "SELECT COUNT(DISTINCT b.id) AS total_bills, COUNT(*) AS total_items, ( SELECT (amount) FROM bill WHERE DATE(billdate) = CURDATE()) AS total_bill_amount FROM bill b,bill_items bi where b.id = bi.billid and DATE(b.billdate) = CURDATE();"
    displayReport(sql)

def displayReport(sql):
    #create cursor 
    cursor = database.connect.cursor(dictionary=True)

    #run sql statement
    cursor.execute(sql)

    #fetch all row 
    table = cursor.fetchall()
    
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
                        b.AddBillItem()
                    elif bill_choice == 2:
                        b.DeleteItemFromBill()
                    elif bill_choice == 3:
                        b.SearchItemInBill()
                    elif bill_choice == 4:
                        b.GenerateBill()
                    elif bill_choice == 5:
                        b.DisplayBillItem()
                    else:
                        print("exit to main menu")
                        break  # break inner loop

        elif choice == 3:
            while True:
                # Daily, Weekly, Monthly, Product, Sales Reports
                print("\nPress 1 to generate daily report")
                print("Press 2 to generate last 7 days report")
                print("Press 3 to generate last 30 days report")
                print("Press 4 to generate product report")
                print("Press 5 to generate sales report")
                print("Press 0 to exit to main menu")
                
                report_choice = int(input("enter your choice: "))
                
                if report_choice < 0 or report_choice > 5:
                    print("invalid choice")
                else:
                    if report_choice == 1:
                        DailyReport()
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