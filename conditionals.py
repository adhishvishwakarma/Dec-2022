#
# if <condition == True> :
#     <Something to happen here>

# n = 4
# if n > 2:
#     print('The number is greater than 2.')
# elif n == 2:
#     print('The number is equal to 2')
# elif n == 3:
#     print('The number is equal to 3')
# else:
#     print('The number is smaller than 2')


# num = int(input('Please enter a number: '))
# if num % 2 == 0:
#     print('The number is even.')
# else:
#     print('The number is odd')


# range(begin, end, step)
# range(0, 11) = 0,1,2,3,4,5,6,7,8,9,10
# range(0,5) = 0,1,2,3,4
# range(0,10) = 0,2,4,6,8


#### Loops ####

# For loop

# for <variable> in <sequence/iterator>:
#     <condition>

# for i in range(5, 2, -1):  # 2 4
#     print(i)


# for i in range(0, 11):
#     if i == 7:
#         print(i**2)



# While loop

# while <condition == True> :
#     <Execute statements>

# c = 0
# while 2 == 2:  # true
#     if c < 1:  #true   False
#         print('The number is equal to 2')
#     c = 1
#     break

# c = 0
# while c < 11:   # c = 10
#     c += 1    # c = 11  # c = c+1
#     print(c)  # 11
#
#
# c = 0
# while c < 11:   # c = 10
#     print(c)  # 10
#     c += 1  # c = 11  # c = c+1


# 0,1,2,4
for i in range(0,5):
    if i == 3:
        pass
    print(i)

# break, continue, pass
