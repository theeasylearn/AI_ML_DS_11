import world.europe.country as eu 
import world.afferica.country as af 
import world.asia.country as ai 

#function calling of package 
print(eu.getCountry())
print(af.getCountry())
print(ai.getCountry())

result = eu.hasCountry("France")
print(f"is France existing in europe ",result)

result = af.hasCountry("Kenya")
print(f"is Kenya existing in africa ",result)

result = af.hasCountry("India")
print(f"is India existing in africa ",result)

result = ai.hasCountry("China")
print(f"is China existing in asia ",result)
