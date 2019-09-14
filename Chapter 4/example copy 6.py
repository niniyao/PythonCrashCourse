#Working with part of a list
#Slicing a list
players = ['charlies', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

#Looping through a slice
players = ['charlies', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team.")
for player in players[:3]:
    print(player.title())

