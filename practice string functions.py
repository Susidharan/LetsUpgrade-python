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

##reverse the string

a = ' try some string functions  '
i = len(a)-1
#while i>=0 :
   # print(a[i], end='')
   # i-=1

    ##using strip
#print(a.strip('t'))

##reverse wordes of the string

l = 'reverse words of this string'
words = l.split()
# print(words[ : : -1])

##using replace function
e = 'using replace function'
# print(e.replace('function' , 'command'))

## using remove function
h = 'using remove function'
print(h.remove('using'))
