## Iterators ##

# print(''.join(['a', 'b', 'c']))

# print(list('abc'))


# def custom_join(l, join=''):
#     s = ''
#     for i in l:
#         s += i + join
#
#     return s
#
#
# print(custom_join(['a', 'b', 'c'], ''))


## Iteration protocol

# __iter__(), __next__


# l = ['a', 'b', 'c']
#
# my_iterator = iter(l)
#
# print(my_iterator.__next__())
# print(my_iterator.__next__())
# print(my_iterator.__next__())
# print(my_iterator.__next__())


## For loop

# for i in l:
#     print(i)

#
# iterable = [1,2,3]
# iter_obj = iter(iterable)
#
# while True:
#     try:
#         i = iter_obj.__next__()
#         print(i)
#     except StopIteration:
#         break


## custom interator

n = 5
# 2**1, 2**2, 2**3,.. 2**5

class PowerOfTwo:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.m = 0
        return self

    def __next__(self):
        if self.m <= self.n:
            result = 2 ** self.m
            self.m += 1
            return result
        else:
            raise StopIteration


p = PowerOfTwo(5)
i = iter(p)

# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())


# for a in i:
#     print(a)



### Generator ##

n = 5
# [0, 1, 2, 3, 4]


# def firstn(n):
#     m, l = 0, []
#     while m < n:
#         l.append(m)
#         m += 1
#
#     return l
#
# print(firstn(5))


# def func():
#     yield 'abc'
#     print('func')
#
# a = func()
# print(next(a))
# print(next(a))


def firstg(n):
    m = 0
    while m < n:
        yield m
        m += 1

# for i in firstg(5):
#     print(i)

f = firstg(5)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

# print(f)

### Generator Expression

# print([x for x in range(5)])

g = (x for x in range(5))
# print(g)
#
# for i in g:
#     print(i)


def power_of_two(n):
    m = 0
    while m <= n:
        yield 2 ** m
        m += 1


p = power_of_two(5)
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))

for i in p:
    print(i)


##

# def func():
#     res = []
#     for x in ...:
#         res.append(x)
#     return res
#
#
# def gen_func():
#     for x in ...:
#         yield x
