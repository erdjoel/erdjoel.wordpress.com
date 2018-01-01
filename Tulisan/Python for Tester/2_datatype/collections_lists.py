# mutable
# can be unpacked like tuple
# index starting at 0

empty_list = []  # . All other lists are treated as True
another_empty_list = list()

mom_grocery_list = ['apple', 'banana', 'tomato']
dad_grocery_list = ['milk', 'tea', 'coffee']
bro_grocery_list = ['skateboard', ['guitar', 'banjo', 'violin']]  # a list can contain different object type

# get item of a list
second_item = mom_grocery_list[1]
third_item_in_second_item = bro_grocery_list[1][2]

# unpacking
item1, item2, item3 = mom_grocery_list

# slicing
mom_list_sliced = mom_grocery_list[1:3]

# change item
mom_grocery_list[1] = 'cabbage'

# +: concatenates two lists.
my_grocery_list = mom_grocery_list + dad_grocery_list

# * create a list of multiple copies of the first list.
# Note that the copies all refer to the same object,
# so when an object is modified. all instance is modified
my_grocery_list = mom_grocery_list * 2

# append: add an object to the end of a list
mom_grocery_list.append('spinach')  # modified in place, return None.

# extend: add the contents of a list to the end of another list
mom_grocery_list.extend(dad_grocery_list)  # modified in place, return None.

# pop: This removes an item from the end of a list or at the specified index. Returns the item.
last_item = mom_grocery_list.pop()
last_items = mom_grocery_list.pop(3)

# index: index of the first occurrence of an item in a list. Raise a ValueError if not found.
mom_grocery_list.index('tea')

# count: count object occurences
count_item = mom_grocery_list.count('tea')  # 1

# insert: This inserts an element before the specified index.
mom_grocery_list.insert(1, 'avocado')

# remove: removes the first occurrence of the specified item. Raise a ValueError if the item does not exist.
mom_grocery_list.remove('avocado')

# reverse: This reverses the elements of the list in-place.
mom_grocery_list.reverse()

# sort: sorts in-place.
mom_grocery_list.sort()

# To get a sorted copy of the list without modifying the
mom_grocery_list_copy = sorted(mom_grocery_list)

# del: deletes an item at specified index
del mom_grocery_list[4]

# Get length of list
len(mom_grocery_list)

# Get the max item in list
max(mom_grocery_list)

# Get the minimum item in list
min(mom_grocery_list)