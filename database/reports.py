import connection as database

def displayReport(sql, params=None):
    # create cursor
    cursor = database.connect.cursor(dictionary=True)

    # run sql statement
    if params:
        cursor.execute(sql, params)
    else:
        cursor.execute(sql)

    # fetch all rows
    table = cursor.fetchall()
    cursor.close()

    if not table or len(table) == 0:
        print("\nNo records found.")
    else:
        columns = list(table[0].keys())
        col_widths = {}
        for col in columns:
            # Find max string representation length of values in this column
            max_val_len = max(len(str(row[col])) for row in table)
            col_widths[col] = max(max_val_len, len(col))
        
        print()
        # Print header
        header_str = " | ".join(f"{col:<{col_widths[col]}}" for col in columns)
        print(header_str)
        print("-" * len(header_str))
        
        # Print rows
        for row in table:
            row_str = " | ".join(f"{str(row[col] if row[col] is not None else ''):<{col_widths[col]}}" for col in columns)
            print(row_str)
        print()

def DailyReport():
    # fetch today data
    sql = "SELECT COUNT(DISTINCT b.id) AS total_bills, COUNT(*) AS total_items, (SELECT SUM(amount) FROM bill WHERE DATE(billdate) = CURDATE()) AS total_bill_amount FROM bill b, bill_items bi WHERE b.id = bi.billid AND DATE(b.billdate) = CURDATE();"
    displayReport(sql)

def WeeklyReport():
    # fetch last 7 days 
    sql = "SELECT COUNT(DISTINCT b.id) AS total_bills, COUNT(*) AS total_items, (SELECT SUM(amount) FROM bill WHERE billdate >= CURDATE() - INTERVAL 6 DAY AND billdate < CURDATE() + INTERVAL 1 DAY) AS total_bill_amount FROM bill b, bill_items bi WHERE b.id = bi.billid AND b.billdate >= CURDATE() - INTERVAL 6 DAY AND b.billdate < CURDATE() + INTERVAL 1 DAY;"
    displayReport(sql)

def MonthlyReport():
    # fetch last 30 days
    sql = "SELECT COUNT(DISTINCT b.id) AS total_bills, COUNT(*) AS total_items, (SELECT SUM(amount) FROM bill WHERE billdate >= CURDATE() - INTERVAL 29 DAY AND billdate < CURDATE() + INTERVAL 1 DAY) AS total_bill_amount FROM bill b, bill_items bi WHERE b.id = bi.billid AND b.billdate >= CURDATE() - INTERVAL 29 DAY AND b.billdate < CURDATE() + INTERVAL 1 DAY;"
    displayReport(sql)

def ProductReport():
    # fetch product wise report 
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    sql = "SELECT p.id, p.name, SUM(bi.quantity) AS sold_quantity FROM product p, bill_items bi, bill b WHERE p.id = bi.productid AND bi.billid = b.id AND DATE(b.billdate) BETWEEN %s AND %s GROUP BY p.id, p.name ORDER BY sold_quantity DESC;"
    displayReport(sql, (start_date, end_date))

def SalesReport():
    # generate day wise sales report 
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    sql = "SELECT DATE_FORMAT(billdate,'%d-%m-%Y') AS bill_date, DAYNAME(billdate) AS day_name, COUNT(id) AS total_bills, SUM(amount) AS total_sales FROM bill WHERE DATE(billdate) BETWEEN %s AND %s GROUP BY DATE(billdate), DAYNAME(billdate) ORDER BY DATE(billdate);"
    displayReport(sql, (start_date, end_date))
