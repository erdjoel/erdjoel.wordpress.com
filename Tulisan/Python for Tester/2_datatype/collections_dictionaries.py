# The key can be any immutable value, including a tuple. Keys must be unique.
# The value can be any kind of Python object, including another dictionary, a list, or anything else

empty_dictionary = {}  # treated as False
empty_dictionary2 = dict()
pet_names = {'cat': 'james', 'dog': 'hiro', 'tiger': 'strip'}

my_cat_name = pet_names['cat']

# The sorted() function returns a sorted list of keys if the keys are comparable.
list_of_pets_type = sorted(pet_names)  # Raises a TypeError If the keys are incompatible

# get
my_dog_name = pet_names.get('dog', 'tiger')  # get dog name or get tiger name if no dog in dictionary.
# Default value is None if not specified

# pop
my_dog_name = pet_names.pop('dog', 'tiger')  # get dog name, then remove it. get and remove tiger if no dog.
# Raise a KeyError if no default is given.

# setdefault
my_donkey_name = pet_names.setdefault('donkey', 'kong')  # get donkey. create {'donkey', 'kong'} entry if not available.

# fromkeys
my_stuffs = dict.fromkeys(['laptop', 'bag', 'bicycle'], 1)  # {'laptop': 1, 'bag': 1, 'bicycle': 1}
# create dictionary using a sequence as the keys and a given default value (or None if no value is given).

super_villains = {'Fiddler': 'Isaac Bowin',
                  'Captain Cold': 'Leonard Snart',
                  'Weather Wizard': 'Mark Mardon',
                  'Mirror Master': 'Sam Scudder',
                  'Pied Piper': 'Thomas Peterson'}

# Delete an entry
del super_villains['Fiddler']

# Replace a value
super_villains['Pied Piper'] = 'Hartley Rathaway'

len(super_villains)

# Get a list of dictionary keys
super_villains.keys()

# Get a list of dictionary values
super_villains.values()

for name, value in super_villains.items():
    print('{0} = {1}'.format(name, value))
    # fiddler = Isaac Bowin
    # Captain Cold = Leonard Snart
    # Weather Wizard = Mark Mardon
    # Mirror Master = Sam Scudder
    # Pied Piper = Thomas Peterson
