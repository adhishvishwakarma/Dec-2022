## Object oriented programming ##

# def func():
#     pass
#
# print(type(func))
#
#
# import sys
#
# print(type(sys))
#
# print(type(1))
# print(type(1.2))
# print(type('Hello'))
# print(type([]))
# print(type({}))
# print(type((1,)))
# print(type(func))
# print(type(object))
# print(type(type))

# def func_some():
#     print('Something')
#
#
# class First:
#     pass
#
#
# f = First()  # Instantiation
# m = First()
# n = First()
#
# print(f)
# print(m)
# print(n)
# print(type(f))
# print(type(First))


# Class/Object Initialization

# class Second:
#     # Init is used to initialize the class
#     def __init__(self, a, b):  # magic methods/ dunder methods in python objects/classes
#         self.a = a
#         self.b = b
#         self.int_variable = 'Class Varible'
#         print('Class is initialized')
#
#     def add(self):
#         print(self.a, self.b)
#         return self.a + self.b + self.c
#
#     def subtract(self):
#         return self.a - self.b
#
#
# s = Second(1, 2)
# d = Second(1, 2)
# # print(s.add())
# # print(s.subtract())
# print(s.int_variable)
# s.name = 'Adhish'  # Dynamic attribute
# s.c = 3
#
# print(s.add())


# Class attributes

class Cat:
    species = 'Mammal'

    def __new__(cls, *args, **kwargs):  # constructor
        pass

    def __init__(self, name, age):
        self.name = name
        self.age = age

c = Cat('Cat', 23)
print(c.species)

