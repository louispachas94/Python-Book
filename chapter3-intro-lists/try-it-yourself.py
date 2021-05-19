#3.4
guest_list = ['rocky','alfredo','martin','fieto']
print(guest_list)

#guest invites
#could also add new variable and assign a element from list to it - another way to do it
print(f'\tplease come to dinner {guest_list[0]}')
print(f'\tplease come to dinner {guest_list[1]}')
print(f'\tplease come to dinner {guest_list[2]}')
print(f'\tplease come to dinner {guest_list[3]}')

#3.5
print(f'\nsucks but {guest_list[3]} will not be able to make it')
#could also use del(guest_list[]) & guest_list.insert(part of list, variable or string or integer)
guest_list[3]= 'Jenny'
print(guest_list)

#new guest invites
print(f'\tplease come to dinner {guest_list[0]} newer')
print(f'\tplease come to dinner {guest_list[1]} new')
print(f'\tplease come to dinner {guest_list[2]} new')
print(f'\tplease come to dinner {guest_list[3]} new')

#3.6

print(f'great news, we found a bigger table {guest_list}')
guest_list.insert(0,'Jairo')
guest_list.insert(2,"james")
guest_list.append('arturo')
print(guest_list)
print(f'\tplease come to dinner {guest_list[0].title()} newer')
print(f'\tplease come to dinner {guest_list[1].title()} newer')
print(f'\tplease come to dinner {guest_list[2].title()} newer')
print(f'\tplease come to dinner {guest_list[3]} newer')
print(f'\tplease come to dinner {guest_list[4]} newer')
print(f'\tplease come to dinner {guest_list[5]} newer')
print(f'\tplease come to dinner {guest_list[6]} newer')

#3.7
print(guest_list)
print(f'sorry looks like we need to make this only 2 ppl {guest_list}')

#removed using pop() method
print(f'sorry {guest_list.pop()} we have to cancel')
print(f'sorry {guest_list.pop()} we have to cancel')
print(f'sorry {guest_list.pop()} we have to cancel')
print(f'sorry {guest_list.pop()} we have to cancel')
print(f'sorry {guest_list.pop()} we have to cancel')

rocky = guest_list[1].title()
jairo = guest_list[0]

print(f'\t\nWe are still on for dinner {jairo}')
print(f'\t\nwe are still on for dinner {rocky}')

#removed last elements using del 
del guest_list[0]
del guest_list[0]

#list empty
print(guest_list)

#3.8

places = ['lima','la','sf','nyc','miami','hayward']

#original
print(places)

#with sorted() function
print(sorted(places))

#original
print(places)

#with sorted() function, but reverse
print(sorted(places,reverse=True))

#original
print(places)

#reverse
places.reverse()
print(places)

#reverse back to original
places.reverse()
print(places)

#sort() method A-Z
places.sort()

print(places)

#sort() method Z-A
places.sort(reverse=True)
print(places)

#3.9
#created varibale with len() as element, and printed an f string using variable. using same list previous ex.
guests_number = len(guest_list)
print(f'we need a table that can have {guests_number} of chairs available to sit.')

#3.10
states = ['penn','florda','ny','','california','illiones','texas','alabama','north carolina','new jersey','arizona']
print(states)

#sorted fucntion
print(sorted(states))

#sort
states.sort()
print(states)

#sort Z-A
states.sort(reverse = True)
print(states)

#pop()
states.pop()
print(states)

#del
del states[2]
print(states)

#append
states.append('nevada')
print(states)

#insert with choice of spot
states.insert(3,'new mexico')
print(states)

#len
print(len(states))

#remove
states.remove('new mexico')
print(states)

#print always the last element of the list

#since this came before the new element it will go off up until before the insert
print(states[-1])
states.insert(11,'test')
print(states)
#still prints last element
print(states[-1])

#error to find answer
print(len(states))
print(states[10])
#no element in 13th spot, since list only goes to 10 elements, but start at 0 when counting