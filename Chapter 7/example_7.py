# Using a while loop with lists and Dictionarie

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['allice', 'brain', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# The while loop runs as long as the list is not empty. 要等list里面没东西 才会跳出来。
# A for loop is effective for looping through a list, you shouldn't modify a list inside a for loop because Python will have trouble keeping track of the items in the list.
