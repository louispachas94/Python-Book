#tuples use () and need at least one comma (,) to work
#tuples are immutable - cant change values with indexing like lists
first_tuple=(4,4,2,1,1,1)
print(first_tuple)
print('\n')

print(f'this is the first values in the tuple {first_tuple[0]}')

#looping through all values in a tuple
print('\n')
for number in first_tuple:
    print(number)

print('\n')

#writing over a tuple
#overwrite the tuple with a new one using the same tuple name 
nike=('vapor','legend','magista','t90')
print('These are the nike models original list:')
for shoes in nike:
    print(shoes)

nike=(55,3,2,11,10)
print('\nNewly list to ints:')
for shoes_two in nike:
    print(shoes_two)

