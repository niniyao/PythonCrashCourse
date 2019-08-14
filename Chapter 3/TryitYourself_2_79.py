invited_people = ['Spongebob', 'Doraemon',
                  'D. W.', 'Auther', 'Lily', 'Mintgreen', 'Yuzu']
                  
message = 'Dear ' + invited_people[0] + ', ' + \
    '\nYou are invited to dinner at my house tonight. See you at 7pm!' + '\nBest,' + '\nNini'
print(message)

message = 'Dear ' + invited_people[1] + ', ' + \
    '\nYou are invited to dinner at my house tonight. See you at 7pm!' + '\nBest,' + '\nNini'
print(message)

message = 'Dear ' + invited_people[-2] + ', ' + \
    '\nYou are invited to dinner at my house tonight. See you at 7pm!' + '\nBest,' + '\nNini'
print(message)
print('\n')

message = 'Dear ' + invited_people[1] + ', ' + \
    '\nI am sorry to hear you cannot join us for dinner tonight. Hope to see you next time!' + \
    '\nBest,' + '\nNini'
print(message)
print('\n')

invited_people[1] = 'Pikachu'
print(invited_people)
print('\n')
message = 'Dear ' + invited_people[0] + ',\n' + \
    '\nYou are invited to dinner at my house tonight. See you at 7pm!\n' + '\nBest,' + '\nNini'
print(message)
print('\n')
message = 'Dear ' + invited_people[1] + ',\n ' + \
    '\nYou are invited to dinner at my house tonight. See you at 7pm!\n' + '\nBest,' + '\nNini'
print(message)
print('\n')
message = 'Dear ' + invited_people[-2] + ',\n ' + \
    '\nYou are invited to dinner at my house tonight. See you at 7pm!\n' + '\nBest,' + '\nNini'
print(message)
