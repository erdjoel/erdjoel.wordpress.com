# Generator functions is a functions except that use the keyword yield .
# When a standard function reaches a return statement, it returns the value and the function
# then throws away all of its internal data. The next time the function is called, everything starts off
# from scratch.

# The yield statement returns a value, just like return does, but the function preserved everything.
# The next call of the function picks up from the yield statement, even if that’s in the middle of a block
# or part of a loop.

# There can even be multiple yield statements in a single function.

def odds(start=1):
	"""return all odd numbers from start or the next highest odd integer
	note: odd = ganjil
	"""
	if int(start) % 2 == 0: start = int(start) + 1
	while True:
		yield start
		start += 2

# generator functions can become iterators
for n in odds():
	if n > 7: break  # to avoid infinite loop
	else: print(n)

# NOTE: If you use odds() a second time in the same program, it creates a brand-new instance of the iterator and the sequence starts over.
