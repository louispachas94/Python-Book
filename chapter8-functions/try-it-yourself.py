# 8.1
def display_message():
    print('I am learning about fucntions')

display_message()

# 8.2
def favorite_book(title):
    print(f'\nOne of my favorite books is {title}')

favorite_book('power')

# 8.3
print('\n')
def make_shirt(size, message):
    print(f'Shirt size will be {size.upper()} & message of {message}.')

make_shirt('m', 'hello world')
make_shirt(size='medium', message= 'Hello space')

# 8.4
print('\n')
def default_shirt(sizes = 'large', messages = 'I love python'):
    print(f'Shirt size will be {sizes.upper()} & message of {messages}.')

default_shirt()
default_shirt(sizes='medium')
default_shirt(sizes = 's', messages= 'i love scripting')

# 8.5
print('\n')
def describe_city(city, country = 'us'):
    print(f'{city.upper()} is in {country.upper()}.')

describe_city('La')
describe_city('sf')
describe_city('lima','peru')

# 8.6
print('\n')
def city_country(city, conutry):
    return f'{city.title()}, {conutry.title()}'

call_city_fucntion  = city_country('lima', 'peru')
print(call_city_fucntion)
call_city_fucntion = city_country('mexico city', 'mexico')
print(call_city_fucntion)
call_city_fucntion = city_country('panama city', 'panama')
print(call_city_fucntion)

# 8.7
print('\n')
    # since track_number=none; parameter not tied to any data type; 
    # so when paremter is called the arugment determines the data type
def make_album(artist, album, track_number = None):
    if track_number:
        dictionary_music = {'artist': artist.title(), 'album': album, 'track number': track_number}
    else:
        dictionary_music = {'artist': artist, 'album': album}
    return dictionary_music

print(make_album('50 cent', 'get rich or die tryin'))
print(make_album('50 cent', 'curtis'))
print(make_album('50 cent', 'animal ambition'))

# 8.8
print('\n')
# using 8.7 code
def make_albumv1(artist, album, track_number = None):
    # sets up the parameters to be in a dictionary format; needed before going onto while loop
    if track_number:
        dictionary_musicv1 = {'artist': artist.title(), 'album': album, 'track number': track_number}
    else:
        dictionary_musicv1 = {'artist': artist, 'album': album}
    return dictionary_musicv1

while True:
    users_input_artist = input("Enter an artist; type done when finish -  " )
    if users_input_artist == 'done':
        break
        
    users_input_album = input('Enter their album; type done when finish - ')
    if users_input_album == 'done':
        break
    print(make_albumv1(users_input_artist, users_input_album))
    
print(make_album('50 cent','the massacre', 20))

# 8.9
print('\n')

message_list = ['shakes for dinner', 'seafood for lunch', 'subway for breakfast']

# create function, parameter
def show_message(texts_list):
# for loop with functions parameter
    for text in texts_list:
# for loop will print 
        print(text)
# call function with created list as the parameter
show_message(message_list)

# 8.10, cont. from 8.9
print('\n')
new_message_list=[]
# create a function with 2 parameters - current list & new empty list
def send_messages(texts_list, sent_texts):
# while loop for current list
    while texts_list:
        print(texts_list)
# create a new variable define removing last item in the current list
        current_list = message_list.pop()
# with 2nd parameter append newly popped item from current list to new list
# using 2nd parameter since it is tied to the 2nd/new list. needs to be seprate and have own parameter
        sent_texts.append(current_list)
# call function, using both lists as the parameter
send_messages(message_list, new_message_list)
# print to verify list populated and current one is empty
print(new_message_list, message_list)

# 8.11, cont. from 8.10
print('\n')
# call the fucntion from 8.10 but with the parameter/copied current list. [:] means copy list, in this case would be the original list
send_messages(message_list[:], new_message_list)
# verify the list have changed
print(message_list, new_message_list)