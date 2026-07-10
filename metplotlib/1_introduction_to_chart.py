#create chart that display movement of nifty50 in last 7 days
import matplotlib.pyplot as plt 

#create data 
#days 
x = [1,2,3,4,5,6,7] #7
y = [1000,1020,1050,1070,1040,1060,1080] #7

#create chart
plt.plot(x,y)

#customize chart
plt.title("Nifty 50 last 7 days movement")
plt.xlabel("days")
plt.ylabel('Points')

#display chart
plt.show()