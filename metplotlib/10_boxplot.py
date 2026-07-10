import matplotlib.pyplot as plt 


# Employee Monthly Salaries (in thousands) by Department
# Note: 120 (manager), 35 (intern) are outliers
sales = [45, 48, 50, 52, 47, 49, 51, 46, 53, 48, 120, 35] 

# Note: 150 (senior architect), 40 (junior) are outliers
engineering = [65, 70, 68, 72, 67, 71, 69, 73, 66, 70, 150, 40] 

# Note: 28 (part-time), 55 (director) are outliers
hr = [38, 42, 40, 44, 39, 43, 41, 45, 38, 42, 28, 55] 

# Note: 95 (CMO), 32 (intern) 
marketing = [50, 55, 52, 58, 53, 56, 54, 57, 51, 55, 95, 32] 

list = [sales,engineering,hr,marketing]

plt.boxplot(list,labels=['sales','engineering','hr','marketing'])

plt.xlabel('Departments')
plt.ylabel('Salary')
plt.title('Department wise salary using boxplot chart')
plt.show()

