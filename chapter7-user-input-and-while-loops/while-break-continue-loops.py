# While loops - runs as longs as the condtion of the statement is TRUE; as long as user wants them to
# ways to control the flow of a while loop: setting active flag, break, continue

starting_num = 0
while starting_num <= 4:
    # print goes first so it starts at the starting mark
    print(starting_num)
    '''after it prints the starting pt. it will continue which is to +1
     same as starting_num = starting_num + 1'''
    starting_num += 1 
    # after the +1, ptogram will loop back to the print line and print the starting pt. now with +1 until the statement is not true

# Using a Flag
prompt = '\nI will repeat what you will input: '
    # just extra str to mention if they input quit program will end; works without it
prompt += 'input quit to end '
    # active is flag set to true(could be named anything); will monitor wheater or not the program should continue running 
active = True
    # so while True...
while active:
    # so while this is true play the prompt message
    message = input(prompt)
    # if user's input == 'quit
    if message == 'quit':
    # if statment is true then program will not continue running; program stops
        active = False
    else:
    # else statement will loop back to start and print prompt/message from starting pt to loop again untill quit is entered which will kill the program
        print(message)

# Using break to exit a loop
""" break - to exit a while & for loop immediately without running any remianing code in the loop,
regardless of the results of any conditional test """
while True:
    new_ask = input('\nDo you like to play this game? ')
    if new_ask == 'no':
        break
    # will loop back until quit is entered to break loop
    else:
        print("\nGreat lets continue playing")

# Using continue in a loop
"""" continue - rather than breaking out of a loop; continue is used to return to the start of the 
loop based on the result of a conditional test """
    # starting point
current_num = 0
    # while current_num is LESS than 10
while current_num < 10:
    # current_num adding 1 to 0; one loop is just +1
    current_num = current_num + 1
    # if current_num divided by 2 has no remainder then it will NOT Print! continue will stop the program
    if current_num % 2 == 0:
    # kill program if it has 0 remainder
        continue
    # print the current_num numbers that when divided by 2 have remainders
    print(current_num)

# Avoiding infinte loops
    # make sure all while loops have a way to stop

