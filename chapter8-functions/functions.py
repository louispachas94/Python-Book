# functions
# () - is used to add information to run fucntion; check def line to see if anything is in the ()
# example:
def hello():
    print('hello world')
# calling hello fucntion
hello()

# example with infomartion (parameter) needed from ()
def hello_user(username):
    print(f'\nHello {username}, welcome to the app!')
hello_user('louis')

# info passed into fucntion is called parameter
# the value of the parameter is called an argument

# postional arguments -arguments for a function that have multiple arguments
def laptop_owned(os, brand):
    print(f'\nMy laptop brand is a {brand} and runs {os}')
    print(f'System OS is {os}')
laptop_owned('linux', 'lenovo')

# multiple fucntion call - can call a functuion multiple times with different arguments
laptop_owned('macos', 'apple')

# keyword arguments - name value pair that you must pass to a function; directly associating a argument to a parameter
# ex. laptop_owned(os = 'macos', brand= 'macbook')

# Default value: defualt value for a parameter; used when you want to set a parameter default value
# you can overide value by when calling function and put parameter = 'overide_value'
# ex. def laptop_owned(os = 'macos', brand)

# avoide argument errors - unmatched arguments when inputting too few or too many arguments

""" return values - not always needs to print output, it can process data and then return a value or set of values. value the fucntion returns is
a return value"""
# return statement takes a value from inside a function and sends it back to the line that called the function
# ex.
print('\n')
def full_name_formatted(first, last):
    #  no print, associate value to a variable
    fullname  = f'{first} {last}'
    # return statement takes value from function
    return fullname
    #new variable whos value is the function with arguments
name_test = full_name_formatted('louis', 'pachas')
    #print variable name_test
print(name_test)

    #^^^ done; below while loop was added as fucntion already is set so adding a while loop after fuicntion call is easy
    # using a fucntion with a while loop
while True:
    print('\nPlease tell us your name?')
    print('Enter q to quit')
    first_name = input('Enter your first name? ')
    if first_name == 'q':
        break
# making an argument optional - optional parameter needs to be at the end of all parameters in the fucntion definition
# ex.
print('\n')
# optional parameter as last parameter and give value empty string
def name_with_middle(first_n, last_n, middle_n = ''):
    # IF when function is called and a argument is provided for middle_n parameter 
    if middle_n:
    # full_name is formatted to place middle_n inbetween first_n and last_n
        full_name = f'{first_n} {middle_n} {last_n}'
    # IF no argument is provided for middle_n parameter
    else:
    # full name is formatted without middle_n
        full_name = f'{first_n} {last_n}'
    #return statment
    return full_name
    # assicoaite variable to the function and provide the arguments for all parameter or only needed ones
test_middle_name = name_with_middle('louis', 'pachas', 'michael')
test_no_middle_name = name_with_middle('louis', 'pachas')
    # print variable
print(test_middle_name)
print(test_no_middle_name)

# function that returns a dictionary
print('\n')
def build_person(first_name, last_name):
    # return a dictionary of info about a person
    # assigns fucntion arguments to dictionary's value
    person = {'first': first_name, 'last': last_name}
    # return statement
    return person
    # accosicate fucntion to a variable
baby_name = build_person('jeni', 'corona')
print(baby_name)

# passing a list in a fucntion
    # add a parameter to fucntion
def greet_user(name):
    # since argument will be a list; need a for loop to hit all
    for names in name:
    # message with f string
        greeting = f'Hello {names.title()}'
        print(greeting)
    # call function with a list as the argument
greet_user(['louis', 'jenny', 'mike'])

# Modifying a list in a function
    # main idea is to show functions can be split; so one does only one thing; scalability
print('\n')
def print_model(unprinted_desings, printed_designs):
    # setting up parameter
    # while true
    while unprinted_desings:
    # create a varible with value being .pop unprinted_desings list
        current_design = unprinted_desings.pop()
    # print value of current_desings
        print(f'Printing Model: {current_design}')
    # add current_design value to printed_design list data type
        printed_designs.append(current_design)

def show_completed(printed_designs):
    print('These have been printed:')
    # for loop on printed_desings to print list values
    for showing in printed_designs:
        print(showing)
    # create list with values
unprinted_desings = ['4k', 'hd', '720', '8k']
    # blank list; which will be filled by above list
printed_designs = []
    # call print_model function with arguments
print_model(unprinted_desings, printed_designs)
    # call show_completed function with arguments
show_completed(printed_designs)
