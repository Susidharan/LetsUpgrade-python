#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dhara
#
# Created:     05-06-2023
# Copyright:   (c) dhara 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
## Revising List Methods

#1.len()
a = [1,2,3,4,5,6,7,8,6,8,4,2,]
print(len(a))

#2.count()
print(a.count(6))

#3.index()
print(a.index(6))

#4.append()
print(a.append(6))
print(a)

#5.insert()
print(a.insert(3, 12))
print(a)

#6.extend()
b = [2,4,5,6,7,3,4,2,1]
print(a + b)

#7.remove()
print(a.remove(1))
print(a)