# Using break to exit a loop


while True:
    city = input("Your favorite city: ")

    if city.lower() == 'quit':
        break
    else: print("I'd love to go to " + city.title() + "!")



        