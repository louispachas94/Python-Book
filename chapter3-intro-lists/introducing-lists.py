#fill a list with append method
fill_list = []
fill_list.append('honda')
fill_list.append('dodge')
#add to list with position in mind
fill_list.insert(1,'benz')

#removing an element from list - del
del fill_list[1]
#pop.() method pops the last element on the list
fill_list.pop()

print(fill_list)

new_list = [4,5,2,'item 1', 'yes',4.2]
#before pop methond
print(new_list)
#popped 5
new_list_2 = new_list.pop(1)
#print list without 5
print(new_list)
#print the element that was popped - 5
print(new_list_2)
#remove method using an item by value
new_list.remove('item 1')
print(new_list)
#remove method using an item by variable
four = 4
new_list.remove(four)
print(new_list)

print(f'\nmy car has {four} tires when riding it on the freeway')


#organizing a list
cars = ['bwm','ferrari','toyota','honda']
#method to have list go A-Z; sort(reverse=true) will Z-A
cars.sort()
print(cars)
print(len(cars))


autos = ['e320','ford','nissan','honda','subuaru']
print(autos)
#sorted(autos) function, is only a temp. when u use it
print(sorted(autos))
#only temp now we print
print(f'list of cars {autos}')

#reverse method
transportation= ['car','train','auto','boat','jog']
print(transportation)

#add method before print; it just reverse the original order of the list NOT Z-A
transportation.reverse()
print(transportation)

#len(add variable of list or add list) method to determind how many elements are in the list
print(len(transportation))

#extra ex.
lentght = len(transportation)
print(lentght)

#extra ex.
print(len([3,4,5,2,"hello world",4,5,5,6,6,5,34,3,2,2,1,11,0]))