#4.1 -Pizzas
pizzas = ['sausage','pep','mushroom']
for yum in pizzas:
    print(f'\tI really like this toppings {yum} from MOD pizzas')
print('Mod pizzas are so good')

#4.2
animals = ['dog','cat','fish']
print('\n')
for pets in animals:
    print(f'\tThis animal called {pets.title()} are good creatures')

print('\tthese are all good pets')


#4.3
for twenty in range(1,21):
    print(twenty)
print('\n')

#4.4
    #list that has 1- a million
million = list(range(1,1000001))
    #verify list printed right
#print(million)

#takes long for output, FYI

    #for loop to print list
#for each in million:
 #   print(each)

#4.5
one_million = list(range(1,1000001))

print(min(one_million))
print(max(one_million))
#sums up a list 1-1m 
print(sum(one_million))

print('\n')
#4.6

for odd in list(range(1,21,2)):
    print(odd)
print('\n')
#4.7
for three in list(range(3,31,3)):
    print(three)

print('\n')

#4.8
#make a prelist and use append to add to list so u can print outside the for loop
cubes_4_8=[]
for cubes in range(1,11):
    cubes_4_8.append(cubes**3)

print(cubes_4_8)

#4.9
    #could remove the list part before range - still work
cubes_2 = [cubes_3**3 for cubes_3 in range(1,11)]
print(cubes_2)

#4.10
print('\n')
list_1= ['one','two','three','four','five','six','seven','eight','nine']

for firsts in list_1[0:3]:
    print(f'The first 3 items in the list are: {firsts}')

print('\n'
)

for halfs in list_1[3:6]:
    print(f'the middle 3 items in the list are: {halfs}')

print('\n')

for final in list_1[6:10]:
    print(f'the final 3 items in the list are {final}')

print('\n')

#4.11
friend_pizza =pizzas[:]
print(friend_pizza)

pizzas.append('pesto')
friend_pizza.append("chicken")

print('my friends favorite pizzas are:')
for pizza in friend_pizza:
    print(pizza)

print('\n')

print('my favorite pizzas are:')
for pizzaz in pizzas:
    print(pizzaz)

print('\n')

#4.12 ? not clear directtion

#4.13
buffet_food=('pizza','ice cream','ribs','soup','fried rice')

#1st part
print('This is the original menu:')
for menu in buffet_food:
    print(menu)

#2nd part
    #buffet_food[0]='sliced ham'
    # was given an error message
print('\n')

#3rd part
buffet_food=('pizza','ice cream','ribs','salad','pasta')
print('This is the new and revised menu:')
for new_menu in buffet_food:
    print(new_menu)

print('\n')
