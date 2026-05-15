name = "The Easylearn Academy"
print(name)
print(name.upper())
print(name.lower())

print(f"has {name} contain only alphabets and numbers",name.isalnum())
print(f"has {name} contain only alphabets",name.isalpha())
print(f"has {name} contain only lowercase alphabets",name.islower())
print(f"has {name} contain only uppercase alphabets",name.isupper())
print(f"has {name} contain only titlecase alphabets",name.istitle())
print(f"has {name} contain only digits ",name.isdigit())
print(f"has {name} contain only space ",name.isspace())

print(f"{name} has ",len(name), " characters")

gujarat_cities = [
    "Ahmedabad", "Surat", "Vadodara", "Rajkot", "Gandhinagar",
    "Bhavnagar", "Jamnagar", "Junagadh", "Anand", "Mehsana",
    "Bhuj", "Porbandar", "Navsari", "Vapi", "Bharuch",
    "Nadiad", "Surendranagar", "Morbi", "Palanpur", "Godhra",
    "Veraval", "Amreli", "Dahod", "Himmatnagar", "Patan",
    "Ankleshwar", "Valsad", "Gondal", "Jetpur", "Dwarka"
]
print(gujarat_cities)
line = ' ' #store separator character into line variable 
cities = line.join(gujarat_cities)
print(cities)

dishes = "Pithla, Bhakri, Bharli Vangi, Sabudana Khichdi, Batata Bhaji, Masale Bhaat, Varan Bhaat, Kanda Poha, Upma, Thalipeeth"

#convert it into list 
list = dishes.split()
print(list)

line = "India is a country where India’s diversity, India’s culture, India’s history, and India's unity are celebrated."
print(line)
print(line.replace("India","Bharat"))
print(line.replace("India","Bharat",1))