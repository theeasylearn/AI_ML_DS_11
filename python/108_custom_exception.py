from datetime import datetime as dt 
'''
write a program to accept male & female person birthdate to apply for marriage certificate. make sure male is 21 old and female is 18 years old. if criteria do not satisfy raise exception TypeError and display message not eligible to apply for marriage certificate. otherwise display message eligible to apply for marriage certificate
'''
#create Custom Exception
class MarriageCertificateException(Exception):
    pass 
while True:
    try:
        male_birthdate = input("Enter Male person birthdate DD-MM-YYYY")
        female_birthdate = input("Enter Female person birthdate DD-MM-YYYY")

        #convert date into actual date
        male_birthdate = dt.strptime(male_birthdate,'%d-%m-%Y')
        female_birthdate = dt.strptime(female_birthdate,'%d-%m-%Y')

    except ValueError as error:
        print("Invalid date")
    else:
        print(male_birthdate,female_birthdate)
        #current date 
        today = dt.now()

        #calculate gap between male person birthdate & currentdate
        male_gap = abs(today - male_birthdate)
        male_age = male_gap.days // 365

        #calculate gap between female person birthdate & currentdate
        female_gap = abs(today - female_birthdate)
        female_age = female_gap.days // 365
        print(f"Male age = {male_age} Female age = {female_age}")
        try:
            if male_age<21 or female_age<18:
                raise MarriageCertificateException
        except MarriageCertificateException:
            print("male person be 21 year and female must 18 year old for apply marriage certificate")
        else:
            print("you are eligible to get marriage certificate")
        finally:
            break
    finally:
        print("Good bye")
