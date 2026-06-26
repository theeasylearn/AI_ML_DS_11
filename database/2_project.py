import products as p
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
                print("Press 5 to view all bills")
                print("Press 0 to exit to main menu")
                
                bill_choice = int(input("enter your choice: "))
                
                if bill_choice < 0 or bill_choice > 5:
                    print("invalid choice")
                else:
                    if bill_choice == 1:
                        print("let us add item to bill")
                    elif bill_choice == 2:
                        print("let us delete item from bill")
                    elif bill_choice == 3:
                        print("let us search item in bill")
                    elif bill_choice == 4:
                        print("let us generate bill")
                    elif bill_choice == 5:
                        print("let us view all bills")
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