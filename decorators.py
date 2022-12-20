## Decorators ##

# assigning functions to variables
# def greet(name):
#     return f'Hello {name}'
#
# g = greet
#
# print(g('Adhish'))
#


# nested functions

# def greet(name):  # defining
#     def get_message():  # defining
#         return 'Hello '
#     result = get_message() + name
#     return result


# print(greet('Adhish'))

# Function can be passed as parameters to other function


# def greet(name):
#     return f'Hello {name}'
#
#
# def call_func(func):
#     return func('World')  # greet('World')
#
# print(call_func(greet))

# Function can also be returned

# def compose_func():
#     def get_message():
#         return 'Hello there!'
#
#     return get_message  # returning the definition, not calling the function
#
# g = compose_func()  # g got assigned with definition of get_message function
# print(g())


## Closure: Inner function have access to the enclosing scope


# def compose_func(name):
#     def get_message():  # definition
#         return f'Hello {name}'
#
#     return get_message
#
#
# g = compose_func('Adhish')
# print(g())


# def compose_func --> store the definition into memory and moves forward
# executing next line i.e. 59, We are executing the compose_func and assigning the return value to g
# Found another function definition, storing it in the memory
# executing next line, i.e. 55, Here we are returning the definition of get_message
#           and destroying the compose_func function.
# Now we have value of g assigned as definition on get_message function
# Executing next line, calling g which is our get_message function
# Get_message function uses 'name' argument from compose_func which is already destroyed
# So even after the outer or enclosing function is destroyed, the inner function still keeps the state in the memory
# or in simple terms remember the arguments/variables and this property is called as CLOSURE


### Decorators are a way to modify the behavior of the function without actually changing the structure


# def make_pretty(func):
#     def inner():
#         print('I got decorated')
#         func()
#     return inner
#
#
# @make_pretty
# def ordinary():
#     print('I am ordinary')
#
# # ordinary()
#
# # pretty = make_pretty(ordinary)  # holds the defintion on inner
# # print(pretty())
#
# # ordinary = make_pretty(ordinary)
# # ordinary()
#
# ordinary()

#
# def smart_divide(func):
#     def inner(a, b):
#         print(f'I am trying to divide {a} by {b}')
#         if b == 0:
#             print("Can't divide")
#             return
#         return func(a, b)
#     return inner
#
#
# @smart_divide
# def divide(a, b):
#     return a/b
#
# # divide = smart_divide(divide)
#
# print(divide(2, 1))  # calling inner function with variables
#
# import datetime
# import time

#
# def timit(func):
#     def inner():
#         start_time = datetime.datetime.now()
#         func()
#         end_time = datetime.datetime.now()
#         print('Time taken', end_time - start_time)
#     return inner
#
#
# @timit
# def any_func():
#     time.sleep(3)
#     print('completed')
#
# any_func()


## Chaining of decorator

def star(func):
    def inner():
        print('*'*30)
        func()
        print('*'*30)
    return inner


def hash(func):
    def inner():
        print('#'*30)
        func()
        print('#'*30)
    return inner

@star
@hash
def some_func():
    print('I am the function')

some_func()

some_func = star(hash(some_func))
