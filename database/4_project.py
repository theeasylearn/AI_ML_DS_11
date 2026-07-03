import products as p
import bills as b 
import connection as database
import reports
import traceback
import datetime

def log_error(err):
    try:
        with open("error.log", "a") as f:
            f.write(f"[{datetime.datetime.now()}] Error: {str(err)}\n")
            f.write(traceback.format_exc())
            f.write("="*50 + "\n")
    except Exception as log_err:
        print("Failed to write to error.log:", log_err)

while True:
    try:
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
                            reports.DailyReport()
                        elif report_choice == 2:
                            reports.WeeklyReport()
                        elif report_choice == 3:
                            reports.MonthlyReport()
                        elif report_choice == 4:
                            reports.ProductReport()
                        elif report_choice == 5:
                            reports.SalesReport()
                        else:
                            print("exit to main menu")
                            break  # break inner loop

            else:
                print("exit from program")
                break
    except Exception as e:
        print("An error occurred:", e)
        log_error(e)