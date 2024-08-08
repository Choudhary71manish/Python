""" output """
# print ('hello','hii',143)  



""" introducation"""

# It is used for:
# web development (server-side),
# software development,
# mathematics,
# system scripting.

""" python varsion """

# import sys
# print (sys.version)            


#4 python syntax

# if 5>2 :
#     print ('its ture 5>2')
    
    
#4.1

# if 5>2:
#     print ("5>2 ture")     # indeend is importent
# if 5>2 :
#     print ("5>2 ture")     


""" comment way """

#single line
""" multiple 
line 
comment"""


'''  multi
line
comments

'''



""" variable  and type """

# x = 4                     # type is int 
# y = " hello manish"       # tpye is str

# print( type(x))
# print( type(y))



""" casting """
# x = str(3)    # x will be '3'
# y = float(3)   # y wil be 3.0



""" variable name """
#  #legal 
# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"
# #illegal
# 2myvar = "John"
# my-var = "John"
# my var = "John"

""" multi word variable names"""
# myVariableName  = "john"  # camel case use
# MyVariableName  = "pascal case" # pascal case
# my_variable_name = "snake case" # snake case

""" many values to multiple variables"""
# x ,t, y ,z = "apple","banana", "cherry",4
# print (x)
# print (y)

""" one value to multiple variables"""
# x = t = y = a = "apple"
# print(x) 
# print(y)

""" unpack collection""" #imp
# fruits = [ "apple", "banana","cherry"] 
# x, y, z = fruits 
# print(x)
# print(y)
# print(z)

""" output variables """
# x = "py"
# y = "is"
# z = "awesome"
# print(x,y,z)           # py is awesome #someline 
# print(x + y + z)       # pyisawesome   #someline nospace

""" + """
# x = 5
# y = "John"
# print(x, y)

""" + """
# x = 5
# y = "John"
# print(x + y)             # error


""" global variable """
x = "awesome"

def myfunc():
    print("py is" +" " + x)

myfunc()
 
""" ex"""
# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)             #globle

""" ex"""
# x = "awesome"
# def myfunc():
#   global x
#   x = "fantastic"
#   print( "py is " + x) 
# myfunc()
# print( "py is " + x)  

""" data type"""
# text = str 
# number = int , float , complex 
# sequence = list , tuple , range 
# mapping = dict
# set = set , frozenset
# boolean = bool
# binary = bytes, bytearray , memoryview
# none = None 
""" getting the data type type()"""
# x = 45
# x = 20.5
# x = 1j
# x = "string"
# x = range(5)
# x = (10, "small")          #tuple
# x = {"one","two","set"}    #set
# x = {"one": 1, "two":2 }   #dict   key: value
# x = ["one","two","tree"]   #list 
# x = True               
# x = None
# x = frozenset({"a","b","c"})   #frozenset
# x = b"hello"               #bytes
# x = bytearray(2)           #bytearray
# x = memoryview(bytes(5))   #memoryview

# print(type(x))           #type 
# print(x)                  #output


"""example"""
# x = str("Hello World")	
# x = int(20)	
# x = float(20.5)		
# x = complex(1j)	
# x = complex(4p)           #error
# x = list(("apple", "banana", "cherry"))   # typekeyword()		
# x = tuple(("apple", "banana", "cherry"))
# x = range(6)	
# x = dict(name="John", age=36)	
# x = set(("apple", "banana", "cherry"))	
# x = frozenset(("apple", "banana", "cherry"))	
# x = bool(5)		
# x = bytes(5)		 # b'\x00\x00\x00\x00\x00'
# x = bytearray(5)		
# x = memoryview(bytes(5))

# print(type(x))           
# print(x) 


"""type conversion """
# x = 1 #int
# x = float(x)
# print(type(x))            
# print(x)          #1.0

# x = 2.99
# x = int(x)
# print(type(x))            
# print(x)          #2

# x = 2.99
# x = complex(x)
# print(type(x))            
# print(x)          #(2.99+0j)

""" type casting"""
# int, float, complex,.. --> str

""" struing"""
# print("hello")
# print('print')   #both are some

# print("it's alright")
# print('he is called "manish"')
# print("""hello 
#       this 3rd type 
#       of output""")

# print('''this
#       is 
#       a 
#       typy''')

""" string are arrays"""
# a = "hello world"
# print(a[3])

""" looping through a string"""
# y = "hello my name is "
# for x in y :
#     print(x)

"""string length"""
# a = "h a"
# print(len(a))        #3

""" check string """         # imp
# txt = "hello manish"
# print("hello" in txt)     #True
 
""" use in if """    #imp
# txt = "abcd efghijk"
# if "cd" in txt:
#     print ("yes , present cd")
 
"""check if not"""              #imp
# txt ="abcdefghijklmnopqrstuvwx yz"
# print("yza" not in txt)        #True

# x = "abcd fghj" 
# if "ab" not in x:
#     print(" abcd not present")    # ab is present but condition is flase

""" slicing strings"""           #imp #You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
 
""" indexing"""
# a = "hello my name is manish"
# print(a[5:])    #my name is manish  # a[start : end] if you can make empty
# print(a[:])     #hello my name is manish
# print(a[:5])    #hello

"""negative indexing"""
# a = "hello my name is manish"
# print(a[-5:])     #anish
# print(a[-5:-2])   #ani
# print(a[:-4])     #hello my name is ma

""" modify strings"""
"""upper() case"""       
# a = "hello manish"
# print(a.upper())    #upper
# print(a.lower())    #lower

""" strip() remove whitespace"""            #imp
# a = " the king "
# print (a.strip())  #the king

""" replace() string"""
# a = "hello, manish"
# print(a.replace("ello","ii"))
# print(a.replace(" ","ii"))

""" split string """
# a = " hello , world"
# b =  print(a.split(",")) # [' hello ', ' world']

""" string conceatenation"""
# a = "Hello"
# b = "World"
# c = a + b
# print(c)
# print( a + ' ' + b)

""" format string"""
# age = '36'
# txt = "My name is John, I am " + age
# print(txt)

""" f-string"""         #imp
# age = '36'
# txt = f"my age is {age}      #Python 3.6
# print(txt)
"""ex"""
# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

""" escape characters"""
# \' single quote
# txt = 'It\'s alright.'
# print(txt)               # It's alright.

# \\ backslash
# txt = "Hello \bWorld!" 
# print(txt)              #helloWorld

# \n new line
# txt = "Hello\nWorld!"
# print(txt) 

# \r carriage return
# txt = "Hello\rWorld!"
# print(txt)               #World
                        
# \t tab
# \f form feed

# \ooo octal value
# txt = "\110\145\154\154\157"
# print(txt)                           #Hello

# \xhh hex value
# txt = "\x48\x65\x6c\x6c\x6f"
# print(txt) 

""" ex"""
# txt = " hello "manish" choudhary"
# print(txt)                         #incalid syntax

# txt = " hello \"manish\" choudhary"
# print(txt)                            #hello "manish" choudhary

""" string mathods"""   ##imp
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

""" python booleans"""
# true and false

# print(3>2)        #True
# print(2==3)       #False
# print(4<9)        #True

"""ex"""
# print(bool("hello"))    #True
# print(bool(20))         #True   except 0 is false
""" value True"""
# bool("abc")
# bool(123)
# bool(["apple", "cherry", "banana"])

"""same value false"""
# bool(False)
# bool(None)
# bool(0)
# bool(())
# bool({})
# bool([])

""" datatype """
# x = 200
# print(isinstance( x, int))


""" python oprators"""
''' arithmetic + - / * % ** // #the floor division // rounds the result down to the nearest whole number '''
''' assignment = -= += /= %= *= **= //=   >>= <<= :=(=) &=(AND)|=(or) ^=(XOR)'''
''' comparison  == !=(not) > < <= >=   #True /False '''
''' logical     and ,or ,not             # True/fale '''
''' identify  is , is not   #true/False '''
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x
# print(x is not z)       #o/p false
''' membership  in , not in #True /false '''
# x = ["apple", "banana"]
# print("banana" in x)             # op True
''' bitwise &(and), |(or), ^(xor), ~(not),<<(leftshift), >>(rightshift)  '''
# precedence  #print((6 + 3) - (6 + 3)) #op 0
              #print(100 + 5 * 3) #op 115



#highest precedence
""" imp ranking """ 
# # ()  :parentheses
# print((6 + 3) - (6 + 3)) #OP 0
# # **  :exponentiation
# print(100 - 3 ** 3)   #op 73
# # +x, -x ,~x  :unary plus, unary minus, bitwise NOT
# print(100 + ~3)     #op 96
# # *, /, //, % :multiplication , division, floor division, modulus
# print(100 + 5 * 3)   #115
# # +, -        :addition subtraction
# print(100 + 5 * 3)   #115
# # >>, << bitwise left , right
# print(8 >> 4 - 2)      #op 2
# # & : bitwise and
# print(6 & 2 + 1)   #op 2
# # ^ : xor
# print(6 ^ 2 + 1) #op 5
# # | : or 
# print(6 | 2 + 1)  #op 7
# # == , |= , >= ,> ,is ,in, not is, not in, : comparisons,identify,membership operators
# print(5 == 4 + 1)  #op true
# # not : logical
# print(not 5 == 5)  #op false
# and : logical
# print(1 or 2 and 3)  #op 1 ***and, or, is bool value return 
# 2 and 3 : 3 , 2 or 3 :2  #***imp 
# # or : logical




''' list []'''
""" lists [] , list(())"""  # list are ordered, that order are not change
# fruits =[ "apple" ,"banana" ,"cherry" ,"apple"]
# print (fruits)                          #['apple', 'banana', 'cherry' , 'apple']

# list items are ordered , changeable ,allow duplicate values
# list items are index [0] 

""" list length """
# fruits =[ "apple" ,"banana" ,"cherry" ,"apple"]
# print(len(fruits))             #op 4

""" list in datatype """
# list1 = [1,2,3,5]
# list2 = [True , True ,None]
# list3 = ["A", "b",]
# list4 = ["a",34,True,5,6]
# print(type(list4))            #op list

""" list(()) constructor"""
# list5 = list(( "a" , "b"))
# print(list5)                 #op  ['a', 'b']

""" Access items """
# list5 = list(( "a" , "b"))
# print(list5[1])

""" nagative index """
# list5 = list(( "a" , "b" ,3,4,5,6))
# print(list5[-3])            #op 4
# print(list5[-1])        # op 6

""" range of index """
# list5 = list(( 1 , 2 ,3,4,5,6))
# print(list5[2:5])           #op [3, 4, 5]
# print(list5[3:])            #op [4, 5, 6]
# print(list5[:])             #op [1, 2, 3, 4, 5, 6]
# print(list5[:4])            #op [1, 2, 3, 4]

""" nagative indexing """  
""" check if item exists """         #imp2
# list1 = ["a", "b", "c", "d"]
# if "c" in list1:
#     print("yes , 'c' is in the list" )


""" change item value """
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

""" change range of item values """
# list1 = [1,2,3,4,5,6,7,8]
# list1[3:6] = ["a","b","c"]
# print(list1)

""" change list item """
# thislist = ["apple", "banana", "cherry","a"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

""" insert() item """
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "watermelon")             #insert()
# print(thislist)                           #op ['apple', 'banana', 'watermelon', 'cherry']

"""" append() item """
# list1 = ["a","b","c"]
# list1.append("v")
# print(list1)


""" extend() list """      #imp
# list1 = ["a" , "b", "c","d"]
# list2 = ["x", "y", "z"]
# list1.extend(list2)
# print(list1)

""" add any iterable  """
# list1 = ["a" , "b", "c","d"]
# tuple1 = ("t","u","p","l")          #tuple
# dic1 =  {"kiwi":2, "orange":3}

# #list1.extend(tuple1)
#                   #['a', 'b', 'c', 'd', 't', 'u', 'p', 'l']
# list1.extend(dic1)
# print(list1)            #['a', 'b', 'c', 'd', 'kiwi', 'orange']

""" remove() specified list """
# list1 = ["a","b","c","d"]
# list1.remove("c")
# print(list1)                      #['a', 'b', 'd']

"""ex"""
# list1 = ["a","b","c","d" ,"c"]
# list1.remove("c")                       #first occurrence
# print(list1)                            #['a', 'b', 'd', 'c']

""" pop() remove specified index """
# list1 = ["a","b","c","d" ,"c"]
# list1.pop(2)                    # specified index
# print(list1)                 #['a', 'b', 'd', 'c']
"""ex"""
# list1 = ["a","b","c","d" ,"c"]
# list1.pop()                    # specified index pop() remove last item
# print(list1)                 #['a', 'b', 'c', 'd']

""" del keyword remove specified index"""
# list1 = ["a","b","c","d" ,"c"]
# del list1[2]
# print(list1)             #['a', 'b', 'd', 'c']

""" completely delete list """
# list1 = ["a","b","c","d" ,"c"]
# del list1
# print(list1)                   #NameError : list1 is not defined

""" clear() the list """
# #list still remains but it has no content
# list1 = ["a","b","c","d" ,"c"]
# list1.clear()
# print(list1)                   #[]

""" loop lists """
# list1 = ["a","b","c","d" ,"c"]
# for x in list1 :
#     print(x)
# #op     
# # a
# # b
# # c
# # d
# # c
""" loop through the index numbers """
# list1 = [ "a","b","c","d","c"]
# for x in range(len(list1)):
#     print(list1[x])
# # #op     
# # # a
# # # b
# # # c
# # # d
# # # c

""" while loop"""
# list1 = [ 2,3,4,5,6,7]        # 6[0-5]
# i = 0
# while i<len((list1)): # i = 0,1,2,3,4,5<len=6
#     print(list1[i])
#     i = i+1 

""" looping using list comprehension"""    #imp
# list1 = [ 2,3,4,5]
# [print(x) for x in list1]    
# op
# 2
# 3
# 4
# 5

""" list comprehension """
# its offers a shorter syntax when you wnt to create a new list based on the values of an existing list
#ex = list of fruits , you wnt a new list , comtaining only the fruits with the letter "a" in te name

"""ex"""
# fruits = [ "apple", "banana","cherry","kiwi","mango"]
# newlist = []
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)           #['apple', 'banana', 'mango']
 
"""comprehension"""   #imp

# fruits = [ "apple", "banana","cherry","kiwi","mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)             #['apple', 'banana', 'mango']


"""syntex"""
# newlist = [expression for item in itrable if condition == True]
# newlist = [x.upper() for x in fruits]

"""ex"""
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = ['hello' for x in fruits]
# print(newlist)    #['hello', 'hello', 'hello', 'hello', 'hello']

""" ex"""
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)       #['apple', 'orange', 'cherry', 'kiwi', 'mango']

"""ex"""
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#      if x != "banana":
#          None
#      else: 
#         x="or"
#      newlist.append(x)
# print(newlist)

""" sort() lists """
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)
""" ex"""
# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

"""sort(reverse = True) descending """
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

""" customize sort(key = func) function """
# def myfunx(n):
#     return abs(n - 50)
# list1 = [200,100,50,20,10]
# list1.sort(key = myfunx)
# print(list1)                           #[50, 20, 10, 100, 200]

""" case insensitive sort """
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)        # capital then lower case letter


"""ex"""
# list1 = ["banana","apple","Kivi","cherry"]
# list1.sort(key = str.lower)
# print(list1)


""" reverse()"""
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)       #['cherry', 'Kiwi', 'Orange', 'banana']

""" copy() lists"""
# list1 = [ 2,3,4,5]
# newlist = list1.copy()
# print(newlist)                     #[2, 3, 4, 5]

""" list()"""
# list1 = [ 2,3,4,5]
# newlist = list(list1)
# print(newlist)                           #[2, 3, 4, 5]

""" join list"""
# list1 = [2,3,4]
# list2 = [5,6,7]
# list3 = list1 + list2
# print(list3)                     #[2, 3, 4, 5, 6, 7]

"""another way"""
# list1 = ["a","b","c"]
# list2 = [1,3,4]
# for x in list2:
#     list1.append(x)
# print(list1)                    #['a', 'b', 'c', 1, 3, 4]


""" extend()"""
# list1 = ["a","b","c"]
# list2 = [1,3,4]
# list1.extend(list2)
# print(list1)                   #['a', 'b', 'c', 1, 3, 4]

""" list methods """
# append()   : list1.append("kivi")
# clear()    : list1.clear()
# copy()     :newlist = list1.copy()
# count()    : 
# extend()  :list1.extend(list2)
# index()   : 
# insert()  :thislist.insert(1, "watermelon")  
# pop()     :list1.pop(2)          2 is indexing no.
# remove()  :list1.remove("c")
# reverse() : thislist.reverse()
# sort()     : list1.sort()

""" tuple(()) """
''' tuple        '''
''' access tuples '''
''' update tuples '''
''' unpack tuples '''
''' loop tuples   '''
''' join tuple    '''
''' tuple method  '''
# tuple are used to store multiple items in a single variable
# ordered | unchangeable | allow duplicate
# tuple1 = ("a","b","c","d","a","c")
# print(tuple1)

""" len()"""
# print(len(tuple))

""" tuple or not """
# tuple1 = ("apple",)           #tuple
# tuple2 = ("apple")          #string
# print(type(tuple2))

""" type() """
# tuple1 = ("asv",23,True)

""" constructor """
# tuple1 = tuple((234,2344,45,67))

''' collection Arrays'''
# tuple : ordered | unchangeable | allows duplicate
# list  : ordered | changeable   | allows duplicate
# dict  : ordered | changeable   | no duplicate
# set   :unordered| unchangeable | no duplicate   | unindexed

""" access tuple items"""
# tuple1 = ("a","b","c","d")
# print(tuple1[2])      #c
 

""" negative indexing """
# tpl = ("a", "v" , "c")
# print(tpl[-1])        #c

""" range of index"""
# tpl = (2,3,4,5,6,7,8)
# print(tpl[1:]) # (3, 4, 5, 6, 7, 8)
# print(tpl[:4]) # (2, 3, 4, 5)
# print(tpl[-3:-1]) #(6, 7)

""" check it item exists """
# tpl = (2,3,4,5,67)
# if 67 in tpl:
#     print("yes have 67 in")

""" update tuples """      #imp
'''Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.'''
# tpl = (3,4,5,6,7,8)
# y = list(tpl)
# y[0] = 99
# tpl = tuple(y)
# print(tpl)              #(99, 4, 5, 6, 7, 8)

""" append() """
# tpl =(3,4,5,6)
# y = list(tpl)
# y.append("a")
# tpl = tuple(y)
# print(tpl)

""" other way """
# tpl = (2,34,56)
# tpl3 = (3,)        #(3) its a string 
# tpl = tpl +tpl3
# print(tpl)

""" remove """
# tpl = (3,4,5,6,7,8)
# y = list(tpl)
# y.remove(5)
# tpl = tuple(y)
# print(tpl)  


""" delete """
# tpl = (3,4,5)
# del tpl
# print(tpl)

""" unpack tuples """
##when we create a tuple , we normally assign values to it this is called "packing" a tuple
# tpl = (3,3,2,4)
## we are also allowed to extract the values back into variables this is called "unpacking"
''' unpacking tuple'''    #imp
# fruits = ("apple", "banana", "cherry")
# (green ,yellow , red) = fruits
# print(green)       #apple
# print(yellow)       #banana
# print(red)          #cherry
# print(yellow)      #banana

""" using asterisk * """
# fruits = ("apple", "banana","strawberry","raspberry")
# (green , yellow , *red) = fruits 
# print(green)
# print(yellow)
# print(red)
## op
## apple
## banana
## ['strawberry', 'raspberry']
""""""
# fruits = ("apple", "banana","strawberry","raspberry")
# (green , *yellow , red) = fruits
# print(green)
# print(yellow)
# print(red)
##apple
##['banana', 'strawberry']
##raspberry

""" loop though a tuple"""
# fruit = (3,4,5)
# for x in fruit:
#     print(x)

""" loop though the index numbers """
'''rang() len()'''
# tpl = (3,4,5)
# for i in range(len(tpl)):
#     print(tpl[i])

""" using a while loop """
# tpl = (3,4,2,2)
# i = 0
# while i < len(tpl):
#     print(tpl[i])
#     i +=1

""" join two tuple   +   """
# tpl1 = (3,4,5)
# tpl2 = (3,2,1)
# tpl = tpl1 + tpl2
# print (tpl)            # (3, 4, 5, 3, 2, 1)

""" multiply tuples *   """
# tpl = (2,3,4)
# tpl1 = 2*tpl            # 2*tpl = tpl*2
# print(tpl1)     # (2, 3, 4, 2, 3, 4)

""" tuplw methods """
# count() : returns the no. of times aspecified value occurs in a tuple
# index() : search the tuple for a specified value and return the position of where it was found

""" set(()) , {}"""
# sets are used to store multiple items in a single variable
# unorder | unchangeable | unindexed | not allow duplicates

""" duplicates not allowed | unchange """
# myset = {2,3,4,3,2,4,6}
# print(myset)    #op  {2, 3, 4, 6}

'''ex'''
# thisset = {3,4, False ,5,6, True , "r",}
# print(thisset)       #{False, True, 'r', 3, 4, 5, 6}

""" length of set """
# sett =  {3,4, False ,5,6, True , "r",}
# print(len(sett)) #7
# print(type(sett)) #<class 'set'>

"""### set(())  constructor """
''' sets                         '''
''' acceass set items       '''
''' add set items           '''
''' remove set items               '''
''' loop sets               '''
''' join sets                      '''
''' set methods          '''
# sett = set(("a","b",1,3,4))
# print(sett)        #{1, 3, 4, 'a', 'b'}

""" python collextions arrays """
# list  : ordered | changeable | allows duplicate
# tuple : ordered | unchaneable| allows duplicate
# dict  : ordered | changeable | dont duplicate
# set   :unordered|unchangeable| dont duplicate |unindexed

""" access items """ 
# thisset = {3,4, False ,5,6, True , "r",} 
# for x in thisset:
#        print(x)                                           
# # False
# # True
# # r
# # 3
# # 4
# # 5
# # 6

""" cheack item """
# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset)

""" change cannot but add() new"""
# sett1 = {2,3,4}
# sett1.add(7)
# print(sett1)         #{2, 3, 4, 7}

""" update() """
# sett1 = {1,2,3}
# sett2 = {4,7,5}
# sett1.update(sett2)
# print(sett1)         #{1, 2, 3, 4, 5, 7}

""" add any iterable """
# sett = {2,3,4}
# listt = [1,2,2,2,1]
# sett.update(listt)
# print(sett)                    #{1, 2, 3, 4}

"""## remove set item """
''' remove() '''
'''discard()'''
# sett = {2,3,4}
# sett.remove(3)
# print(sett)           #{2, 4}

''' discard() ''' #Note: If the item to remove does not exist, discard() will NOT raise an error.
# sett = {2,3,4}
# sett.discard(3)
# print(sett)           #{2, 4}
''' pop() ''' # remove a random item
# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset)


''' clear()'''   # empties the set
# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)

''' del ''' #keyword will delete the set
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)

""" loop item """
# sett = {3,4,56,6}
# for x in sett:
#     print(x)
# # 56
# # 3
# # 4
# # 6

""" ##join set """

'''  update()           '''
'''  union()        , | '''
'''  intersection() , & '''
'''  intersection_update() '''
'''  difference()   , -   '''
'''  difference_update() '''
'''  symmetric_difference() , ^  '''
''' symmetric_diffrence_update() '''
''' update()'''       #Note: Both union() and update() will exclude any duplicate items.
# sett ={3,4,5}
# sett1 = {6,7,8}
# sett.update(sett1)
# print(sett)               #{3, 4, 5, 6, 7, 8}


''' union() or | opretor'''
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)                  #{'a', 1, 2, 'b', 'c', 3}
''' ex'''
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1 | set2       # its union()
# print(set3)

''' join muiltipal '''
# sett1 = {"a","b"}
# sett2 = {1,2,3}
# sett3 = {"sd","ef"}
# sett4 = {23,43,34}
# mysett = sett1.union(sett2,sett3,sett4)
# print(mysett)

''' ex with |'''
# sett1 = {"a","b"}
# sett2 = {1,2,3}
# sett3 = {"sd","ef"}
# sett4 = {23,43,34}
# mysett = sett1 |sett2 |sett3 | sett4
# print(mysett)

''' set and tuple '''
# sett = {1,23,3}
# tpl = (3,4,55,0)
# mysett = sett.union(tpl)
# print(mysett)
''' intersection() , & opretor '''   #imp    #You can use the & operator instead of the intersection() method, and you will get the same result.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)
# print(set3)                                #{'apple'}
''' ex with & '''         #Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 & set2
# print(set3)
'''ex  False =0, true =1'''
# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}
# set3 = set1.intersection(set2)
# print(set3)          #{False, 1, 'apple'}
''' intersection_update() '''    #intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.intersection_update(set2)
# print(set1)                       #{'apple'}
''' difference()  , - ''' #imp
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# # set3 = set1.difference(set2)
# # print(set3)      #{1, 2}
# set3 = set2.difference(set1)
# print(set3)            #{5, 6}
'''  -  '''          #Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# set3 = set1 - set2
# print(set3)

''' difference_update() '''
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.difference_update(set2)
# print(set1)

''' symmetric_difference()  '''
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3)
''' ^ '''           #Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 ^ set2
# print(set3)

''' symmetric_diffrence_update() '''
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.symmetric_difference_update(set2)
# print(set1) #{'cherry', 'microsoft', 'banana', 'google'}
  
""" set methods """ #Python has a set of built-in methods that you can use on sets.
''' add()                   '''
''' clear()                 '''
''' copy()                  '''
''' discard()               '''
''' pop()                   '''
''' remove()                '''
''' union()           |       '''
''' diffrence()          -    '''
''' diffrence_update()      -=   '''
''' intersection()        &     '''
''' intersection_update()    &=   '''
''' isdisjoint()                ''' #Returns whether two sets have a intersection or not
''' issubset()               <=      '''#	Returns whether another set contains this set or not
''' <                            '''
''' >                            '''
''' issuperset()             >=          '''
''' symmetric_difference()        ^       '''
''' symmetric_difference_update()  ^=            '''


""" dictionaries """
''' access items ''' #get(), keys()
''' change items '''
''' add items    '''
''' remove items '''
''' loop dictionarues '''
''' copy dictionaries '''
''' nested dictionaries '''
''' dictionary methods ''' 

""" dictionaries """     # py3.7 are ordered py3.6 and earlier unordered
# ordered | changeable |  not duplicates '''
# dict1 = {"brand": "ford" , 
#          "model ": "mustang",
#          "year" :1964  }
# print(dict1)
# print(dict1["brand"])

''' duplicate value '''
# dictt = { "brand" : "ford",
#          "model" : "mustang",
#          "year" : 1964,
#          "year" : 2020}
# print(dictt) #{'brand': 'ford', 'model': 'mustang', 'year': 2020}
# print(len(dictt))   #3
# print(type(dictt))   # dict

''' dict() constructor '''
# dictt = dict( brand = "ford",
#          model = "mustang",
#          year = 1964,)
# print(dictt) # {'bread' : 'food' ,'model':'mustang','year':1964}

'''access dictionary items '''
# dictt = { "a" : 1,
#          "b" : 2,
#          "c" : 3}
# print(dictt["b"])  # 2

''' get() '''
# x = dictt.get("b")
# print(x) #2

''' keys() ''' # keys() method will return a list of all the keys in the dict
# dictt = { "a" : 1,
#          "b" : 2,
#          "c" : 3}
# x = dictt.keys()
# print(x)  #dict_keys(['a','b','c'])

''' ex '''      #imp
# car = {  "a" : 1,
#          "b" : 2,
#          "c" : 3
#          }
# x = car.keys()
# print(x) #before the change #['a','b','c']
# car["d"] = 3 
# print(x)  #afther the change #['a','b','c','d']
 
''' values ''' #values() #Make a change in the original dictionary, and see that the values list gets updated as well:
# car = {  "a" : 1,
#          "b" : 2,
#          "c" : 3
#          }
# x = car.values()
# print(x)    #dict_values([1, 2, 3])
# car["d"] = 4
# print(x)    #dict_values([1, 2, 3, 4])

''' items()''' #The items() method will return each item in a dictionary, as tuples in a list.
# car = {  "a" : 1,
#          "b" : 2,
#          "c" : 3
#          }
# x = car.items()
# print(x)          #dict_items([('a', 1), ('b', 2), ('c', 3)])
# car["d"] =4
# print(x)          #dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

''' keys() , values() , items() '''

''' check the key exists '''
# car = {  "a" : 1,
#          "b" : 2,
#          "c" : 3
#          }
# if "a" in car:
#     print("yes , 'a' is one of  the keys")

''' change dictionary items'''
# thisdict ={
#     "brand":"ford",
#     "model": "mustang",
#     "year" : 1999
# }
# thisdict["year" ]= 2000
# print(thisdict)     #{'brand': 'ford', 'model': 'mustang', 'year': 2000}

''' update dictionary '''
''' update()'''
# thisdict ={
#     "brand":"ford",
#     "model": "mustang",
#     "year" : 1999
# }
# thisdict.update({"year":2020})
# print(thisdict)       #{'brand': 'ford', 'model': 'mustang', 'year': 2020}

''' add dictionary '''
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# thisdict["color"] = "red"
# print(thisdict)

''' remove dictionary items '''
''' pop() '''
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("brand")
# print(thisdict) #{'model': 'Mustang', 'year': 1964}

''' popitem() '''       # removes the last inserted item
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)             #{'brand': 'Ford', 'model': 'Mustang'}

''' del keyword '''
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # del thisdict["model"]
# # print(thisdict) 

# '''''' #del keyword can also delete the dictionary completely
# del thisdict
# print(thisdict)     

''' clear() '''  #empties the dictionary:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)          #no error

''' loop dictionaties '''
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # for x in thisdict:
# #     print(x)               #only keyprint
# for x in thisdict:
#   print(thisdict[x])       #only value

''' values() '''
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.values():
#     print(x)         #Ford \n Mustang \n 1964

''' keys()'''
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.keys():
#   print(x)       #brand \n model \n year

''' items()'''
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x, y in thisdict.items():
#     print(x,y)
# # brand Ford
# # model Mustang
# # year 1964

''' copy() dictionaryes '''
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)            #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
'''   dict() '''  
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)               #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

''' ex ''' #dict2 = dict1 :you can copy a dictionary simply by typing
#because dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2 
# dict1 = {2:"a",3:"b"}
# dict2 = dict1
# print(dict2)         #{2: 'a', 3: 'b'}

''' Nested dictionaries '''
# child1 = { 
#     "naem":"a",
#     "age" : 9}
# child2 = { 
#     "naem":"b",
#     "age" : 7}
# child3 = { 
#     "naem":"c",
#     "age" : 5}
# myfamily = {
#     "child1" : child1,
#     "child2" : child2,
#     "child3" : child3 }
# print(myfamily) 
#op {'child1': {'naem': 'a', 'age': 9}, 'child2': {'naem': 'b', 'age': 7}, 'child3': {'naem': 'c', 'age': 5}}

''' ex '''
# myfamily = {
#     "child1" : {
#         "name":"a",
#         "age" : 9 },
#     "child2" : {
#         "name":"b",
#         "age" : 6 },
#     "child3" : {
#         "name":"c",
#         "age" : 3 }        
#         }
# print(myfamily) #{'child1': {'name': 'a', 'age': 9}, 'child2': {'name': 'b', 'age': 6}, 'child3': {'name': 'c', 'age': 3}}

''' access items in nested dictionaries '''
# myfamily = {
#     "child1" : {
#         "name":"a",
#         "age" : 9 },
#     "child2" : {
#         "name":"b",
#         "age" : 6 },
#     "child3" : {
#         "name":"c",
#         "age" : 3 }        
#         }
# print(myfamily["child2"]["name"])

''' loop through nested dictionaries '''
''' items() '''
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# for x, a in myfamily.items():
#     print(x)
#     for y in a:
#         print(y + ':', a[y])

''' dictionary methods '''
''' get() '''
''' update() '''
''' values() '''
''' keys() '''
''' pop() '''
''' popitems() '''
''' clear() '''
''' copy() '''
''' items() '''
''' fromkeys() ''' # return a dict with specified keys and value
''' setdefualt() ''' # return value of the spwcified key ,if key does not exist: insert the key , with specified value










""" numbers"""

# import random 
# print (random.randrange(1,10))  # only intger
