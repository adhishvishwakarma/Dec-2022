## List ##
# Mutable ordered sequence of elements

l = []
l = ['Hello', 1, (2, 3, 4), [5, 6, 7]]  # mixed datatype

# print(l[3][0])  # Accessing elements
#
# print(l[1:3])  # Slicing


l = ['Hello', 1, (2, 3, 4), [5, 6, 7]]

# print(id(l))
# l[0] = 'World'
# print(id(l))
# print(l)
#
# del l[0]
# print(l)
# print(id(l))

# l[2][0] = 8  # tuple cannot be updated even if it is inside a list
# print(l)

t = ('apple', (5, 9, (6,)), [1, 2, 3])

# t[2][0] = 9
# print(t)  # list can be updated even if it is inside a tuple

## List functions ##

# l = [1, 2, 3, 4]
# l.append(5)  # appends at the end of list
# print(l)
# l.insert(1, 'Hello')  # inserts at the index with a value
# # insert(index, value)
# print(l)

l = [1, 2, 3, 4, 1]
# l.remove(1)  # Removes the first occurence of the element
# print(l)
# a = l.pop()  # Deletes the last value of the list
# print(l, a)

# a = l.pop(2)  # Deletes the index value which is passed
# print(l, a)
#
# l.count()
# l.index()

l1 = [1, 2, 3]
l2 = [4, 5, 6]
# l1.extend(l2)
# print(l1, '\n', l2)


# print(l1 + l2)
# print(l1)
# print(l2)
# l1.extend(l2)
# print(l1)
# print(sorted(l))
# print(list(reversed(l)))  # Iterator
# l.reverse()
# print(l)
# print(l[::-1])

# print('Hello' * 3)
# print(['Hello'] * 3)
# ['Hello'] + ['Hello'] + ['Hello']
# ['Hello', 'Hello', 'Hello']
# ['Hello'], ['Hello'], ['Hello']

# s = 'Hello World abc'
# l = s.split(' ')
# print(l)
#
# s = ' '.join(l)
# print(s)

### List comprehension ###

# l = [1, 2, 3, 4, 5]
# r = []  #
# for i in range(1, 10):
#     if i % 2 != 0:
#         r.append(i ** 2)  #
# print(r)
#
# r = [i**2 for i in range(1, 10, 2)]
# print(r)
#
# r = [i ** 2 for i in range(1, 10) if i % 2 != 0]
# print(r)
#
# print([i for i in 'Hello'])
#
# l = []
# for i in 'Hello':
#     l.append(i)
#
# # ['H', 'e', 'l', 'l', 'o']

# # create a new list
# # extract elements from an iterable using loop
# # perform operation on the element
# # append that element to the new list
#
# r = []  #
# for i in range(1, 10):
#         r.append(i ** 2)  #
# print(r)
#
# r = [i ** 2 for i in range(1, 10) if i%2 != 0]
# print(r)
#
# ## [<operation> <loop> <condition>]
#
# # ['Odd', 'Even', 'Odd' ...]

s = 'Lorem ipsum Hello World'
# Create a string with all the space separated strings as revered
o = 'meroL muspi olleH dlroW'
