# conditions and if statements 
# equals ==
# not equals !=
# less than <
# greater than > 
# <=
# >=

""" if / if else """
# a = 330
# b = 200
# if a>b :
#     print("a is great than b")
# # else :
# #     print("b is great than a")

''' if / elif '''
# a = 11
# b = 2
# if a>b :     # only selete one condition if/ elif../ or else
#     print("a is great than b")
# elif b>a :
#      print("b is great than a")
# elif a == b :
#     print(" both are equals")

''' if / elif / else'''
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

''' Short hand if ''' #imp 
# if a>b : print("a>b")
''' Short hand if elif ''' #imp
# a = 2
# b = 3
# print("a")if a>b else print("b")

''' Short hand 3 comditions '''
# a = 4
# b = 4
# print("A") if a > b else print("b") if a < b else print("=")

''' and '''
# a = 40
# b = 30 
# c = 50
# if a > b and c > a:
#     print(" both condition true ")

''' or '''
# a = 10
# b = 20
# c = 30 
# if a > b or c > a :
#     print("at least one of the conditions is True")

''' not '''
# a = 10
# b = 20
# c = 30 
# if not a > b  :
#     print(" a>b not true")

''' nested if '''
# x = 45
# if x > 10 :
#     print("above 10")
#     if x > 20:
#         print(" above 20 ")
#     else: print(" not above 20 ")

''' pass '''
# a = 1
# b = 2 
# if b>a :   #IndentationError
''' ex '''
# a = 1
# b = 2 
# if b>a :
#     pass       # no error


""" python loops """
''' while loops '''
''' for loops '''


''' while loops ''' # while loop we can execute a set of statements as long as a conditions is true.
# i = 1
# while i<6:
#     print(i)
#     i += 1     # 1 2 3 4 5

''' break  statement '''
# we can stop the loop even if the while condition is true
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1               # 1 2 3

''' continue statement '''
# continue statement we can stop the current iteration and continue with the next 
# i = 0
# while i < 6:
#     i += 1 
#     if i == 3:
#         continue
#     print(i)

''' else statement ''' # imp
# with the else statement we can run a block of code once when the condition no longer is true
# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else: 
#     print(" i is no longer less than 6")  

''' for '''
# for loop is used for iterating over a sequence
#(that is either a list,tuple,dictionary,set)

''' ex '''
# fruits = ["apple" ," banana", " cherry"]
# for x in fruits:
#     print(x) # apple \n banana \n cherry

''' looping through a string '''
# for x in "banana":
#     print(x)

''' break '''
# fruits = ["apple","banana","cherry"]
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break

''' continue statement '''
# fruits = ["apple", "banana", "cherry"]
# for x in fruits :
#     if x == "apple":
#         continue
#     print(x)

''' range() function '''
# range( start , end , step)
# range(6) 0 by default and increments by 1 (0-5)
# range(3 ,6 , 2) range 3,4,5 and increaments by 2


''' ex '''
# for x in range(5):
#     print(x)

''' ex ''' 
# for x in range (3,8,2):
#     print(x)  #3 5 7

'''  else in for loop '''  #imp # if loop not break then else run 
# for x in range(2,8):
#     print(x)
#     if x==6:
#         break
# else:
#     print("finally finished")  #op 23456
'''Note: The else block will NOT be executed if the loop is stopped by a break statement.'''
'''ex '''
# for x in range(2,8):
#     print(x)
# else:
#     print("finally finished") 
# # 2
# # 3
# # 4
# # 5
# # 6
# # 7
# # finally finished

''' nested loops '''
# inner loop will be exexuted one time foe each iteration of the outer loop 

''' ex '''
# fruits = ["apple", "banana","cherry"]
# color = ["lightgreen","green" , "red"]

# for x in color:
#     for y in fruits:
#         print( y , x)

''' pass statement '''
''' for loops cannot be empty,'''
# for x in [1,2,3]:
#     pass

''' functions '''
#  "def" keyword 
#  def my_func( agument1, agument2,..)

''' ex '''
# def my_func():          # initial de
#     print("hello from a function")

''' calling '''
# def my_func():          
#       print("hello from a function")
# my_func() #calling 

''' arguments '''
# def my_func(fname):
#     print(fname + "hello")
# my_func("email")
# my_func("linus")

'''  paraments or arguments '''
#The terms parameter and argument can be used for the same thing: information that are passed into a function
#This function expects 2 arguments, and gets 2 arguments:
# def my_func(fname,lname):
#     print(fname + " " + lname)

# my_func("manish","choudhary")

''' the function expects 2 arguments , but gets only 1'''
# def my_func( fname ,lname):
#     print(fname + lname )
# my_func("manish")       # typeerror


''' arbitray arguments , *args''' #imp
#This way the function will receive a tuple of arguments, and can access the items accordingly
# def myfunc(*kids):
#     print("this youngest child id " + kids[2])
# myfunc("aa","bb","cc")

''' keyword arguments ''' ### imp
# you can also send arguments with the key = value syntax
''' ex '''
# def my_func(child3, child2, child1):
#     print("the youngest child is " + child3)
# my_func(child1 = "zz",child3 ="yy",child2 = "xx")

''' arbitrary keyword arguments , **kwargs '''
# def myfunc(**kid):
#     print("asterisk asterisk" + kid["lname"])
# myfunc(fname = "asterisk" , lname = "asterisk")

''' defult parameter value '''
# def myfunc( country = "usa"):
#     print(" asterisk country name "+ country)
# myfunc("india")
# myfunc()
# myfunc("japan")

''' passing a list as an arguments '''
#any data type of agruments to a func (string,list,tuple,dict)
# def myfunc(food):
#     for x in food:
#         print(x)
# fruits = ["a", "b", "c"]
# myfunc(fruits)     # a b c \n

''' return values '''
# def myfunc(x):
#     return 5*x
# print(myfunc(3))
# print(myfunc(4))

''' the pass statment '''
# def myfanc():
#     pass             # if not use pass error indentationerror
# myfanc()

''' positional only arguments '''
# ,/ arguments
# def func(x ,/): # whithout the ,/ you are actuallu allowed to use keyword args even 
#     print(x)
# func(3)

'''ex '''
# def func(x ): # whithout the ,/ you are actuallu allowed to use keyword args even 
#     print(x)
# func(x=3)    # ,/ use we will get  error 

''' keyword only arguments '''
# def func(* , x):  # tospecify that a funtion can have only keyword args and *, before the args
#     print(x)
# func(x = 3)    

''' ex'''
# def func( x):  # without *, you are allowed to use positionale args even if the function expects keywrd args
#     print(x)
# func(3)    

''' * , / ''' 
# def func(*,x):
#     print(x)
# func(3)     #erro typeerror

''' combine poditional only and keyword only '''
# def func(a,b,/,*,c,d): #Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
#     print(a+b+c+d)
# func(5,6,c=7,d=8)

''' recursion '''
# function can call itself

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
    
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)


''' ex  print 1 to n without loop'''
# def func(n):
#     if n == 0: return
#     func(n-1)
#     print(n , end=' ')
# func(10)

''' print fibonacci series '''
#  1 2 3 5 8 13 21
#  a7 =  13 + 8    a7 = a6 + a5
#  a6 =  8 + 5                                       # c=5 b=8 bn=13
#  a5 =  5 + 3                                       # c=3 b=5 bn=8
#  a4 =  3 + 2                    b2 = b1 + c  , c = b # c=2 b=3,bn=5   
#  a3 =  2 + 1   a3 = a2 + a1     b1 = b + a  , c = b # a=1,b=2,bn=3,c=2/3
#  a2 =  1 + 1   
#  a1 =  1 + 0            

#  a6 = a5 + a4
#  n  =  n +   
''' use loop in fibunaccci'''
# i = 0
# a = 0
# b = 1
# c = None
# for i in range(10):
#     print( a, end = ' ')
#     c = b + a               # 3 = 2+1
#     a = b                   # a=2
#     b = c                   # b=3
''' fibunacci series use func '''
# def fbnc(count):
#     if count>1:
#         print(count)    
#         a = fbnc(count -1) + fbnc(count-2)
#         print("aft",a)
#     else :
#         fbnc(0) = 0
#         fbnc(1) = 0
#         return print("return")



# fbnc(10)    
''' test '''
### 1  2 3 4 5 6 7 = sum 430 tk sum
# i = 0 
# n = 10
# sum = 0 
# for i in range(n+1):  
#             sum = i + sum
# print(sum)

''' test func'''
# def sum(n):
#     sum = 0
#     i = 0 
#     for i in range(n+1):
#         sum = sum + i
#     print(sum)

# sum(4)

''' test recurison'''

# def sum(n):
#     sum = 0
#     for i in range(n + 1):
#         sum = sum + i
#     print(sum)

# sum(4))        

''' recursive pritn no. '''

# def func(n):
#     if n == 0 : return
#     func(n-1)
#     print(n)
# func(5)

''' recursive a^2 '''
# def sqrser(n):
#      if n == 0: return
#      sqr = n*n
#      sqrser(n-1)
#      print(sqr)
# sqrser(4)
''' iota '''
# def iota(n):
#      if n == 0 : return 1
#      a = (iota(n-1))
#      sum  = n*a
#     #  print("bf",n) 
#      return sum
# x = iota(3)
# print(x)  


''' factorial '''
# def fac(n):
#     if n == 0:
#         return 1
#     return n*fac(n-1)
# print(fac(4))


''' fbnc '''# 0 1 1 2 3 5 8 13 21
# def fbnc(n):
#     if n == 0: 
#          return 0
#     if n == 1:
#          return 1
#     a = fbnc(n-2) + fbnc(n-1)         
#     print(a)
#     return a
# fbnc(5)

# n = 0 , rt 0
# n = 1 , rt 1
# n = 2 , rt 1
# n = 3 , rt 2


''' fbnc '''   # my concept
# def f(x , n=0):
#     if n == x:
#         return
#     if n == 0:
#         global a ,b 
#         a =  0
#         b =  1   
#     c = a + b
#     a = b
#     b = c
#     f(x,n+1)
#     print(a,b,c)
# f(10)

''' fbnc '''
# def f(n):
#     if n == 1 : 
#         global a ,b 
#         a =  0
#         b =  1    
#         return 
#     f(n-1)
#     c = a + b
#     a = b
#     b = c
#     print(a,b,c)
#     return c
# f(15)

''' fbnc '''
# def f(n):
#     if n == 0 :
#         return
#     if n == 10 :
#         global a,b
#         a = 0
#         b = 1
#     c = a+b
#     a = b
#     b = c
#     # print("bf", a,b,c)
#     f(n-1)
#     print(c)
#     if  n == 10:
#         print(1)
#         print(0)

# f(10)    

''' end practics'''
''' Lambda '''
## a lambda function is a small anonymous function.
## lambda function can take any number of arguments , but can only have one expression.
''' syntax of lambda '''
## lambda arguments : expression
''' ex '''
# x = lambda a :a +10 
# print(x(5))

''' ex '''
# x = lambda a, b : a*b
# print(x(2,3))

''' ex '''
# x = lambda a,b,c :a+b
# print(x(1,2,3))


''' why use lambda functions '''
## anonymous function inside another function 
## def f(n):
## return lambda a : a*n

''' ex '''
# def f(n):
#     return lambda a : a*n
# fn = f(2)
# print(fn(11))

''' ex '''
# def myfunc(n):
#   return lambda a : a * n
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
# x = mydoubler(11)
# print(x)
# print(mytripler(11))

## use lambda function when an anonymous function is required for a short period of time

''' arrays '''
## pythin does not have buit- in support for arrays, but python lists can be used inseted
''' ex '''
# car = ["ford","volvo","bmw"]

## what is an array : an array is a speial vvarable , which ca hild more then one value at a time
## if you have a list of items ( list of a car name )
## car1 = "ford"
## car2 = "volvo"
## car3 = "bmw"  # if u have 300 car than soluton is an array

''' access array '''
# x = cars[0]

''' modify array '''
# cars[0] = "toyota"

''' length array '''
# x = len(cars)

''' looping array '''
# for x in cars:
#     print(x)

''' adding arrary elements '''
# cars.append("honda")

''' pop array elements'''
# cars.pop(1)
''' remove array elements''' # lists remove() method only removes the "first occurrence" of the specified value
# cars.remove("volvo")

""" array method """
## append() # add elements at the end of list
## clear() #remve all elements for the list
## count() # returns the numberof elements with the apecified value
## extend() # add the elements of a list , to the end of the current list 
## index() # return the index of the first element with the specified value
## insert() # adds an element at the specified position 
## pop() # removes the element at the specified position
## remove() # removes the first item with the specified value
## reverse() # reverses the order of the list 
## sort() #sorts the list


""" class and objects """
# class myclass:
#     x = 5 

''' create objest '''
# class myclass:
#     x = 5 
# p1 = myclass()
# print(p1.x)

''' __init__() function ''' # when we create a object auto create init function 
# class person:
#     def __init__(self,xname,xage):
#         self.name = xname
#         self.age = xage 

# p1 = person("manish" , 30)
# print(p1.name , p1.age)

### note : the __init__() function is called automatically every time the class is bering used to create a new object

''' __str__() '''
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
# p1 = Person("John", 36)
# print(p1)
 
''' __str__()'''
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def __str__(self):
#     return f"{self.name}({self.age})"    # f is imp           
# p1 = Person("John", 36)
# print(p1)

''' object methods'''
## object can also contain methods  methods in objects are func that belong to the object

# class person:
#     def __init__(self,name,age ):
#         self.name=name
#         self.age=age
#     def myfunc(self):
#         print("hello my name is " + self.name)
# p1 = person("john",36)
# p1.myfunc()

## note: the self parameter is a rederence to the current instance of the class, and is used to access variables that belong to the class.

''' self parameter '''
## the self parameter is a reference to the current instance of the class and is used to access varibles thet belongs to the class
## it does not have to be named self , you can call it whatever you like , but it had to be the first  parameter of any function in the class:

# class person:
#     def __init__(abcd , name, age):
#         abcd.name = name
#         abcd.age = age
#     def myfunc(abcd):
#         print("hello my name is " + abcd.name)
# p1 = person("john" , 34)
# p1.myfunc()    

''' modify object properties '''
# p1.age = 40 

''' delete object properties '''
# del p1.age 

''' delete objects '''
# del p1 

''' the pass statement '''
## class definitions cannot be empty
# class person:
#     pass 

""" inheritance """
''' create a parent class '''
# class person:
#     def __init__(self, name , age ):
#         self.name = name 
#         self.age = age
#     def printdetail(self):
#         print(self.name , self.age)

# x = person("john" , 67)
# x.printdetail()

# ### ''' create a child class '''
# class student(person):
#     pass                # use the pass keyword when you do not want to add any other properties or methods to the class.
# s1 = student("manish" , 27)
# s1.printdetail()
 
''' add __init__ () func in child's class '''
### so we have created a child class that inherits the properties and methods from its parent 

# class student(person):
#     def __init__(self,name, age):      ##when u add the __init () function the child cladd will no longer inherit the parent's init() func
#### Note: the child's init() function overrides the inheritance of the parent's  init()function.
####
#### to keep the inheritence of the parent's init() function , add a call to the parent's init()

''' ex '''
# class student(person):
#     def __init__(self,name,age):
#         person.__init__(self,name,age)

''' use the super() function '''
# class student(person):
#     def __init__(self, name , age ):
#         super().__init__(name, age )

''' add properties '''
# class person:
#     def __init__(self ,name,age):
#         self.name = name
#         self.age = age 
#     def func1(cnnt):
#         print(cnnt.name , cnnt.age)    

# class student(person):
#     def __init__(self , name , age ):
#         super().__init__(name,age )
#         self.graduationyear = 2018

# s1 = student("manish" ,27)        
# print(s1.name, s1.age, s1.graduationyear )

# p1 = person("vinita" ,20)
# print( p1.name , p1.age )
# p1.func1()

''' ex2 '''
# class person:
#     def __init__(self ,name,age):
#         self.name = name
#         self.age = age 
#     def func1(cnnt):
#         print(cnnt.name , cnnt.age) 

# class student(person):
#     def __init__(self,name,age ,year):
#         super().__init__(name,age)
#         self.year = year
    
# s1 = student("mainsh" , 20,2030 )
# print( s1.name ,s1.age, s1.year )

''' add methods '''
# class person:
#     def __init__(self ,name,age):
#         self.name = name
#         self.age = age 
    
# class student(person):
#     def __init__(self,name,age,year ):
#         super().__init__(name,age)
#         self.year = year
#     def welcome(self):
#         print("welcome", self.name,self.age,self.year)    

# s1 = student("vinta" , 30 , 2020)
# s1.welcome()

""" Iterators """ #iterator is an objects that contains a countable number of values , an iterator is an objext taht can be iterated upon , meaning that you can traverse through all the values.
## technically , in python an iterator is an object which implements the iterator protocal , which consist of the methods  "__iter__() and __next__() "
# mytuple = ("apple", "banana","cherry")
# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))

''' iterator vs iterable '''
### lists ,tuple , dictionaries and sets are all iterable objects.
### even string are iterable objexts , and can return an iterator

# mystr = "apple"
# myit = iter(mystr)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

''' looping through an iterator '''
### we can also use a "for" loop to iterate though an itrable object
# mytyple = ("apple", "banana", "cherry")
# for x in mytyple:
#     print(x)

### the "for" loop actually creates an iteraor object and executes the next() method for each loop

''' create an iterator '''
## __iter__() method acts similar , u can do operations(initializing) but must always return the iterator object itself

''' ex '''
class mynumber:
    def __iter__(self):
        self.a = 1
        return self 
    def __next__(self):
        x = self.a
        self.a += 1 
        return x 
myclass = mynumber()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))






















































































































































































































































































































































































""" dout in """
''' positional only arguments '''
''' keyword only arguments '''
''' combine poositional in;y and keyword only'''
