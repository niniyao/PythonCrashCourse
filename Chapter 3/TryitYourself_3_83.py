loved_characters = ['Spongebob', 'Doraemon',
                  'D. W.', 'Auther', 'Lily', 'Mintgreen', 'Yuzu']
print(loved_characters)
print(loved_characters[0].title())

# changing elements in the list
loved_characters[0] = 'Nezha'
print(loved_characters)

#adding elements to the list
loved_characters.append('Shuke')
print(loved_characters)

#inserting elements into a list
loved_characters.insert(2, 'Beita')
print(loved_characters)

#remove elements using the del statement
del loved_characters[0]
print(loved_characters)

#remove elements using the pop() Method
print(loved_characters.pop())
print(loved_characters)

#pop() items from any positon
print(loved_characters.pop(1))
print(loved_characters)

#removing an item by value
loved_characters.remove('Auther')
print(loved_characters)

#sorting a list permanently with the sort() method
loved_characters.sort()
print(loved_characters)

#sorting a list temporarily with the sorted() function
loved_characters = ['Doraemon', 'D. W.', 'Lily', 'Mintgreen', 'Yuzu']
sorted(loved_characters)
print(loved_characters)
print(sorted(loved_characters))

#printing a list in reverse order
loved_characters.reverse()
print(loved_characters)

#finding the length of a list
print(len(loved_characters))
