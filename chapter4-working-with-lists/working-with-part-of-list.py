#slicing ex. [0:3]; last argument should be not included; up until but not including

food_today = ['pizza','tuna','eggs','sausage','chips','water']
print(food_today[1:4])

print('\n')

#looping thru a slice

players = ['ronaldo','messi','neymar','paolo','jefferson','chorri','tapia','robinho']

for peruvian in players[3:7]:
    print(f'these are great {peruvian.title()} players')