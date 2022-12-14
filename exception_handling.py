## Exception handling ##

"""SyntaxError
TypeError
NameError
IndexError
KeyError
IndentationError
ValueError
ZeroDivisionError
"""

# try:
#     print(a)
# except NameError:
#     print('Name Error occured')
#


"""
try:
    # do something
    
except Exception as e:
    # do something else
"""



# try:
#     x = int(input('Please enter a number: '))
#     y = int(input('Please enter a number: '))
#     a = x/y
#     # print(b)
#     print("Output of the division is", a)
# except (ZeroDivisionError, NameError):
#     print('Dividing by zero is not allowed and you need to define variables')
# except Exception as e:
#     print(e)
#     print('Executing the exception block')


l = ['a', 0, 2, 4]

# for i in l:
#     try:
#         x = 1/int(i)
#         print('The reciprocal of {} is {}'.format(i, x))
#     except Exception as e:
#         print('Exception occured: {} , cannot produce reciprocal of {}'.format(e, i))



# try:
#     a = 10/1
#     print(a)
# except Exception as e:
#     print('Zero division Error')
# else:
#     print('Program completed')


# to Raise Exception

#raise

# raise MemoryError('This is an error')

# try:
#     a = int(input('Pleas enter a number: '))
#     if a <= 0:
#         raise ValueError('Please enter positive number')
#
# except ValueError as e:
#     print(e)

## Finally block

# try:
#     a = 10/1
#     print(a)
# except Exception as e:
#     print('Zero division Error')
# else:
#     print('Program completed successfully')
# finally:
#     print('This would be executed irrespective of error')
#     # Close the file or connection
#
