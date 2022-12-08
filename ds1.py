## Immutable ##


## strings ##
import string

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

# print(s[5:0:-1])
# print(s[::-1])  # Reversing a string
# print(s[::-2])


s = 'Hello World abc'
# print(s.find('e'))
#
# print(len(s))
#
# print(s.index('l'))
#
# print(s.count('l'))

# print(s.upper())
# print(s.lower())
#
# print(s.startswith('Hello'))
# print(s.endswith('dld'))

# print(s.split('o'))


## String formatting ##

# name = input('Please give me your name: ')
# print('Hello %s' % name)

a, b, c = 'Adhish', 'Ram', 'Laxman'
d = 'a'

# print('Hello %s, %s & %s %d' % (a, b, c, d))
#
# print('Hello {}, {} and {} {}'.format(a, b, c, d))

# print(f'Hello {a}, {b} and {c} {d}')


## Tuples ##

# t = ()
# t = (1, 2, 3)
# # mixed datatypes
# t = (1, 'Hello', 2.3, (4, 5, 6))  # Immutable ordered sequence of elements
#
# print(type(t))
# print(t)
#
# m = 1, 2  # tuple packing
#
# print(type(m))
#
# a, b, c = 1, 2, 3  # tuple unpacking
# print(a, b, c)
#
# x = 1, 2, (3, 4)  # tuple packing
# print(type(x))
# k, l, m = x  # tuple unpacking
# n, o = m  # (3, 4)
# # print(k, l, m)
# print(n, o)


## Indexing ##

a = ('apple', (5, 9, (6,)), (1, 2, 3))

# print(len(a))
# a was out tuple, so we used index to extract the element
# the element was also a tuple, so we can use the same method to extract the element again using index
# print(a[1][1])

# print(a[2][0])

# print(a[1][2][0])


## Slicing ##

a = ('apple', (5, 9, (6,)), (1, 2, 3))

# print(a[::-1])
#
# print(a[1][::-1])
#
# b = a[0], a[1][::-1], a[2]
# print(b)

# print(a[-1], -2)
# print(a[2][0:2])
# print(a[-1][0:2])


### Updating tuples ###

# a = ('apple', (5, 9, (6,)), (1, 2, 3))
# b = 'Hello',
#
# print(id(a))  # where a is stored
# print(id(b))  # where b is stored
#
# a += b  # c = a + b
# print(id(a))  # where a is stored again
# print(a)


## Delete tuple ##

# a = ('apple', (5, 9, (6,)), (1, 2, 3))
# del a
# print(a)


## Tuple functions ##
a = ('apple', (5, 9, (6,)), (1, 2, 3, 3))
# print(a[-1].count(3))
# print(a.index(1))

## len, max, min

# print(max(a[2]))
# print(min(a[2]))
# print(sum(a[2]))
# print(type(sorted(a[2])))
# print(sorted(a[2]))


## loop on a tuple

a = ('apple', (5, 9, (6,)), (1, 2, 3, 3))
# for i in a:
#     print(i)

## membership operator

print('a' in 'Hello World')
print('apple' in a)

print('a' not in 'Hello World')
print('apple' not in a)
