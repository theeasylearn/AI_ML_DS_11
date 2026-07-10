#create chart that display movement of nifty50 in last 7 days
import matplotlib.pyplot as plt 
import numpy as np 
#create data 
#days 
x = np.arange(1,22)
y = [23995.70, 24177.65, 23997.55, 24119.30, 24032.80, 24330.95, 24326.65, 24176.15, 23815.85, 23379.55, 23412.60, 23689.60, 23643.50, 23649.95, 23618.00, 23659.00, 23654.70, 23719.30, 24031.70, 23913.70, 23907.15]

#increase canvas (screen size of chart)
plt.figure(figsize=(12,8))
#create chart
plt.plot(x,y)

#customize chart
plt.title("Nifty 50 last 30 days movement",fontsize='large',fontweight='bold',pad=10)
plt.xlabel("days",fontsize='11',fontweight='bold',labelpad=10)
plt.ylabel('Points',fontsize='11',fontweight='bold',labelpad=10)
# line style can be '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
plt.grid(which='both',linestyle='dotted',linewidth=0.7)
plt.legend(loc='upper left',title=['nifty 50 (india)'])
#display chart

plt.xlim(left=1,right=22) #start and stop value for x 
plt.xticks(ticks=x,labels=x)
plt.yticks(ticks=range(23000,24400,100),labels=range(23000,24400,100))
plt.tight_layout()
plt.show()