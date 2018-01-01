empty_string = ''  # treated as false in boolean expression.
single_quote_string = 'single'
double_quote_string = "using double quotes for longer text."
triple_single_quote = '''triple single quotes spanning
                        multiple lines is rarely used'''
triple_double_quote = """triple double quotes spanning
                        multiple lines is used for long, long text and docstring"""
single_quote_inside_double_quote = "This quote's format is acceptable"
double_quote_inside_single_quote = 'Used when you want to "quote" someone'

backslash = 'hello \\ python'  # hello \ python
# other escape characters
# \\			Backslash (\)
# \'			Single-quote (')
# \"			Double-quote (")
# \a			ASCII bell (BEL)
# \b			ASCII backspace (BS)
# \f			ASCII formfeed (FF)
# \n			ASCII linefeed (LF)
# \N{name}		Character named name in the Unicode database (Unicode only)
# \r			ASCII carriage return (CR)
# \t			ASCII horizontal tab (TAB)
# \uxxxx			Character with 16- bit hex value xxxx (Unicode only)
# \Uxxxxxxxx		Character with 32- bit hex value xxxxxxxx (Unicode only)
# \v			ASCII vertical tab (VT)
# \ooo			Character with octal value oo
# \xhh			Character with hex value hh

# string multiplication
multiply_string = "a" * 3  # result: aaa

upper_string = "case_to_convert".upper()  # other function: lower(), capitalize()

# * is just the filler -- can be replaced
string_center = "case to check".center(20, '*')  # centering, result: '***case to check****'
string_left = "case to check".ljust(20, '*')  # left justified, result: 'case to check*******'
string_right = "case to check".rjust(20, '*')  # right justified, result: '*******case to check'

# startswith, endswith
# preferred instead of string slicing
if "barcode".startswith('bar'):  # Avoid: if foo[:3] == 'bar':
	print('something!')

# able to test multiple substrings at once if they are passed as a tuple.
if "barcode".startswith(('ba', 'ar')):  # Check: starts with ba or ar?
	print('something!')  # True, it started with ba

# find, rfind. -1 on failure
# don't use: string.find('text', 'ter')
'caterpillar'.find('l')  # index of 'l' from the front = 7
'caterpillar'.rfind('l')  # first 'l' from behind = 8

# isalpha, isdigit, isalnum, isupper, islower, etc
# test the string content.
'pop'.isalpha()  # true. Alphabet.
'pop2'.isalnum()  # true. Alphanumeric.
'123'.isdigit()  # true. Digit/numeric.

# join
concat_string = single_quote_string + double_quote_string  # Avoid this. Inefficient operation.
concat_string = " - ".join([single_quote_string, double_quote_string])  # join should be used instead
# above code will join first and second string with " - " in the middle
# result will looks like: 'using single quotes - using double quotes'

# split, splitlines, partition
# split() a string into a list of substrings based on a given separator (default is whitespace).
# splitlines() returns a list of lines, effectively splitting using the newline character.
# partition() splits a string based on the given separator, but only up to the first occurrence;
# it then returns the first string, the separator, and the remaining string.
string_multiple_line = '''test
multiple
line of string'''
split_string = string_multiple_line.split()  # ['test', 'multiple', 'line', 'of', 'string']
split_line = string_multiple_line.splitlines()  # ['test', 'multiple', 'line of string']
partition_string = string_multiple_line.partition()  # ('test\nmultiple\nline', ' ', 'of string')

# strip, lstrip, rstrip
' test '.strip()  # 'test'. Strip whitespace from front and end.
' test '.lstrip()  # 'test '. Strip whitespace from front.
' test '.rstrip()  # ' test'. Strip whitespace from end.

# replace
'hello python, good morning.'.replace(' ', '-')  # 'hello-python,-good-morning.'

# format
count = 5
thing = 'some text'
print('{0}. {1}'.format(count, thing))  # format and print
print('{0:5}. {1!r}'.format(count, thing))  #     5. 'some text' -- :5 left padding 5 space, !r: format raw
print('{0:_<5}. {1!s}'.format(count, thing))  # 5____. some text -- :_<5 left padding 5 underscore, !r: format string
print('{0:_>5}. {1!a}'.format(count, thing))  # ____5. 'some text' -- :_>5 right padding 5 underscore, !r: format raw
print('{0:*^5}. {1!r}'.format(count, thing))  # **5**. 'some text' -- :*^5 left and right padding 5 asterisk, !a: format all

