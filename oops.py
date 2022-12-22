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

# class Cat:
#     species = 'Mammal'
#
#     def __new__(cls, *args, **kwargs):  # constructor
#         pass
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# c = Cat('Cat', 23)
# print(c.species)
#

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Coordinate: ({self.x}, {self.y})'

    def distance(self, other):
        # ((x2-x1)**2 + (y2-y1)**2)**1/2
        d = ((self.x - other.x)**2 + (self.y - other.y)**2) ** 1/2
        return d
#
# c1 = Coordinate(3, 4)
# c2 = Coordinate(1, 2)
#
# print(c1.distance(c2))  # self = c1 and other = c2
# print(c2.distance(c1))  # self = c2 and other = c1
#
# print(c1.distance(c1))


# Inheritance

class Animal:  # Base class
    def __init__(self):
        print('Animal')

    def can_live_on_land(self):
        print('yes')

    def can_speak(self):
        print('yes')


# can_speaklass Monkey:
#     def __init__(self):
#         print('monkey')
#
#     def can_speak(self):
#         print("can speak monkey")
#
#     def has_legs(self):
#         print("four legs")

#
# class Human(Monkey, Animal):
#     h = 'Human'
#     def __init__(self):
#         print('human')
#         # self.a = a
#         # self.__b = b  # Private variable
#
#     def has_legs(self):
#         print('two legs')
#
#     def can_speak(self):
#         print('voice')
#
# a = Animal()
# m = Monkey()
# h = Human()
#
# # m.can_live_on_land()
# # m.has_legs()
# # m.can_speak()
#
# h.can_speak()
# # h.can_live_on_land()

"""
Single Inheritance
Multi level inheritance
hierarchical inheritance
multiple inheritance

"""

## Polymorphism
# many forms

# Encapsulation
# public and private variables

# Abstraction
