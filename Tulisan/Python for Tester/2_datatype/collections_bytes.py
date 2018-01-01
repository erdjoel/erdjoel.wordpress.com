# A byte is an 8-bit value, equivalent to an integer from 0–255
# byte and bytearray

byte_from_string = b'Alphabet'
byte_array = bytearray(6548)
byte_array2 = bytearray('String', 'utf8')
print(byte_from_string[0])  # 65. int representation of A
c = b'A'

print(byte_from_string[0] == c)  # false. Accessing index 0 return int value of the string instead. 65 != 'A'
print(byte_from_string[0] == c[0])  # true. 65 = 65.

# Empty byte strings are treated as False in Boolean expressions.
