#for loop simpl ex.
brands= ['nike','adidas','puma']

for each_items in brands:
    print(f'\nthese are the brands I like to wear: {each_items}')
    #with title method after the above statement
    print(f'\tbut there are other brands than just {each_items.title()}')

#making numumerical lists
    #using for loop
for value in range(1,11):
    print(value)
    #using list(range(start, end +1))
num = list(range(1,12))
print('\n')
print(num)

#making a list 1-10 * 2 using range
doubles =[]
print('\n')
for number in range(1,11):
    #could also do doubles.append(number*2) and then just print
    double = number*2
    doubles.append(double)

print(doubles)
print('\n')

#find max,min,sum
print(max(doubles))
print(min(doubles))
print(sum(doubles))

#list comprehensions
print('\n')
    #triple from 1-11, values*3; one liners
triple=[valuez*3 for valuez in range(1,12)]
print(triple)

