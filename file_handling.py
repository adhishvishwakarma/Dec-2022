## File handling ##

# open
# operation
# close

# Modes
# reading - r
# writing - w
# append - a


f = open('file.txt', 'r')  # opening the file

# print(f.read())  # performing read operation
#
# f.close()  # closing the file

# print(f.read(10))  # My first f
# print(f.read(3))  # ile
# print(f.read(10))  # /nThis is s
#
# print(f.tell())  # Telling the cursor's position
# print(f.seek(10))  # Setting the cursor's position
#
# print(f.read(2))

# print(f.read(13))
# print(f.read())

# for line in f:
#     print(line)

# print(f.readlines())  # Gives out list of lines as strings
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

## Writing file ##

# f = open('file.txt', 'w')
# f.write('I am writing on the file\n')
# f.write('I am writing second line\n')
# f.writelines(['This is the third line\n', 'Fourth line'])
# f.close()

# r = open('file.txt', 'r')
# print(r.read())
# r.close()

### Context manager

# with open('file.txt', 'r') as f:
#     print(f.read())


# f = open('file.txt', 'a')
# f.write('Fifth line')
# f.close()

# with open('file2.txt', 'x') as f:
#     f.write('\nFifth line')


# Modes
"""
r, w, a, x
rb, wb, ab  # binary modes
r+, w+, a+  # read and write mode
rb+, wb+, ab+

"""

# f = open('file.txt', 'w+')
# f.write('I am writing on the file\n')
# f.write('I am writing second line\n')
# f.writelines(['This is the third line\n', 'Fourth line'])
# f.seek(0)
# print(f.read())

"""
r - read, require file, resets the cursor to the top
w - write, if file does not exist, create a new file. If file exist, delete the content and start writing from the start
a - append, if file does not exist, create a new file. If file exist, start writing from the cursor's position
x - exclusive creation, if file does not exist, create a file and start writing from the start. 
    If file exists fail with error
"""
