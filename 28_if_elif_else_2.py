# write a program to calculate & display gross annual income, tax and net income from monthly given income as per below income tax rule 
# annual gross income                        Tax Rate
# Above Rs. 24,00,000                        30%
# From Rs. 20,00,001 to Rs. 24,00,000	     25%
# From Rs. 16,00,001 to Rs. 20,00,000	     20%
# From Rs. 12,00,000 to Rs. 16,00,000	     15%
# below 12,00,000                             5%
'''
    accept monthly income 
    calculate gross income (monthly income x 12)
    calculate tax as per rule 
    calculate net income (grossIncome - tax)
'''
monthlyIncome = int(input("Enter monthly income"))
grossIncome = monthlyIncome * 12
tax = None 
if grossIncome<1200000:
    tax = (grossIncome * 5) / 100
elif grossIncome<1600000:
    tax = (grossIncome * 15) / 100
elif grossIncome<2000000:
    tax = (grossIncome * 20) / 100
elif grossIncome<2400000:   
    tax = (grossIncome * 25) / 100
else: 
    tax = (grossIncome * 30) / 100

netIncome = grossIncome - tax 

print(f"gross income {grossIncome} tax = {tax} net income = {netIncome}")