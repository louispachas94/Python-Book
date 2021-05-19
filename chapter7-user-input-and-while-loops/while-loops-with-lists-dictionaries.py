# moving items from one list to another
""" example users who havent been verified,
and an empty list to hold confirmed users
"""
unconfirmed_users = ['jenny', 'louis', 'rocky']
confirmed_users = []

""" verify each user until there are no more unconfirmed users
move each verified user into the list of confirmed users
"""
while unconfirmed_users:
    # removes the last value in unconfirmed_users
    current_users = unconfirmed_users.pop()

    print(f'\nLooking to confirm: {current_users.title()}')
    # add the removed values in unconfirmed_users to confirmed_users
    confirmed_users.append(current_users)
    # display all confirmed users ath the end of program; make sure its out of the while loop
print('\nThe following users have been confirmed: ')
for confirmed in confirmed_users:
    print(confirmed.title())

# Removing all instances of specific values from a list
    # remove() to remove a specific value in a list; one at a time
food = ['pizza','fish','sandwich','pizza','chips','pizza']
    # loop through the list food with pizza in mind
while 'pizza' in food:
    # in going through each loop remove pizza; when no pizza value is left is when the program ends
    food.remove('pizza')
    # list without any piza value; original had 3
print(food)

# Filling a dictionary with user input
responses = {}

    # set a flag to active
polling_active = True

while polling_active:
    # prompts for users name and response input
    name = input("What is your name? ")
    response = input("Which Nike cleats do you like? ")

    # store the name & response in the dictionary
        # dictionary name[key] = value
    responses[name] = response
    print(responses)

    # If done or not going to take poll
    next_user = (input('Finish? (yes or no)'))
    if next_user == 'yes':
        polling_active = False

    # results
    print('\nResults are here:')
    # for loop through the dictionary {responses} and print
    for name,response in responses.items():
        print(f'Name: {name} - Response: {response}')
