import mysql.connector as connector
#create connection 
try:
    connect = connector.connect(host='localhost',user='root',passwd='',
                                database='ai_ml_ds_11',port='3306')
    print('connection created.')
except connector.Error as error:
    print("connection could not be created due to error,")
    print(error.errno)
    print(error.msg)
