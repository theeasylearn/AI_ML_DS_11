from datetime import datetime as dt 

current_date_time = dt.now()

print(current_date_time)

names = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

#indian format 
indian_format_date = names[current_date_time.weekday()] + " " + str(current_date_time.day) + "/" + str(current_date_time.month) + "/" + str(current_date_time.year)

print(indian_format_date)

#write a code to display hours minutes seconds  
# hh:mm:ss

