#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dhara
#
# Created:     04-06-2023
# Copyright:   (c) dhara 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------



##using translate function
original_string = '''+98895001  +29423929聽 +99012500聽 +977925588聽(    +972461111聽('''
characters_to_remove = "聽("

translation_table = str.maketrans('', '', characters_to_remove)
modified_string = original_string.translate(translation_table)

print(modified_string)


##using split function
s='''+98895001  +29423929聽 +99012500聽 +977925588聽(    +972461111聽('''
words= s.split()
for word in words:
    a=word.strip('聽(')
    print(a[::1], end=" ")

