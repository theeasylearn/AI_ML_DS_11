#create chart that display movement of nifty50 in last 7 days
import matplotlib.pyplot as plt 

#create data 
#days 
x = [1,2,3,4,5,6,7] #7
y = [1000,1020,1050,1070,1040,1060,1080] #7

#create chart
plt.plot(x,y)

#customize chart
plt.title("Nifty 50 last 7 days movement",fontsize='large',fontweight='bold',pad=10)
plt.xlabel("days",fontsize='11',fontweight='bold',labelpad=10)
plt.ylabel('Points',fontsize='11',fontweight='bold',labelpad=10)
# line style can be '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
plt.grid(which='both',linestyle='dotted',linewidth=0.7)
plt.legend(loc='upper left',title=['nifty 50 (india)'])
#display chart

plt.xlim(left=1,right=8) #start and stop value for x 
plt.ylim(bottom=900,top=1200) #bottom and top value for y 
plt.show()