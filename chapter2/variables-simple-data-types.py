#2.1
message_one = 'hello world'
print(message_one)

#2.2
message_two = 'hello universe'
print(message_two)

message_two = 'hello solar system'

print(message_two)

#Strings

#changing case (title, upper, lower) these are methods so need .() after
#\n is just for new line
name = '\nLouis pachas'
print(name.title())
name_one = '\npachas'
print(name_one.upper())
name_two = '\nLOUIS'
print(name_two.lower())

#f strings
gf = 'Jenny'
print(f'\nI love you {gf} so much')

#strip method; close in on white spaces; .strip()
whitespaces_right = 'testng     '
whitespaces_left = 'testingg        '
whitespaces_both = '         testing       '

print(whitespaces_right.rstrip())
print(whitespaces_left.lstrip())
print(whitespaces_both.strip())


#2.3
name_2='Jenny   '
print(f'Hello {name_2.rstrip()} how are you doing today?')

#2.4
print(name_two.lower())
print(name_two.title())
print(name_two.upper())

#2.5
print('\n\tRic Flair once said "To be the man, you have to beat the man"')

#2.6

famous_person = 'Ric Flair'
print(f'{famous_person} once said "To be the man, you have to beat the man"')


#2.7
name_three = '  Jenifer                       '
print(name_three.strip())
print(name_three.lstrip())
print(name_three.rstrip())

print(f'\n\t{name_three.strip()}')