#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dhara
#
# Created:     29-05-2023
# Copyright:   (c) dhara 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
## reverse the string


n="Susidharan"
i= len(n) - 1

while i>=0:
    print(n[i], end = '' )
    i -= 1

##find the occurence of the substring

s= "i have to get job within this year"
print(s.find('ar'))

##display position of all occurences

a='''i have to practice more to familiar with python'''
subs='th'
n = len(a)
pos = -1

while 1:
    pos = a.find(subs, pos + 1, n)

    if pos == -1:
        print ('Substing not found')
        break

    print(f'Substring found at : {pos}')