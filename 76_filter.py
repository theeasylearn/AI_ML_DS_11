words = [
    "level", "river", "radar", "market", "madam",
    "garden", "racecar", "table", "civic", "school",
    "refer", "window", "noon", "office", "rotor",
    "flower", "kayak", "laptop", "deed", "mobile"
]
print(words)

#filter palindrome into new list 
palindrome = filter(lambda word: word if word == word[::-1] else None ,words)
print(list(palindrome))