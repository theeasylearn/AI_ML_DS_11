#write a program to findout strike rate of batter using given ball and runs
try:
    runs = int(input("Enter runs"))
    balls = int(input("Enter balls"))
    strike_rate = (runs/balls) * 100
    print('all well')
except ValueError:
    print("invalid run/balls. must be numbers only")
except ZeroDivisionError:
    print("balls can not zero")
else:
    print(f"Strike rate = {strike_rate}")
finally:
    print("thank yor for using program")
