## List ##
# Mutable ordered sequence of elements
import copy

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
#
# print(['Odd' for i in range(1, 10) if i%2 != 0])
# print(['Odd' if i%2 != 0 else 'Even' for i in range(1, 10)])
#
# s = 'Lorem ipsum Hello World'
# # Create a string with all the space separated strings as revered
# o = 'meroL muspi olleH dlroW'
#
# print(s.split())
# print([i[::-1] for i in s.split()[::-1]])
# print(' '.join([i[::-1] for i in s.split()]))

# a = ['red', 'green', 'blue']    ## id
# b = a
# print(b)
#
# b.append('yellow')
# print(b)
#
# print(a)
# print(id(a))
# print(id(b))
#
#
# c = a[:]  # copy
# print(id(a))
# print(id(c))
# c.append('purple')
# print(c)
# print(a)
#
# d = [i for i in a]  # copy
# print(id(d))
# print(d)
#
# e = list(a)  # copy
# f = copy.deepcopy(a)  # copy


## Dictionary ##

# d = {}
# l = ['a', 'b', 'c']
# print(l[0])
#
# d = {'key': 'value'}
# print(d['key'])
#
# d = {0: 'a', 1: 'b', 2: 'c'}
# print(d[1])
#
# d = dict(key='value')
# print(d)
# d = dict([(1, 2), (3, 4)])
# print(d)

# del d[1]
# print(d)
# del d
# print(d)
#

# l[0] = 'abc'
# d[1] = 5
# print(d)
#
# a = {'a': 1}
# b = {'b': 2}
# a.update(b)
# print(a)
#
# c = a.copy()

# sq = {1:1, 2:4, 3:9, 4:16, 5:25}
# a = sq.pop(5)
# print(sq, a)
# # sq.pop(1)
# # print(sq)
# # sq.popitem()
# # print(sq)
#
# # sq.clear()
# # print(sq)
#
# print(sq[3])
# print(sq.get(3))


# d = {'a': 1, 'b': 2, 'c': 3}
#
# for i in d:
#     print(i, d[i])
#
# for i in d.values():  # [1, 2, 3]
#     print(i)
#
# for i in d.keys():  # ['a', 'b', 'c']
#     print(i)
#
# for i in d.items():  # [('a', 1), ('b', 2), ('c', 3)]
#     print(i)


## Dictionary comprehension ##

# sq = {1:1, 2:4, 3:9, 4:16, 5:25}
#
# sq = {i:i**2 for i in range(1, 6)}
# print(sq)
#
# s = {}
# for i in range(1, 6):
#     s[i] = i ** 2
#     # print(s)
# print(s)

# revert key value pairs of a dict
d = {'a': 1, 'b': 2, 'c': 3}
o = {1: 'a', 2: 'b', 3: 'c'}

# a, b = (1, 2)
#
# for k, v in d.items():  # [('a', 1), ('b', 2), ('c', 3)]
#     print(k, v)
#
# x = {v: k for k, v in d.items()}
# print(x)

# how do I get the key from value

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 2}
# s = 2
# for k, v in d.items():  # [('a', 1), ('b', 2), ('c', 3), ('d', 2)]
#     if s == v:
#         print(k)
#         break
#
#
# for i in d:  # iterating over the keys
#     if d[i] == s:  #d['b']
#         print(i)
#
# print([k for k, v in d.items() if s == v][0])
#
# d = {'a': 1, 'b': 2, 'c': 3, 'a': 2}

# Dictionary keys should be unique
# Dict keys should only be immutable

d = {
    'asdsd': 1,
    1: 2,
    (1, 3): 3
}
print(d)

