#Make an empty list for storing aliens.
aliens_list = []

#Make 30 green aliens.
for alien_number in range(30,0, -1):
    alien_dict = {'color': 'green', 'points': 5, 'speed': 'slow'}
    alien_dict['number'] = alien_number
    aliens_list.append(alien_dict)

# #modify NO.11-NO.30 aliens:
for alien_dict in aliens_list:
    if int(alien_dict['number']) in range(11,21):
        alien_dict['color'] = 'yellow'
        alien_dict['points'] = 10
        alien_dict['speed'] = 'medium'
    elif int(alien_dict['number']) in range(21,31):
        alien_dict['color'] = 'red'
        alien_dict['points'] = 15
        alien_dict['speed'] = 'high'   

# for alien_dict in aliens_list[11:21]:
#         alien_dict['color'] = 'yellow'
#         alien_dict['points'] = 10
#         alien_dict['speed'] = 'medium'

# for alien_dict in aliens_list[21:31]:
#         alien_dict['color'] = 'red'
#         alien_dict['points'] = 15
#         alien_dict['speed'] = 'high'

for alien_dict in aliens_list:
    print(alien_dict)

# # #Show how many aliens have been created.
# print("Total number of aliens: " + str(len(aliens)))

