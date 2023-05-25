Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> N='Susidharan'
>>> N[2:7]
'sidha'
>>> N[1;10]
SyntaxError: invalid syntax
>>> N[1:10]
'usidharan'
>>> N[0:10]
'Susidharan'
>>> 
>>> N[-10:0]
''
>>> N[-5:2]
''
>>> N='Susidharan'
>>> N[-10:1]
'S'
>>> N[-1:0]
''
>>> N[-1:3]
''
>>> N[-1:-5]
''
>>> N='Susidharan'
>>> N[-5:-1]
'hara'
>>> N[2:-1:10]
's'
>>> N[-2:-1:1]
'a'
>>> N[-4:-500:-1]
'ahdisuS'
>>> 