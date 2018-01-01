
"""For Loop usage
for item in <iterable>:
	code block
else:  # executed when all the iterations are completed. will not be executed if the loop exits via a break or return.
	another code block

"""

# exit out of a for loop:
# break statement, which exits the loop immediately,
# return statement
# continue. exits the block for the current loop iteration only.

# common function used with for loops: enumerate().
# enumerate() returns tuples containing both the iterable item and a sequence number
# enumerate() takes a second optional argument for sequence starting number, starting with 1 rather than the 0.
for number, line in enumerate(open('myfile.txt'), 5):  # open myfile.txt and read starting line 5
    print(number, '\t', line)

# sample
for x in range(0, 10):
    print(x, sep=' ', end="*")

# You can use for loops to cycle through a list
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']

for y in grocery_list:
    print(y)

# You can also define a list of numbers to cycle through
for x in [2, 4, 6, 8, 10]:
    print(x)

# You can double up for loops to cycle through lists
num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])

# using list comprehension
for each_item in [n * n for n in range(1, 11) if not n * n % 2]:
    print(each_item)
