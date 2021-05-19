#5.1
given_shot='vaccinated'

print('Have you been vaccinated yet: ?')
print(given_shot == 'not vaccinated')

print('\n')

#if given_shot == False:
#    print('You should look for an appt.')
#else:
#        print('Ok good')

#5.2
print('st' == 'og')
#more examples....
print('\n')

#5.3
alien_colors = 'red'

#no output
if alien_colors == 'green':
    print('5pts')

#true; yes output
if alien_colors == 'red':
    print(f'The creatures color is {alien_colors}')

#no output
if alien_colors == 'yellow':
    print('is there an output here?')

print('\n')

#5.4
if alien_colors == 'green':
    print('5pts')
else:
    print('\n10pts')

#5.5
if alien_colors == 'green':
    print('5pts')
elif alien_colors == 'yellow':
    print('10pts')
else:
    print('\n=15pts')


#5.6
age = 65

print('\n')

if age < 2:
    print('This person is a baby')
#rememeber since elif is the the else part of this cond. test, we play off the previous cond test
elif age < 4 :
    print('This person is a toddler')
elif age < 13:
    print('This person is a kid')
elif age < 20:
    print('This person is a teenager')
elif age < 65:
    print('This person is a adult')
# else:   could also work
elif age >= 65:
    print('This person is a elder')

#5.7
print('\n')

favorite_fruit = ['blueberries','apple','mango']
if 'cherry' in favorite_fruit:
    print("you like cherrys")
if 'berry' in favorite_fruit:
    print("you like berrys")
if 'apple' in favorite_fruit:
    print("you like apple")
if 'kiwi' in favorite_fruit:
    print("you like kiwi")
if 'watermelon' in favorite_fruit:
    print("you like watermelon")

#5.8
print('\n')

users = ['jenny','louis','rocky','admin','steve']
for greetings in users:
    if greetings == 'admin':
        print('\nHello admin, these are the systems report.')
    else:
        print(f'Welcome {greetings} to the home page.')

#5.9
print('\n')

if users:
    for user in users:
        print(f'these are the names of users {user}')
else:
    print('\nWe need list')
#Works when user list is empty

#5.10
print('\n')

current_users = ['lobo','jairo','mom','dad','brother']
new_users = ['dad','mom','che','santos','perukid']

for username_check in new_users:
    if username_check in current_users:
        print(f'\nWe are going to need a new username for: {username_check}')
    else:
        print(f'This username works: {username_check}')

#5.11
print('\n')

numbers = [1,2,3,4,5,6,7,8,9]
for num in numbers:
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{num}th')