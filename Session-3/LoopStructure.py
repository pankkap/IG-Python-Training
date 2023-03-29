# Python has following Loop Structure
# while
# for loop
# for with Range()

# While Loop

# Initialization 
# condition stop to loop
# Increment | decrement to proceed with loop

# i = 1
# while i<=10:
#     print(i)   # 1
#     i += 1     # i = i + 1

# print("Next Instruction after while Loop")


# for loop in Python

# data = ["Pankaj","Nitin", "Vikas", "Vinnet"]

# for i in data:
#     print(i)


# name = "Pankaj Kapoor"
# for i in name:
#     print(i)

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for i in adj:
#     for j in fruits:
#         print(i,j)


# for i in range(5):  
#     print(i)  #0-4

# for i in range(1,11):  
#     print(i)  #1-10

# for i in range(1,11):  
#     print("3 X "+str(i)+"= "+str(3*i))  # Odd number 1-50

# # Break in Python 
# i = 5
# while i <=50:
#     print(i)
#     if(i==40):
#         break
#     i += 5

# continue in Python 
i = 5
# while i <=50:
#     i +=5
#     if(i==40):
#         continue
#     print(i)
    

# i = 1
# while i <=10:
#     print(i) 
#     i += 1
# else:
#     print('Loop is ended after 10 iteration')    
# # else is an option control sequence you can use

# for i in range(11):
#     print(i)
# else:
#     print("Loop completed")    

# Pass statement    

# i = 1
# if (i<=10):
#     pass
# print("Next Instruction")

pwd = 8
if(pwd>8):
    print("Password is Strong")
else:
    print("Password is Week")

# Short-Hand Notation
pwd = 8
print("Password is Strong") if (pwd>=8) else print("Password is Week")




for i in range (1,11):
    for j in range(1,11):
        if(j==5):
            break
        print(i,j)    