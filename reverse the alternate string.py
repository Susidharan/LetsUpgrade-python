#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dhara
#
# Created:     02-06-2023
# Copyright:   (c) dhara 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

s = 'WAP to reverse the alternate words in the string'
words = s.split()
i = 0

for word in words:
    if i % 2 == 1:
        print(word[::-1], end=' ')
    else:
        print(word, end=' ')
    i += 1

