## Functions

#
# for i in range(0, 3):
#     num = int(input('Please enter a number: '))
#     c = 9
#     if num == c:
#         print('Wow! you guessed it!')
#         break
#     else:
#         print('Sorry wrong number')
#
#
#
# for i in range(0, 5):
#     num = int(input('Please enter a number: '))
#     c = 10
#     if num == c:
#         print('Wow! you guessed it!')
#         break
#     else:
#         print('Sorry wrong number')
#
#
# for i in range(0, 2):
#     num = int(input('Please enter a number: '))
#     c = 3
#     if num == c:
#         print('Wow! you guessed it!')
#         break
#     else:
#         print('Sorry wrong number')
#
#
# # DRY - Don't repeat yourself
#
# def guess_number(turns, match_number):
#     """
#     This function allows user to insert number <turns> times and match it with <matched_number>
#     :param turns: requires an integer
#     :param match_number: requires an integer
#     :return: None
#     """
#     for i in range(0, turns):
#         num = int(input('Please enter a number: '))
#         c = match_number
#         if num == c:
#             print('Wow! you guessed it!')
#             break
#         else:
#             print('Sorry wrong number')
#
# guess_number(3, 9)
# guess_number(5, 10)
# guess_number(2, 3)
#



## Syntax
"""
def function_name(parameters/arguments):
    '''docstring'''
    statments
    return expression
"""

#
# def print_hello_world():  # defining the function
#     print('Hello World')
#
#
# print_hello_world()  # Calling the function


# def print_hello_world():
#     print('Hello World')
#
# print_hello_world()


def greet_user(name):
    # print(f'Hello {name}!')
    # print('Hello {}'.format(name))
    print('Hello %s' % name)


# greet_user('Adhish')
# greet_user('Ram')

# name = input('Please enter your name: ')
# greet_user(name)


# def add_numbers(a, b):
#     print(a + b)
#     return None
#
# # l = [1, 2, 3]
# # print(l.pop())
# # print(l)
#
#
# def add_numbers(a, b):
#     return a + b
#
# print(add_numbers(1, 2))
# x = add_numbers(1, 2)
# print(x)
#
# print(greet_user('Adhish'))

#
# def find_positive_or_negative(num):
#     if num >= 0:
#         return 'Positive'
#     else:
#         return 'Negative'
#
#
# x = find_positive_or_negative(-10)
# print(x)


## Arguments ##

# def greet(name, msg):
#     return f'Hello {name}, {msg}!'


# print(greet('Adhish', 'Good morning'))
# print(greet('Good morning', 'Adhish'))
#
# print(greet(name='Adhish', msg='Good morning'))
# print(greet(msg='Good morning', name='Adhish'))


# def greet(name, msg='Good morning'):  # Default arguments
#     return f'Hello {name}, {msg}!'
#
#
# print(greet('Adhish'))  # if the msg is not provided, the default value will be taken
# print(greet('Adhish', 'Good Evening'))  # If the msg is provided, the provided msg will be used and default value will be ignored

# Arbitrary arguments
"""
*args, **kwargs
"""


# def sum(*args):  # 1, 2, 3,4 , 5... 100
#     c = 0
#     print(args)
#     print(type(args))
#     for i in args:
#         c += i
#
#     return c
#
#
# print(sum(1, 2, 3, 4, 5))
# print(sum(1, 2))
# print(sum(1, 2, 3, 4, 5, 10, -20))


# def greet(**kwargs):
#     for k, v in kwargs.items():
#         print(f'{k} {v}')
#
#
# print(greet(name='Adhish', msg='Good morning'))
# print(greet(msg='Good morning', name='Adhish'))


# def func(required_arg, *args, **kwargs):
#     print(required_arg)
#     print(args)
#     print(kwargs)
#
#
# func(1, 2, 3, 4, k=5, m=6)


## Anonymous function

# s = lambda a, b: a + b
#
# def s(a, b):
#     return a + b
#
# print(s(10, 12))

# def func_name(arg1, arg2):
#     return arg1 + arg2
#
# print(func_name(1, 3))
#
# print((lambda arg1, arg2: arg1+arg2)(1, 3))
#


## Find Factorial ##

# 2! = 2 * 1!
# 3! = 3 * 2 * 1
# 3! = 3 * 2!
# 4! = 4 * 3 * 2 * 1
# 4! = 4 * 3!
#
# n! = n * (n-1)!


# def factorial(n):
#     if n == 1:  # exit condition
#         return 1
#     result = n * factorial(n-1)
#     return result


# n = 3
#
# 3 * factorial(2)
# result = 3 * 2
# return 6
#
#     n = 2
#     2 * 1 #factorial(1)
#     result = 2
#     return 2
#
#         n = 1
#         return 1

# print(factorial(3))
#
#
# l = [1, 2, 3, 4, 5]
#
# print([1] + [2, 3, 4, 5])
#
# print([1] + [2] + [3, 4, 5])
#
# print([1] + [2] + [3] + [4, 5])
#
# print([1] + [2] + [3] + [4] + [5])
# print(1 + 2 + 3 + 4 + 5)
# # 15
#
#
# def find_sum(l):
#     if len(list) == 1:
#         return l[0]
#
#     else:
#         return l[0] + find_sum(l[1:])
#
#
# print([1, 2] + [3, 4, 5])
