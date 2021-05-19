# input() pauses the program and waits for the user to enter some text
welcome_user = input("Hi what is your name? ")
print(f'Welcome to the program {welcome_user.title()}!')

#using integer -int() to convert str to int
debt = input("\nHow much debt are you in? (enter # amount) ")
debt = int()

if debt <= 30_000:
    print('That is not bad!')
else:
    print('Fuck'.capitalize())

# modulo operator - didvends one number by another number and returns the remainder ONLY
print('\n')
print(10%2)
print(11%2)
