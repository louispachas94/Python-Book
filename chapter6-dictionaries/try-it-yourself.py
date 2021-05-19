# 6.1
me = {'first_name': 'Louis',
      "last_name": 'Pachas',
      'age': 26,
      'city_born': 'SF',
      'city_now_live': 'SJ'
      }
print(me['first_name'])
print(me['last_name'])
print(me['age'])
print(me['city_born'])
print(me['city_now_live'])

# 6.2
friends_fav_num = {
    'louis': 11,
    'jenny': 3,
    'rocky': 10,
    'dad': 7,
    'brother': 9
}
print(f"\nLouis's favorite number is: {friends_fav_num['louis']}")
print(f"Jenny's favorite number is: {friends_fav_num['jenny']}")
print(f"Rocky's favorite number is: {friends_fav_num['rocky']}")
print(f"Dad's favorite number is: {friends_fav_num['dad']}")
print(f"Brother's favorite number is: {friends_fav_num['brother']}")

# ALT way
num = friends_fav_num['louis']
print(f"(Alt way too; from book)\tLouis' fav number is :{num}")

# 6.3
glossary = {
    'list': 'list of values; changeable',
    'print': 'output of program',
    'IDE': 'where you can write python programs',
    'for loop': 'loop thru each element/value; go thru one by one',
    'dictonary(python)': 'a collection of elements that have a key & value',
    # adding 5+ (6.4)
    'if statment': 'conditional test',
    'string': 'data type that is mostly words but can be used with numbers or other data types',
    'integer': 'whole numbers',
    'float': 'decimal numbers',
    'Python': 'a high level muliple use programmuing language'
}
meaning = glossary['list']
print(f'\nList means: {meaning}')
meaning = glossary['print']
print(f'\nPrint means: {meaning}')
meaning = glossary['IDE']
print(f'\nIDE means: {meaning}')
meaning = glossary['for loop']
print(f'\nfor loop means: {meaning}')
meaning = glossary['dictonary(python)']
print(f'\ndictonary(python) means: {meaning}')

# 6.4
print('\n')
for keys, values in glossary.items():
    print(f'Term - {keys.title()}: {values}')

# 6.5
print('\n')
rivers = {
    'amazon': 'peru',
    'mediterainian': 'italy',
    'missasippi': 'usa'
}
# sentence using key and values
for river_name, river_location in rivers.items():
    print(f'The {river_name.title()} is located in {river_location.title()}')

# using keys only
print('\n')
for river_names in rivers:
    print(river_names.title())

# using values only
print('\n')
for river_locations in rivers.values():
    print(river_locations.title())

# 6.6
print('\n')
favorite_languages ={
    'louis':'python',
    'jenny':'none',
    'rocky':'dart',
    'lobo':'kotlin',
    'lizardo':'swift'
}
need_to_take = ['jairo','louis','mom','lobo','dad']
for user in need_to_take:
    if user in favorite_languages.keys():
        print(f'{user.title()} thanks for taking the poll!')
    else:
        print(f'{user.title()} please take out poll!')

# 6.7
print('\n')
lou = {
        'first_name': 'louis',
        'last_name': 'pachas',
        'age': 26,
        'location': 'san jose',
        'job': 'IT'
    }
jeni= {
        'first_name': 'jenifer',
        'last_name': 'corona',
        'age': 24,
        'location': 'mv',
        'job': 'teacher'
    }
people = [lou,jeni]
for person in people:
    name = f"{person['first_name'].title()} {person ['last_name'].title()}"
    age = f"{person ['age']}"
    work = f"{person ['job']}"
    live_in = f"{person ['location'].title()}"
    print(f'This person name is {name} they are {age}, and work as {work} in the city of {live_in}')

# 6.8
print('\n')
fish = {
    'name': 'fishy',
    'owner': 'mark',
    'type': 'fish'
}
dog = {
    'name': 'rocky',
    'owner': 'louis',
    'type': 'dog'
}
cat = {
    'name': 'kitty',
    'owner': 'jencarlos',
    'type': 'cat'
}
koala = {
    'name': 'kathy',
    'owner': 'jeni',
    'type': 'koala'
}
pets = [fish, dog, cat, koala]
for pet in pets:
    print(f"Info on the pet {pet['name'].title()}")
    for keyw, value in pet.items():
        print(f"\t{keyw}: {value}")
# original works too; ^^ book solution
"""for petz in pets:
    pet_name = f"{petz['name'].title()}"
    pet_owner_name = f"{petz['owner'].title()}"
    pet_type = f"{petz['type']}"
    print(f'This pet is a {pet_type} named {pet_name}, and its owner is {pet_owner_name}.')"""

# 6.9 no mentioned of list; but examples shows list as value
print('\n')
favorite_places = {
    'jenny':['mod','wingstop'],
    'kathy':['wing stop','tacos'],
    'george':['fukee','mod','poki']
}
for keys,values in favorite_places.items():
    print(f'{keys} favorite places to eat are:')
    # since we need all values (list) we need another for loop
    for places in values:
        print(f'\n\t{places}')

# 6.10
print('\n')
friends_fav_num_pt2 = {
    'louis': [11,10],
    'jenny': [3,0],
    'rocky': [5,10,2],
    'dad': [7,0,858],
    'brother': [5,333,9]
}

for friends,fav_number in friends_fav_num_pt2.items():
    print(f'{friends} favorite numbers are:')
    for friends_number in fav_number:
        print(f' {friends_number}')

# 6.11
print('\n')
cities = {
    'lima': {
        'country': 'Peru',
        'population': 300000,
        'fact': 'best food'
    },
    'san jose': {
        'country': 'USA',
        'population': 1000000,
        'fact': 'Silicon Valley'
    },
    'san francisco': {
        'country': 'USA',
        'population': 1000000,
        'fact': '1906 earthquake'
    },
    'las vegas':{
        'country': 'USA',
        'population': 50000,
        'fact': 'many casinos'
    }
}
# one liners; could have created variables for each of the values in the dictionary
for city, info in cities.items():
    print(f"The city of {city.title()} is located in {info['country']}, and has a population of {info['population']}.\nHere's a quick fact: {info['fact'].title()}")

# 6.12
# using cities dictionary for this problem ^^^ added las vegas dictionary