# Store information about a pizza being ordered.
pizza = {
    'crust':'thick',
    'toppings': ['mushirooms', 'extra cheese']
}

#Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages_list in favorite_languages.items():
    if len(languages_list) == 1:
        print("\n" + name.title() + "'s favorite language is:")
     
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        
    for language in languages_list:
        print("\t" + language.title())

