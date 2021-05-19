# Dictionaries in Python are a collection of key & value pairs
# example
programming = {'languages': 'python', 'ide': 'vs code'}

print(programming['languages'])

# adding a new key & value to a dictionary
print('\n')

programming['keyboard'] = 'mechanical'
programming['mouse'] = 'all in one'

print(programming)

# creating a new dictionary from 0
print('\n')

laptop_brands = {}
laptop_brands['Lenovo'] = 'Thinkbook'
laptop_brands['HP'] = 'X360 spectre'
laptop_brands['Dell'] = 'XPS'
laptop_brands['Apple'] = 'Macbook'

print(laptop_brands)

# modifying a value
print('\n')
# using above dictionary as example
laptop_brands['Dell'] = 'Latitude'

print(laptop_brands)

# removing key (includes value)
print('\n')
del laptop_brands['HP']
print(laptop_brands)

# styling; with example
print('\n')
liga_1 = {
    'lima': 'alianza lima',
    'cuzco': 'cuzco fc'
}
lima_team = liga_1['lima']
print(f'These teams play in Peru: {lima_team.title()}')

# using get() to access VALUES; or if they do not exist
print('\n')

injures = {'back': 'last week', 'ankle': '1 year', 'arm': '2 years', 'knee': '2 weeks'}
toe = injures.get('toes')
foot = injures.get('5 years', 'its been a while')
back = injures.get('back')
print(injures)
# since no key named toe; it prints none/no value exist
print(toe)
# since no key named foot & we added another argument to get() it will print what we put as the value
print(foot)
# key does exist in injures; will print the value of the key
print(back)

# Looping through a dictionary
# looping though all key-value pairs
username_1 = {
    'username': 'lpachas',
    'name': 'Louis',
    'age': 26
}
# needs the .items() method; returns a list of key-value pairs
# k and v could be anything just make sure you have the comma
for k, v in username_1.items():
    print(f'\nThe key titles are: {k}')
    print(f'The value titles are: {v}')

# loop through just the keys; no name for values or comma needed since we just wants keys
for keyz in username_1:
    print(f'\nThese are the keys: {keyz.upper()}')

# part2 of ^^^ but now using sorted method to get A-Z order
for keyh in sorted(laptop_brands):
    print(f'\nThese names of laptops should be in A-Z order: {keyh.upper()}')

# Looping through all VALUES
os_usage = {
    'System76': 'linux',
    'Dell': 'windows',
    'Macbook': 'macOS',
}
for opsys in os_usage.values():
    if opsys == 'linux':
        print('\nThats the best OS!')
    elif opsys == 'windows':
        print('Those are SLOW')
    else:
        print('Those are good OS for daily use.')
print(os_usage.values())

# Nesting
# List of dictionary
favorite_foods = {
    'louis': 'mod',
    'jenny': 'tacos'
}
favorite_places = {
    'retail': 'target',
    'malls': 'oakridge',
}
favorite_car = {
    'jenny': 'crv',
    'louis': 'camry'
}
# append can only add 1 at a time; fyi
date_night = [favorite_car, favorite_foods, favorite_places]
print(f'\n{date_night}')
for date in date_night:
    print(f'Dictionary: {date}')

# List in a dictionary
boot_line = {
    'nike': ['mercurial', 'tiempo', 'phantom vision'],
    'adidas': ['f50', 'adipure', 'X'],
    'puma': ['future', 'one', 'king'],
    'umbro': 'speciali'
}
print(f"\nMy favorite boots are {boot_line['umbro']} and {boot_line['nike'][0]}")

# Dictionary in a dictionary
users_dictionary = {
    'louis': {
        'first_name': 'louis',
        'last_name': 'pachas',
        'age': 26,
        'location': 'san jose',
        'job': 'IT'
    },
    'jenny': {
        'first_name': 'jenifer',
        'last_name': 'corona',
        'age': 24,
        'location': 'mv',
        'job': 'teacher'
    }
}
for user, info in users_dictionary.items():
    print(f"\nThe dctionary of the users: {user}")
    full_name = f"{info['first_name']} {info['last_name']}"
    ages = f"{info['age']}"
    locations = f"{info['location']}"
# new line starts and print below starts with first loop with louis, next loop jenifer goes with the 2nd line printed from above 
    print(f"\tThe users names: {full_name}, How old {ages}, and live in {locations}")

    