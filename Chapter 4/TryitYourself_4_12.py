my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("my favoriate foods are:")
for my_food in my_foods:
    print(my_food)

print("\nmy friend's favoriate foods are:")
for friend_food in friend_foods:
    print(friend_food)

