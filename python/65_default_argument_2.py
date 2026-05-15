def getInches(km,meter=0,foot=0):
    totalInches = foot * 12 
    totalInches +=  (meter * 3.28 * 12)
    totalInches += (km * 1000 * 3.28 * 12)
    return totalInches

km = int(input("Enter KM"))
meter = int(input("Enter Meter"))
foot = int(input("Enter foot"))

result = getInches(km,meter,foot)
print("result into inches using 3 arguments",result)

result = getInches(km,meter)
print("result into inches using 2 arguments",result)

result = getInches(km)
print("result into inches using 1 arguments",result)


