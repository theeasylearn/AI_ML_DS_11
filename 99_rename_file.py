import os 
old_filename = input("enter old filename")
new_filename = input("enter new filename")

os.rename(old_filename,new_filename)
print('file renamed')
