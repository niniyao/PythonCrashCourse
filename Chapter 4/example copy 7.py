#Coping a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("my favoriate foods are")
print(my_foods)

print("\nmy friend's favoriate foods are")
print(friend_foods)

#to prove we have two separate lists.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("my favoriate foods are")
print(my_foods)

print("\nmy friend's favoriate foods are")
print(friend_foods)

# If you see unexpected behavior when working with a copy of a list, make sure you are coping the list using a slice.