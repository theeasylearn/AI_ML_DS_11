import matplotlib.pyplot as plt 
# Passenger vehicle wholesale figures for the Top 10 carmakers in India (Full Year 2025)
car_sales = [1786226, 592771, 567607, 559558, 320703, 259043, 108277, 65614, 62576, 36420]
# Manufacturer names corresponding to the 2025 sales values
companies = [
    "Maruti Suzuki",
    "Mahindra & Mahindra",
    "Tata Motors",
    "Hyundai Motor India",
    "Toyota Kirloskar",
    "Kia India",
    "Skoda Volkswagen Group",
    "JSW MG Motor India",
    "Honda Cars India",
    "Renault India"
]
# Hexadecimal color codes for each car manufacturer (Top 10)
hex_colors = [
    "#A1C4FD",  # Maruti Suzuki (Light Ice Blue)
    "#E2E8F0",  # Mahindra & Mahindra (Soft Silver/Platinum)
    "#96E6A1",  # Tata Motors (Light Mint/EV Teal)
    "#B0C4DE",  # Hyundai Motor India (Light Powder Blue)
    "#FF9999",  # Toyota Kirloskar (Soft Pastel Red)
    "#CBD5E1",  # Kia India (Light Slate Grey)
    "#A7F3D0",  # Skoda Volkswagen Group (Pale Emerald Green)
    "#CCFBF1",  # JSW MG Motor India (Soft Pale Teal)
    "#FCA5A5",  # Honda Cars India (Light Coral Red)
    "#FEF08A"   # Renault India (Soft Pastel Yellow)
]
plt.pie(car_sales,labels=companies,colors=hex_colors,autopct='%1f%%')
plt.title('Card company market share')
plt.show()

