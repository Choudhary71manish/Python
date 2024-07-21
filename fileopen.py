# file open
# open()   #function

# "r" read
# "w" write
# "a" append : open a file for appending, creates the file if it does not exit
# "x" create : create the file return error if file exists
# "t" text : default value text ModuleNotFoundError
# "b" binary : binary mode

""" file open"""
# f = open("learnpython\demo.txt")

""" open and read"""
# f = open("learnpython\demo.txt", "r")
# print(f.read())

""" read only part"""
# f = open("learnpython\demo.txt", "r")
# print(f.read(5))                     # hello 

""" read lines"""
# f = open("learnpython\demo.txt", "r")
# print(f.readline())                     # hello my name is manish
""" """
# f = open("learnpython\demo.txt", "r")
# print(f.readline())                     #hello my name is manish
# print(f.readline())                     #my age is 18+

"""use looop"""
# f = open("learnpython\demo.txt", "r")
# for x in f:
#   print(x)                             # all print

""" close files"""
# f = open("learnpython\demo.txt" , "r")
# print(f.readline())
# f.close()

""" file write"""
# "w" : overwrite
# "a" : append
 
# f = open("learnpython\demo2.txt" , "a")  # new file make
# f.write("now the file has more content!")
# f.close()

""" open , read a after appending"""
# f = open("learnpython\demo2.txt", "r")
# print(f.read())

""" write "w" """
# f = open("learnpython\demo2.txt", "w")
# f.write("woops! i have overwrite in demo2 file in its means old data we are delete and put same new data")
# f = open("learnpython\demo2.txt", "r")          # mode is read
# print(f.read())

""" create new file""" 
# "x" : create - will create a file , returns an error if the file exist
# "a" : append - will create a file if the specified file does not exist
# "w" : write  - will create a file if the specified file does not exist
"""ex"""
# f = open("learnpython\demo2.txt", "x")   #FileExistsError
# f = open("learnpython\demo2.txt", "a")     #work
# f = open("learnpython\demo2.txt", "w")     #work
# f = open("learnpython\demo4.txt", "x")     #create newfile
# f = open("learnpython\demo5.txt", "w")     #create newfile
# f = open("learnpython\demo6.txt", "w")     #create newfile


""" delete file """
# import os 
# os.remove("learnpython\demo4.txt")            #demo4 is delete

""" cheack if file exist"""
# import os
# if os.path.exists("learnpython\demo4.txt"):
#     os.remove("learnpython\demo4.txt")
# else:
#     print("the file does not exist")

""" delete folder """
import os
os.rmdir("learnpython\myfolder")

""" file handling conplete"""