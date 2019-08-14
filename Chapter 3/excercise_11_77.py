motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motor_1 = 'ducati'
motorcycles.remove(motor_1)
print(motorcycles)
print("\nA " + motor_1.title() + " is too expensive for me.")

motor_2 = 'suzuki'
motorcycles.remove(motor_2)
print(motorcycles)
print("\nA " + motor_2.title() + " is too expensive for me.\n")

# print("\n")  单打一个空行，它会空两行。

too_expensive = []
too_expensive.append(motor_1)
print(too_expensive)

too_expensive.append(motor_2)
print(too_expensive)

print("\n" + too_expensive[0].title() + " and " + too_expensive[1].title() + " both are expensive to me!")
