# Please write the code to find if a character exists in a string else print 'No'

# s = 'Hello World'
# c = 'a'
#
# x = False  # a does not exist
# for i in s:
#     if c == i:
#         print('Yes')
#         x = True  # found a so making the flag as True
#         break
# # print('No')
# if x == False:
#     print('No')  # print only if a does not exist

#
# k = 0
# while k < len(s):
#     if s[k] == c:   #s[0] == 'H'
#         print('Yes')
#         break
#     k += 1
# print('No')


## Find the length of a string which excludes space

# s = 'Hello World'
# # print(len(s))
# c, d = 0, 1  # c is for increasing index and d is for counting
# while c <= len(s):
#     if s[c] == ' ':
#         c += 1  # c = 6
#         continue
#     d += 1  # 11
#     c += 1  # 11
#
# print(d)
#
# s = 'Hello World a'
# c = 0
# for i in s:
#     if i == ' ':
#         continue
#     c += 1
# print(c)
