# 7.1
rental_car_pick = input("Hello, which rental car would you like? ")
print(f"\nThanks for making a choice, let me see if we have a {rental_car_pick}")

# 7.2
dinner_group_num = int(input("Hello, how many for your dinner group? "))
if dinner_group_num > 8:
    print('\nA table will be ready soon')
else:
    print('\nTable is ready now!')

# 7.3
get_num = int(input('Give us a number?  '))
if get_num % 10 == 0:
    print('\nthat is multiple of 10!')
else:
    print('\nnot a mulitple of 10')

# 7.4
    # look at solutions for alt. way to do this
pizza_prompt = '\nEnter pizza toppings you want (type quit if finish): '
while True:
    prompt = input(pizza_prompt)
    if prompt == 'quit':
        break
    else:
        print(f"\nI will add {prompt} to your pizza!")

# 7.5 - didnt complete on own
movie_prompt = "How old are you? (Enter quit when done) "
while True:
    person_age = input(movie_prompt)
    # if user enters quit,; kills program
    if person_age == 'quit':
        break
    # convert person_age to integer
    person_age = int(person_age)
    if person_age < 3:
        print('ticket is free!')
    elif person_age < 12:
        print('ticket is $10')
    else:
        print('ticket is $15')

# 7.6
""" For 7.5
part 1: 
part 2: create variable and assign value of True; instead of break change variable value to false to kill program
part 3: already there
"""

# 7.7
""" current_number = 0
while True:
    current_number += 1
    print(current_number)
"""

# 7.8
sandwich_orders = ['blt','tuna salad','steak cheese','vegan','grilled cheese']
finished_sandwiches = []
    # loop
while sandwich_orders:
    # removes last value in sandwich_orders
    current_sandwich = sandwich_orders.pop()
    # prints the string & f-string which is the value that was popped from above
    print(f'working on making you a {current_sandwich}')
    # add the popped value from sandwich_orders to finsihed_sandwiches
    finished_sandwiches.append(current_sandwich)
print('\n')
    # print final message of what was made
for sandwich in finished_sandwiches:
    print(f'I have made you a {sandwich}!')


# 7.9
sandwich_orders_v2 = ['pastarmi','blt','pastarmi','tuna','pastarmi']
print('We are out of pastarmi')
    # set up while loop of pastarmi in list
while 'pastarmi' in sandwich_orders_v2:
    # remove() method removes all pastarmi values in list
    sandwich_orders_v2.remove('pastarmi')
    # print list to verfify removal - needs to be outside of while loop
print(sandwich_orders_v2)

# 7.10
    # needs to come back dictinary so we can tie user and their vote
responses_back = {}
    # set flag to show polling is active
polling_active = True
    # while true
while polling_active:
    # users inputs name and response 
    users_name = input("what is your name? ")
    users_response = input('what is your dream vacation? ')
    # add key & value to responses_back
    responses_back[users_name] = users_response
    print(responses_back)

    # after all users responded; break out loop
    last_user = input('was that all the users? yes or no ')
    if last_user == 'yes':
        polling_active = False
    
    # results; dont forget to check spacing and out of block of a loop
print('\nResults:')
for user,answer in responses_back.items():
    print(f'User: {user} & Response {answer}' )