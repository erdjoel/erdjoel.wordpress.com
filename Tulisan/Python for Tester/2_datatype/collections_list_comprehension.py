# list comprehension

# <result expression> for <loop variable> in <iterable> if <filter expression>
[n*n for n in range(1,11) if not n*n % 2]  # [4, 16, 36, 64, 100] -- even number % 2 is 0

# other example: [pycFiles for name in names if name.endswith('pyc')] # return a list containing name endswith pyc

# looping list comprehension
for each_item in [n * n for n in range(1, 11) if not n * n % 2]:
    print(each_item)

# can be rewritten that as a conventional for loop, like this:
result = []
for n in range(1,11):
    if not n*n % 2:  #remember: 0 is false for Python
        result.append(n*n)
