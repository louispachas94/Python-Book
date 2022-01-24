

# 8.12 
print('\n')
#set up fucntion with parameter
def sandwich_orders(*toppings):
# set up first part of sumarry
    print('making a sandwhich')
# loop thru 
    for topping in toppings:
        print(f'Sandwhich will have: {topping}')

sandwich_orders('cheese','ham',' beef')
sandwich_orders('cheese','ham',' spinich')
sandwich_orders('cheese','mayo''roast beef',' beef')

# 8.13
print('\n')
# **parameter
def user_profile(fistname, lastname, **extra):
# **parameter[dictionary name] = content
    extra['firstname'] = fistname
    extra['lastname']=lastname
    return extra
user = user_profile('louis','pachas', month ='dec', date = 8, year = 1994 )
print(user)

# 8.14
print('\n')
def car(manufacture, models, **car_info):
    car_info['manufacture'] = manufacture
    car_info['model'] = models
    return car_info
cars = car('ford','f150',color = 'red', insurence = 'geico')
print(cars)

# 8.15
#alt to use fucntion from another file/module
print('\n')
from pizza import pizza_order
pizza_order(20,'cheese')

# 8.16
# copied car function to car.py
print('\n')
import car
from car import car
import car as cars
from car import *
from car import car as carz

# 8.17
def printing(
    number,math):
    for py in number:
        print(f'this many {py}{math}')
printings=(3,9)
printing(printings)