invited_people = ['Spongebob', 'Doraemon',
                  'D. W.', 'Auther', 'Lily', 'Mintgreen', 'Yuzu']

invited_people[1] = 'Pikachu'
print(invited_people)

invited_people.insert(0, 'Jun')
invited_people.insert(3, 'Ani')
invited_people.insert(-1, 'Gong')
print(invited_people)
print('\n')

print(invited_people)
not_guest_1 = invited_people.pop()
print(invited_people)
print(not_guest_1)
message = 'Dear ' + not_guest_1 + ',\n' + '\nI am so sorry that I cannot invite you to dinner tonight because the new dinner table will not arrive today. My old table cannot provide enough seats for our guests. I will definitely invite you again when I got the bigger dinner table!\n' + '\nBest,' + '\nNini'
print(message)
print('\n')

print(invited_people)
not_guest_2 = invited_people.pop()
print(invited_people)
print(not_guest_2)
message = 'Dear ' + not_guest_2 + ',\n' + '\nI am so sorry that I cannot invite you to dinner tonight because the new dinner table will not arrive today. My old table cannot provide enough seats for our guests. I will definitely invite you again when I got the bigger dinner table!\n' + '\nBest,' + '\nNini'
print(message)
print('\n')

print(invited_people)
not_guest_3 = invited_people.pop()
print(invited_people)
print(not_guest_3)
message = 'Dear ' + not_guest_3 + ',\n' + '\nI am so sorry that I cannot invite you to dinner tonight because the new dinner table will not arrive today. My old table cannot provide enough seats for our guests. I will definitely invite you again when I got the bigger dinner table!\n' + '\nBest,' + '\nNini'
print(message)
print('\n')

print(invited_people)
not_guest_4 = invited_people.pop()
print(invited_people)
print(not_guest_4)
message = 'Dear ' + not_guest_4 + ',\n' + '\nI am so sorry that I cannot invite you to dinner tonight because the new dinner table will not arrive today. My old table cannot provide enough seats for our guests. I will definitely invite you again when I got the bigger dinner table!\n' + '\nBest,' + '\nNini'
print(message)
print('\n')

print(invited_people)
not_guest_5 = invited_people.pop()
print(invited_people)
print(not_guest_5)
message = 'Dear ' + not_guest_5 + ',\n' + '\nI am so sorry that I cannot invite you to dinner tonight because the new dinner table will not arrive today. My old table cannot provide enough seats for our guests. I will definitely invite you again when I got the bigger dinner table!\n' + '\nBest,' + '\nNini'
print(message)
print('\n')

print(invited_people)
not_guest_6 = invited_people.pop()
print(invited_people)
print(not_guest_6)
message = 'Dear ' + not_guest_6 + ',\n' + '\nI am so sorry that I cannot invite you to dinner tonight because the new dinner table will not arrive today. My old table cannot provide enough seats for our guests. I will definitely invite you again when I got the bigger dinner table!\n' + '\nBest,' + '\nNini'
print(message)
print('\n')

print(invited_people)
not_guest_7 = invited_people.pop()
print(invited_people)
print(not_guest_7)
message = 'Dear ' + not_guest_7 + ',\n' + '\nI am so sorry that I cannot invite you to dinner tonight because the new dinner table will not arrive today. My old table cannot provide enough seats for our guests. I will definitely invite you again when I got the bigger dinner table!\n' + '\nBest,' + '\nNini'
print(message)
print('\n')

print(invited_people)
not_guest_8 = invited_people.pop()
print(invited_people)
print(not_guest_8)
message = 'Dear ' + not_guest_8 + ',\n' + '\nI am so sorry that I cannot invite you to dinner tonight because the new dinner table will not arrive today. My old table cannot provide enough seats for our guests. I will definitely invite you again when I got the bigger dinner table!\n' + '\nBest,' + '\nNini'
print(message)
print('\n')

print(invited_people)
message = 'Dear ' + invited_people[0] + ',\n' + \
    '\nYou and Spongebob are still invited to my house for dinner tonight. I am sorry that I could not invite more people to the dinner because the big dinner table has not arrived. I will see you at 7pm!\n' + '\nBest,' + '\nNini'
print(message)
print('\n')

message = 'Dear ' + invited_people[1] + ',\n' + \
    '\nYou and Jun are still invited to my house for dinner tonight. I am sorry that I could not invite more people to the dinner because the big dinner table has not arrived. I will see you at 7pm!\n' + '\nBest,' + '\nNini'
print(message)
print('\n')

del invited_people[1]
print(invited_people)
del invited_people[0]
print(invited_people)
# 要从后往前删，如果先删了0，1就不是1了。
