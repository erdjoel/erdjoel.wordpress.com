# Reading files
myFileObj = open(filename, 'w')
# other modifier:
# 'r' read-only (default mode, can be omitted)
# 	'r+' read and write. Doesn't create the file if not exist. Seek(0) will change the append behaviour to insert text where the index is set (instead of at the end)
#	'rb', 'r+b'
# 'a' append
#	'a+' read and append. Will also create the file if required. Seek(0) doesn't change the position where the text will be appended (always at the end).
#	'ab', 'a+b'
# 'w' read and write. will create the file if not exist.
#	'w+' open-clear all content-write. Use this if you always want to start with empty file
#	'wb', 'w+b'
# On Windows, 'b' appended to the mode opens the file in binary mode, so there are also modes like 'rb', 'wb', and 'r+b'.
# Python on Windows makes a distinction between text and binary files; in text files the end-of-line characters are automatically altered slightly when data is read or written.
# This behind-the-scenes modification to file data is fine for ASCII text files, but it’ll corrupt binary data like that in JPEG or EXE files.

myFileObj.name		# get the file name
myFileObj.close()		# Closes the file. Like File->Save.. in your editor. ALWAYS close the object
myFileObj.truncate()	# Empties and Save the file. Watch out if you care about the file.
myFileObj.read()		# Reads the contents of the file. You can assign the result to a variable.
myFileObj.readline()	# Reads just one line of a text file.
myFileObj.write(stuff)	# Writes stuff to the file.
myFileObj.mode		# Get the file mode.


with open("tmp.txt", "w") as tmp:
	print("Hello", "World", end="END", sep="-", file=tmp)

with open('somefile.txt', 'w+') as f:
    f.write('somedata\n')		# f now point to the end of file
    f.seek(0)		# reset f position to beginning of text
    data = f.read()	# returns 'somedata\n'



import traceback		# to obtain the exception as a string by calling raceback.format_exc()
try:
	raise Exception('This is the error message.')
except:
	errorFile = open('errorInfo.txt', 'w')
	errorFile.write(traceback.format_exc())
	errorFile.close()