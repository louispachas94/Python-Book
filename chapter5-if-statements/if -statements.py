# if, elif, else example

pizza_price = 90

if pizza_price < 12:
    print('cheap')

elif pizza_price<11.8:
    print('cheaper')

else:
    print('WOW')

print('\n')

#testing multiple conditions
pizza_toppings = ['pep','sausage','pesto','spinich','chesse']

if 'mushroom' in pizza_toppings:
    [print('Add this')]

if 'pep' in pizza_toppings:
    print('we have added this')

if 'pesto' in pizza_toppings:
    print('this is already added')
print('\n')

#checking for value in a list
for toppings in pizza_toppings:
    if toppings == 'chesse':
        #printed last because going thru list, its the last value 
        print('Sorry we are out !')
    else:
        print(f'adding the toppings of {toppings}')
print('pizza made')

#checking if list is empty
print('\n')

fruit=[]
if fruit:
    for name in fruit:
        print(f'here are the names:{name}')
else:
        print('\nNothings in the list')

#using multiple lists
print('\n')

new_toppings = []
not_pizza_toppings = ['fries','ice cream','pancakes']

for is_ava in not_pizza_toppings:
    if is_ava in pizza_toppings:
        print('not ava')
    else:
        print('we dont support that')

print('those are the only things avaliable')
