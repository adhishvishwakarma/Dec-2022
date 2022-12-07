## Immutable ##


## strings ##

s = 'a'
d = "abc"
c = '''this is also a# string'''
v = """We can use double quotes too"""

# print(type(v))

s = """ Hi, My name 
is Adhish
"""

# print(s)
# print(type(s))

s = """ Hi, My name\nis Adhish\n"""

# print(s)
# print(type(s))

## Indexing ##
s = 'Python'

# P   y   t  h   o   n
# 0   1   2  3   4   5
# -6 -5 -4  -3  -2  -1

# print(s[0])
# print(s[-1])
# print(s[3])
# print(s[-6])
# print(s[-2])

# print(s[10])
# print(s[5])

## Slicing ##

s = 'Python'

# print(s[1:])
# print(s[:-1])
# print(s[3:-2])
#
# print(s[:])  # duplicate string
#
# print(s[-3:5])
#
# print(s[0:5:2])

print(s[5:0:-1])
print(s[::-1])  # Reversing a string
print(s[::-2])

