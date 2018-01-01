1. create a simple, conventional module based on integer inputs.
2. then create another module that defines a class that can be used to represent a piece of binary data and expose the bitwise functions as methods.
3. create a package containing both modules.

TRY IT OUT Creating a Module
1. Create a new folder called bitwise. This eventually becomes your package.

2. In that folder create a Python script called bits.py containing the following code (or load it from
the book’s downloadable filenamed bits.py ):

#! /bin/env python3
''' Functional wrapper around the bitwise operators.
Designed to make their use more intuitive to users not
familiar with the underlying C operators.
Extends the functionality with bitmask read/set operations.
The inputs are integer values and
return types are 16 bit integers or boolean.
bit indexes are zero based
Functions implemented are:
NOT(int) -> int
AND(int, int) -> int
OR(int,int) -> int
XOR(int, int) -> int
shiftleft(int, num) -> int
shiftright(int, num) -> int
bit(int,index) -> bool
setbit(int, index) -> int
zerobit(int,index) -> int
listbits(int,num) -> [int,int...,int]
'''
def NOT(value):
	return ~value

def AND(val1,val2):
	return val1 & val2

def OR(val1, val2):
	return val1 | val2

def XOR(val1,val2):
	return val1^val2

def shiftleft(val, num):
	return val << num

def shiftright(val, num):
	return val >> num

def bit(val,idx):
	mask = 1 << idx # all 0 except idx
	return bool(val & 1)

def setbit(val,idx):
	mask = 1 << idx # all 0 except idx
	return val | mask

def zerobit(val, idx):
	mask = ~(1 << idx) # all 1 except idx
	return val & mask

def listbits(val):
	num = len(bin(val)) - 2
	result = []
	for n in range(num):
		result.append( 1 if bit(val,n) else 0 )
	return list( reversed(result) )

3. Save the file and, while still in your bitwise folder, start the Python interpreter.

4. Type the following code to test your new module:
>>> import bits
>>> bits.NOT(0b0101)
-6
>>> bin(bits.NOT(0b0101))
'-0b110'
>>> bin(bits.NOT(0b0101) & 0xF)
'0b1010'
>>> bin(bits.AND(0b0101, 0b0011) & 0xF)
'0b1'
>>> bin(bits.AND(0b0101, 0b0100) & 0xF)
'0b100'
>>> bin(bits.OR(0b0101, 0b0100) & 0xF)
'0b101'
>>> bin(bits.OR(0b0101, 0b0011) & 0xF)
'0b111'
>>> bin(bits.XOR(0b0101, 0b11) & 0xF)
'0b110'
>>> bin(bits.XOR(0b0101, 0b0101) & 0xF)
'0b0'
>>> bin(bits.shiftleft(0b10,1))
'0b100'
>>> bin(bits.shiftleft(0b10,4))
'0b100000'
>>> bin(bits.shiftright(0b1000,2))
'0b10'
>>> bin(bits.shiftright(0b1000,6))
'0b0'
>>> bits.bit(0b0101,0)
True
>>> bits.bit(0b0101,1)
False
>>> bin(bits.setbit(0b1000,1))
'0b1010'
>>> bin(bits.zerobit(0b1000,1))
'0b1000'
>>> bits.listbits(0b10111)
[1, 0, 1, 1, 1]

How It Works
The module is a fairly straightforward list of functions that wrap the built-in bitwise operators for not
( ~ ), and ( & ), or ( | ), xor ( ^ ), shift left ( << ), and shift right ( >> ). These operations work on binary data—that
is, simply a sequence of 1s and 0s stored as a unit within the computer. All data in the computer is,
ultimately, stored in binary form.

These wrapper operations are complemented by a set of functions that test whether a bit has a value of
1 (this is known as being “set”), set a bit (to 1), or zero a bit (also known as “resetting” the bit). The bit
number counts from the right, starting at zero. The tests are done using a bit pattern (also known as a
bitmask) that, in all cases except zerobit(), consists of all zeros except for the bit you want to test or
set. You created the mask by shifting 1 left by the required number of bits. zerobit() uses the bitwise
complement of the usual mask to create one that consists of all 1s apart from a 0 where you want to
reset the bit.

Finally, you have a function that lists the individual bits of the given value. This last function is slightly
more complex and demonstrates some of Python’s coding features. You first determine the length of the
number by converting to a binary string with bin() and subtracting 2 (to account for the leading 0b
characters). You then create an empty result list and loop over the bits. For each bit you append either a
1 or 0, depending on whether or not the bit is set, using Python’s conditional expression construct.

The testing of the module throws up some interesting issues. You start off by importing your new
module. Because you are in the folder where the file lives, Python can see it without modifying the
sys.path value. You start testing with the NOT() function (prefixed, of course, with the module name,
bits ), and straightaway you can see an anomaly in that the Python interpreter prints the decimal
representation as the result. To get around that, you can use the bin() function to convert the number
to a binary string representation. However, there is still a problem because the number is negative. This
is because Python integers are signed, that is, they can represent positive or negative numbers. Python
does this internally by having the leftmost bit represent the sign. By inverting all of the bits, you also
invert the sign! You can avoid the confusion by using a bitmask of 0xF (or decimal 15 if you prefer) to
retrieve only the rightmost 4 bits. By converting this with bin(), you now see the inverted bit pattern
you expected. Obviously, if the value you were inverting was bigger than 16, you would need to use a
longer bitmask. Just remember that each hex digit is 4 bits, so all you need to do is add an extra F to
your mask.

The next set of tests—covering the functions AND() through to shiftleft() —should be
straightforward, and you can check the results by visually inspecting the input bit patterns and the
results. The shiftright() examples do show one interesting outcome in that shifting the bits too far
to the right produces a zero result. In other words, Python fills the “empty” space left by the shift
operations with zeros.

Moving on to the new functionality, you used bit(), setbit(), and zerobit() to test and modify
individual bits within the given value. Again, you can visually inspect the input and result patterns to
see that the correct results are produced. Remember that the index parameter counts from zero starting
from the right.

Finally, you tested the listbits() function. Once more, you can easily compare the binary input
pattern with the resultant list of numbers.

So you see that you now have a working module that you can import and use just like any other
module in Python. You could enhance the module further by providing a test function and wrapping
that in an if __ name __ clause if you wanted, but for now you can proceed to look at how to move
from a single module to a package.

