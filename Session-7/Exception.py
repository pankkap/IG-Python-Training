x = 10
# try:
#     print(x)
#     f = open('demo.txt')
# except NameError: 
#     print("Variable Error")
# except ZeroDivisionError: 
#     print("Divide by zero Error")
# except:
#     print("Exception in the Program")
# else:
#     print("There is not Exception in the Program")
# finally:
#     f.close()
#     # Memory cleanup task
#     print("this block always execute")    


x = (input("Enter a valid Number"))
# try:
#     if(x<1):
#         raise Exception("Sorry you enter value less than 1")
# except:
#     print("There is some Exception")    


# x = "123"

if not type(x) is int:
    raise TypeError("Only Integer allowed")

