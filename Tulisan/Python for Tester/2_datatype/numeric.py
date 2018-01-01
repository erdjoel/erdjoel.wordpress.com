from decimal import *

# 0, 0.0 is false
an_int = 5
a_binary = 0b10010
an_octal = 0o127
a_hex = 0x2F
a_float = 5.7
a_decimal = Decimal('3.0')

an_int_from_float = int(5.3)  # 5
an_int_from_string = int('7.4')
an_int_from_hex = int(0xAB34)
an_int_from_different_base = int('AB34', 16)  # value, base-16 (hex). Result = 43828

a_float_from_string = float('7.4')
a_float_from_int = float(99)
# note: float() cannot handle different bases

a_decimal_from_string = Decimal('5.700')  # require importing decimal module.
# In decimal the zeros is maintained
print(a_decimal + a_decimal_from_string)  # 3.0 + 5.700 = 8.700

# Python floats have the same ranges as the underlying computer architecture.
# They also suffer the same levels of imprecision that make comparing float values a risky option.
a_decimal_from_float = Decimal(3.14)  # print(a_decimal_from_float) =
# 3.140000000000000124344978758017532527446746826171875 -- imprecision in float

"""Some note
Python provides modules for handling rational fractions ( fractions ) for precise fraction calculation
Python also natively supports imaginary number type called complex.
"""

# Order of Operation states * and / is performed before + and -
# Addition          +       x + y
# Subtraction       -       x – y
# Multiplication    *       x * y
# Exponent (Power)  **      x ** y (x to the y power)
# Floor Division    //      x // y (also called integer division. e.g. 5 // 2 = 2)
# Division 	        /       x / y
# Modulo            %       x % y (the remainder of x/y)

# binary operations
a_binary = 1  # 0b001
a_binary2 = 2  # 0b010

bitwise_and = a_binary & a_binary2  # 0b001 & 0b010 = 0b000 = 0
bitwise_or = a_binary | a_binary2  # 0b001 | 0b010 = 0b011 = 3
bitwise_xor = a_binary ^ a_binary2  # ob001 xor 0b010 = 0b011 = 3. XOR -> True if both side have different value.
bitwise_complement = ~a_binary  # ~ob001 = 0b110 = -2. switching each 0 to 1 and vice versa.
# note: on bit notation, first digit is to denote negative number ~ can't be typed directly

bitwise_left = a_binary << 2 # 0b001 << 2 = 0b0100 = 4. shift bit in a_binary to the left by 2 places.
bitwise_right = a_binary2 >> 1  # 0b010 >> 1 = 0b001 = 1. shift to right by 1 places.