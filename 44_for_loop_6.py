team = {
    "Rohit Sharma": 78,
    "Shubman Gill": 45,
    "Virat Kohli": 92,
    "Shreyas Iyer": 34,
    "KL Rahul": 66,
    "Hardik Pandya": 28,
    "Ravindra Jadeja": 41,
    "Ravichandran Ashwin": 15,
    "Jasprit Bumrah": 7,
    "Mohammed Shami": 12,
    "Mohammed Siraj": 9
}
#generate total team score 
score = 0
#calculate average
for player in team:
    print(player, team[player])
    score = score + team[player]
size = len(team)
average = score / size 
print(score)
print(f"average {average:.2f}")