africa_countries = [
    "Algeria", "Angola",
    "Benin", "Botswana", "Burkina Faso", "Burundi",
    "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo (Republic)", "Congo (Democratic Republic)",
    "Djibouti",
    "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia",
    "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau",
    "Ivory Coast",
    "Kenya",
    "Lesotho", "Liberia", "Libya",
    "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique",
    "Namibia", "Niger", "Nigeria",
    "Rwanda",
    "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan",
    "Tanzania", "Togo", "Tunisia",
    "Uganda",
    "Zambia", "Zimbabwe"
]

def getCountry():
    global africa_countries
    return africa_countries

def hasCountry(countryName):
    global africa_countries
    result = countryName in africa_countries
    return result