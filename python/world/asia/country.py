asia_countries = [
    "Afghanistan", "Armenia", "Azerbaijan",
    "Bahrain", "Bangladesh", "Bhutan", "Brunei",
    "Cambodia", "China", "Cyprus",
    "Georgia",
    "India", "Indonesia", "Iran", "Iraq", "Israel",
    "Japan", "Jordan",
    "Kazakhstan", "Kuwait", "Kyrgyzstan",
    "Laos", "Lebanon",
    "Malaysia", "Maldives", "Mongolia", "Myanmar",
    "Nepal", "North Korea",
    "Oman",
    "Pakistan", "Palestine", "Philippines",
    "Qatar",
    "Russia",
    "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", "Syria",
    "Taiwan", "Tajikistan", "Thailand", "Timor-Leste", "Turkey", "Turkmenistan",
    "United Arab Emirates", "Uzbekistan",
    "Vietnam",
    "Yemen"
]

def getCountry():
    global asia_countries
    return asia_countries

def hasCountry(countryName):
    global asia_countries
    result = countryName in asia_countries
    return result
