Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 01:25:11) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> graf = open('/Users/james/Documents/moose.txt')
>>> f.readlines()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    f.readlines()
NameError: name 'f' is not defined
>>> graf.readlines
<built-in method readlines of _io.TextIOWrapper object at 0x102f65bb0>
>>> graf.readline
<built-in method readline of _io.TextIOWrapper object at 0x102f65bb0>
>>> graf2=open('/Users/james/Documents/moose2.txt')
>>> graf2.readlines
<built-in method readlines of _io.TextIOWrapper object at 0x102f65c90>
>>> graf2
<_io.TextIOWrapper name='/Users/james/Documents/moose2.txt' mode='r' encoding='US-ASCII'>
>>> test=graf.read()
>>> test
'      \\     \\ /            \\/    ___//\n    \\_ /    //             \\]   //~~~\n      \\\\    ]]            //   //\n     \\__\\ _]_\\_          _\\\\ __/\\//\n         __ _____\\        /_\\//  _\n     __ _/     \\/~~~~~~\\/ \\__ //\n      _/       [        ]    \\/\n              /[  /  \\  ]\n             /  [(0  0)]\n            /   [      ]\n  _________~   [        ]\n               \\ <    > /\n              / \\______/\n              ]     (_)\n             ] \n'
>>> test.readline
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    test.readline
AttributeError: 'str' object has no attribute 'readline'
>>> graf.readlines()
[]
>>> 
>>> graf.readline()
''
>>> ''
''
>>> 
>>> 
>>> 
>>> 
>>> 
>>> graf.readlines()
[]
>>> 
>>> for line in graf:
	print line,
	
SyntaxError: invalid syntax
>>> for x in graf:
	print x
	
SyntaxError: invalid syntax
>>> for line in graf:
	print(line)

	
>>> 
>>> 
>>> graf
<_io.TextIOWrapper name='/Users/james/Documents/moose.txt' mode='r' encoding='US-ASCII'>
>>> graf2
<_io.TextIOWrapper name='/Users/james/Documents/moose2.txt' mode='r' encoding='US-ASCII'>
>>> for line in graf2:
	print(line)

	
      \     \ /            \/    ___//\n

    \_ /    //             \]   //~~~\n

      \\    ]]            //   //\n

     \__\ _]_\_          _\\ __/\//\n

         __ _____\        /_\//  _\n

     __ _/     \/~~~~~~\/ \__ //\n

      _/       [        ]    \/\n

              /[  /  \  ]\n

             /  [(0  0)]\n

            /   [      ]\n

  _________~   [        ]\n

               \ <    > /\n

              / \______/\n

              ]     (_)\n

             ] \n

>>> for line in graf:
	print(line)

	
>>> 
>>> 
>>> 
>>> 
>>> y = input()
blech
>>> y
'blech'
>>> print "Enter your guess.", input()
SyntaxError: invalid syntax
>>> y = input ("Enter your name: ")
Enter your name: 
>>> y = input ("Enter your guess: ")
Enter your guess: r
>>> y
'r'
>>> word_list=['computer', 'memory', 'disk space', 'monitor', 'video card']
>>> import random
>>> chosen_puzzle = random.shuffle(word_list)
>>> chosen_puzzle
>>> chosen_puzzle = (word_list).shuffle
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    chosen_puzzle = (word_list).shuffle
AttributeError: 'list' object has no attribute 'shuffle'
>>> word_list
['disk space', 'monitor', 'video card', 'memory', 'computer']
>>> chosen_puzzle
>>> print(chosen_puzzle)
None
>>> from random import shuffle
>>> shuffle(world_list)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    shuffle(world_list)
NameError: name 'world_list' is not defined
>>> shuffle(word_list)
>>> for x in word_list:
	shuffle(x)

	
Traceback (most recent call last):
  File "<pyshell#63>", line 2, in <module>
    shuffle(x)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/random.py", line 265, in shuffle
    x[i], x[j] = x[j], x[i]
TypeError: 'str' object does not support item assignment
>>> import random
>>> chosen_puzzle = (random.randint(0,list_count))
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    chosen_puzzle = (random.randint(0,list_count))
NameError: name 'list_count' is not defined
>>> list_count=len(world_list)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    list_count=len(world_list)
NameError: name 'world_list' is not defined
>>> list_count=len(word_list)
>>> chosen_puzzle = (random.randint(0,list_count))
>>> for i in word_list:
	if i!= '':
		print("_",end="")
		else:
			
SyntaxError: invalid syntax
>>>  for i in word_list:
	if i!= '':
		print("_",end="")
		
SyntaxError: unexpected indent
>>> for i in word_list:
	if i != '':
		print("_",end="")
		else:
			
SyntaxError: invalid syntax
>>> for i in word_list:
	if i != '':
		print("_",end="")
		else:
			
SyntaxError: invalid syntax
>>> for i in word_list:
	if i != '':
		print("_",end="")
		else
		
SyntaxError: invalid syntax
>>> for i in word_list:
	if i != '':
		print("_ ",end="")
		else:
			
SyntaxError: invalid syntax
>>> for i in chosen_puzzle:
	if i != '':
		print(_ ),end="")
		
SyntaxError: invalid syntax
>>> for i in chosen_puzzle:
	if i != '':
		print("_ ",end="")
		else:
			
SyntaxError: invalid syntax
>>> print(chosen_puzzle)
5
>>> str = (word_list[chosen_puzzle])
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    str = (word_list[chosen_puzzle])
IndexError: list index out of range
>>> word_list
['video card', 'computer', 'monitor', 'disk space', 'memory']
>>> list_count
5
>>> chosen_puzzle = (random.randint(0,list_count))
>>> chosen_puzzle
3
>>> str = (word_list[chosen_puzzle])
>>> str
'disk space'
>>> for i in chosen_puzzle:
	if i != '':
		print("_ ",end="")
		else:
			
SyntaxError: invalid syntax
>>> 
>>> for i in str:
	if i != '':
		print("_ ",end="")
		else:
			
SyntaxError: invalid syntax
>>> for i in str:
	if i != '':
		print("_ ", end="")
		else:
			
SyntaxError: invalid syntax
>>> for i in str:
     if i != ' ':
          print( "_ ", end="")
     else:
          print ("  ", end="")

          
_ _ _ _   _ _ _ _ _ 
>>> userguess = input("Enter your guess: ")
Enter your guess: b
>>> 

>>> 
>>> for y in str:
     if y != ' ':
          print( "_ ", end="")
     else if  y = userguess:
	     print(userguess)

     else:
          print ("  ", end="")

SyntaxError: invalid syntax
>>> for y in str:
     if y != ' ':
          print( "_ ", end="")
     else if  y == userguess:
	     print(userguess)

     else:
          print ("  ", end="")
          
SyntaxError: invalid syntax
>>> for y in str:
     if y != ' ':
          print( "_ ", end="")
     else if  y == 'userguess'
	     print(userguess)

     else:
          print ("  ", end="")
          
SyntaxError: invalid syntax
>>> for y in str:
     if y != ' ':
          print( "_ ", end="")
     elif  y == userguess
	     print(userguess)

     else:
          print ("  ", end="")
          
SyntaxError: invalid syntax
>>> 
>>> for y in str:
    if y != ' ':
         print( "_ ", end="")
    elif  y == userguess:
	     print(userguess)

    else:
         print ("  ", end="")

         
_ _ _ _   _ _ _ _ _ 
>>> userguess = input("Enter your guess: ")
Enter your guess: d
>>> for y in str:
    if y != ' ':
         print( "_ ", end="")
    elif  y == userguess:
	     print(userguess)

    else:
         print ("  ", end="")

         
_ _ _ _   _ _ _ _ _ 
>>> 
for y in str:
	if  y == userguess:
	     print(userguess)
    elif y != ' ':
         print( "_ ", end="")

    else:
         print ("  ", end="")
         
SyntaxError: unindent does not match any outer indentation level
>>> for y in str:
	if  y == userguess:
	     print(userguess)
	elif y != ' ':
         print( "_ ", end="")

	else:
         print ("  ", end="")

         
d
_ _ _   _ _ _ _ _ 
>>> for y in str:
	if  y == userguess:
	     print(userguess),
	elif y != ' ':
         print( "_ ", end="")

	else:
         print ("  ", end="")

         
d
(None,)
_ _ _   _ _ _ _ _ 
>>> for y in str:
	if  y == userguess:
	     print(userguess,)
	elif y != ' ':
         print( "_ ", end="")

	else:
         print ("  ", end="")

         
d
_ _ _   _ _ _ _ _ 
>>> 
