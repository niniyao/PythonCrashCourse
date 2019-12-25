#Flag
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "



flag = True

while flag == True:
    message = input(prompt)

    if message == 'quit':
        flag = False
    else:
        print(message)


        