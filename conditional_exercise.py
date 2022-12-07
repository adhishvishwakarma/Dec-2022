#### Print #  ######

"""
#
##
###
####
#####
######
#######
"""

# for i in range(1, 8):
#     print('#' * i)



#### Guess the number ####
# Give user 3 tries to guess the number

# for i in range(0, 3): #0,1,2
#     num = int(input('Please enter a number: '))
#     c = 9
#     if num == c:
#         print('Wow! you guessed it!')
#         break
#     else:
#         print('Sorry wrong number')


# a = 0
# while a < 3:
#     num = int(input('Please enter a number: '))
#     c = 9
#     if num == c:
#         print('Wow! you guessed it!')
#         break
#     else:
#         print('Sorry wrong number')
#     a += 1



#### Famous Fizz Buzz problem ####

# Between number 1 to 100
# divisible by 3 -- print Fizz
# divisible by 5 -- print Buzz
# divible by 3 and 5 -- print FizzBuzz
# and rest of the time print the integer

for i in range(1, 101):
    if i%3==0 and i%5==0:  # if i%15==0
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)





### Leap Year ####

# Should be divisible by 4 but not by 100
# but if it is divisible by 100 and also 400 then it is a leap year





