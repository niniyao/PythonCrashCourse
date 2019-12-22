favorite_language = {
    'jen': {'python': 'easy', 'ruby': 'medium'},
    'sarah': {'C': 'hard'},
    'edward': {'ruby': 'medium', 'go': 'easy'},
    'phil': {'python': 'easy', 'haskell': 'hard'},
}

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },

}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
