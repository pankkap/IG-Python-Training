# print(x)

# Excpetion Handling : To avoid Program to be abruptly close
# try:
#   print(x)
# except:
#   print("An exception occurred")

# -----Multiple Except----

# x = 10
# try:
#   print(x/0)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

#------Else Keyword-----
# if no exception caught, else will be used with Exception Handling  

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# -----Finally---------
# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

# -----Finally Example-------
# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")

# Raise
# x = -1
# if x < 0:
#         raise Exception("Sorry, no numbers below zero")

# Raise Exception Handled
# x = -1
# try:
#     if x < 0:
#         raise Exception("Sorry, no numbers below zero")

# except:
#     print("There is an Exception Raised")

x = 123

try:
    if not type(x) is int:
        raise TypeError("Only integers are allowed")
    print(x)
except TypeError:
    print("Some Type Error Raised")    
except:
    print("Some other Exception Raised")    
