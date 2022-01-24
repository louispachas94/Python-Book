# passing arbitrary number of arguments
# fucntions that can collect a arbitrary # of arugments from the calling statement

# ex. a function of pizza toppings but unlimted toppings can be requested, * is the key part
# output will be a tuple, even if its one item
def new_pizza(*toppings):
    print(toppings)

new_pizza('pep')
new_pizza('sau', 'pep', 'mushroom','veggies','ham','cheese')

# another ex. without knowing # of arguments. print call can be dropped and instead use a loop
print('\n')

def new_burger(*sauces):
    for sauce in sauces:
        print(f'These sauces will be added to the order - {sauce}')

new_burger('mustard')
new_burger('mustard','keptup','bbq','ranch','hot','soy sauce')

# mixing parameter positional in a function and arbitrary arguments
# parameter with the *(# of arguments) needs to be the last one if 2 or more parameters are set for the function
print('\n')

def pizza_order(size, *toppings):
        print(f'Pizza size - {size}')
        for topping in toppings:
            print(f'Pizza topping/s - {topping}')

pizza_order(16, 'sau', 'pep', 'mushroom','veggies','ham','cheese')

# using arbitrary keywords argments
# accepts as many key-value pairs, outputs to a dictonary
print('\n')
# create function, set parameters with last one with **, 
def profile_builder(firstname, lastname, **user_info):
# assign 1st & 2nd parameters to arbitary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    user_info['first'] = firstname
    user_info['last'] = lastname
    return user_info

test = profile_builder('louis','pachas',sport = 'soccer')
print(test)