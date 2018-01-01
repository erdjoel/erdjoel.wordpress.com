"""While Loop
while BooleanExpression:
	aBlockOfCode
else:  # optional, rarely used. Executed when BooleanExpression is False, including when the loop exits normally.
	anotherBlock  # will not be executed if the loop is exited by a break or return statement.
"""

# exit out of a while loop:
# break statement, which exits the loop immediately,
# return statement
# continue. exits the block for the current loop iteration only.

while True:
    command = input('Enter a command[rwq]: ')
    if 'q' in command.lower(): break
    if command.lower() == 'r':
        continue
    elif command.lower() == 'w':
        # return 1
else:
    print('Invalid command, try again')

# other example
i = 0;
while i <= 20:
    if i % 2 == 0:
        print(i)
    elif i == 9:
        # Forces the loop to end all together
        break
    else:
        # Shorthand for i = i + 1
        i += 1
        # Skips to the next iteration of the loop
        continue

    i += 1
