In this Try It Out, you build a class that replicates the functions in bits.py as a set of methods. You
then bundle both modules into a package.

1. Navigate into your bitwise folder.

2. Create a new file called bitmask.py with the following code (or load it from the book’s
downloadable filename bitmask.py ):

#! /bin/env python3
''' Class that represents a bit mask.
It has methods representing all
the bitwise operations plus some
additional features. The methods
return a new BitMask object or
a boolean result. See the bits
module for more on the operations
provided.
'''
class BitMask(int):
	def AND(self,bm):
		return BitMask(self & bm)

	def OR(self,bm):
		return BitMask(self | bm)

	def XOR(self,bm):
		return BitMask(self ^ bm)

	def NOT(self):
		return BitMask(~self)

	def shiftleft(self, num):
		return BitMask(self << num)

	def shiftright(self, num):
		return BitMask(self > num)

	def bit(self, num):
		mask = 1 << num
		return bool(self & mask)

	def setbit(self, num):
		mask = 1 << num
		return BitMask(self | mask)

	def zerobit(self, num):
		mask = ~(1 << num)
		return BitMask(self & mask)

	def listbits(self, start=0,end=-1):
		end = end if end < 0 else end+2
		return [int(c) for c in bin(self)[start+2:end]]

3. Now save it so that you can test it in the Python interpreter.

4. Staying in the bitwise folder, start Python and type the following code:
>>> import bitmask
>>> bm1 = bitmask.BitMask()
>>> bm1
0
>>> bin(bm1.NOT() & 0xf)
'0b1111'
>>> bm2 = bitmask.BitMask(0b10101100)
>>> bin(bm2 & 0xFF)
'0b10101100'
>>> bin(bm2 & 0xF)
'0b1100'
>>> bm1.AND(bm2)
0
>>> bin(bm1.OR(bm2))
'0b10101100'
>>> bm1 = bm1.OR(0b110)
>>> bin(bm1)
'0b110'
>>> bin(bm2)
'0b10101100'
>>> bin(bm1.XOR(bm2))
'0b10101010'
>>> bm3 = bm1.shiftleft(3)
>>> bin(bm3)
'0b110000'
>>> bm1 == bm3.shiftright(3)
True
>>> bm4 = bitmask.BitMask(0b11110000)
>>> bm4.listbits()
[1, 1, 1, 1, 0, 0, 0]
>>> bm4.listbits(2,5)
[1, 1, 0]
>>> bm4.listbits(2,-2)
[1, 1, 0, 0]

5. Quit the interpreter.
Now that you have proved the new module works, you can go ahead and convert the bitwise
directory into a Python package.

6. Create a new empty __init.py__ file.

7. To test that the package works, you need to change your working directory to the directory above
bitwise. Do that now.
You now need to test that you can import the package and its contents and access the functionality.

8. Start the Python interpreter and type the following test code:
>>> import bitwise.bits as bits
>>> from bitwise import bitmask
>>> bits
<module 'bitwise.bits' from 'bitwise/bits.py'>
>>> bitmask
<module 'bitwise.bitmask' from 'bitwise/bitmask.py'>
>>> bin(bits.AND(0b1010,0b1100))
'0b1000'
>>> bin(bits.OR(0b1010,0b1100))
'0b1110'
>>> bin(bits.NOT(0b1010))
'-0b1011'
>>> bin(bits.NOT(0b1010) & 0xFF)
'0b11110101'
>>> bin(bits.NOT(0b1010) & 0xF)
'0b101'
>>> bm = bitmask.BitMask(0b1100)
>>> bin(bm)
'0b1100'
>>> bin(bm.AND(0b1110))
'0b1100'
>>> bin(bm.OR(0b1110))
'0b1110'
>>> bm.listbits()
[1, 1, 0]

How It Works
You created a class based on the built-in integer type, int. Because you are only providing new methods
for the class and not storing any additional data attributes, you don’t need to provide a __new__ ()
constructor or __init__ () initializer. The methods are all very similar to the functions written in
bits.py except that you created a BitMask instance as the return type. The listbits() method also
shows an alternative approach to deriving the list using the bin() string representation, and creating
the list using a list comprehension based on a character-to-integer conversion using int(). listbits()
has also been extended to provide a pair of start and end parameters that default to the full length of
the binary number, but could be used to extract a subset of bits. There is a small piece of work involved
in adjusting the end value depending on whether it is a positive or negative index. Negative indices do
not need the addition of two characters because they automatically apply from the right-hand end, so a
Python conditional assignment ensures the correct end value is set.

Having created the class, you then tested it as a standard module by importing it from the local
directory. You then repeated a similar set of tests to the ones you did for bits.py. A few points to
note include the fact that you can mix and match the traditional bitwise operators with the new
functional versions. You can also compare BitMask objects just like any other integer, as you saw in the
shiftright() example. Finally, you proved that your new listbits() algorithm worked and the new
additional arguments function as expected for both positive and negative values.

At this stage you had created two standard modules in a folder. You then created a blank __init__.py
file that turned the folder into a Python package. To test that it worked, you moved up a directory
level so that the package was visible to the interpreter. You then confirmed that you could import the
package and modules within it and access some of the functionality. Congratulations, you now have a
package with two contained modules.