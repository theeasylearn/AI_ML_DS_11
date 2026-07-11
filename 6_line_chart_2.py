import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
import mysql.connector as connector

#create connection 
try:
    connect = connector.connect(host='localhost',user='root',passwd='',database='ai_ml_ds_11',port='3306')
    print('connection created.')
    score = pd.read_sql('select * from score order by overs',con=connect)

    # print(score)
    sns.lineplot(x='overs',y='india',data=score,hue='')
    plt.xticks(ticks=range(1,21))
    plt.xlabel('overs')
    plt.ylabel('runs')
    plt.show()
except connector.Error as error:
    print("connection could not be created due to error,")
    print(error.errno)
    print(error.msg)