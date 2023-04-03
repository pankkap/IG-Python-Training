# File Handling is used to store or get the data from file

# Reading file
# Writing File

# Modes: r, w, a, x
# There are 2 types:
# 1. text file - t
# 2. binary - b

# f = open("C:\\Users\\pankk\\Desktop\\Python Training\\Session-6\\demofile.txt",'w')

# # while True:
# #     readValue = f.readline()
# #     if readValue.isspace():
# #         break
# #     print(readValue)

# # print('hi')

# # writing into the File
# f.close()

# f = open('C:\\Users\\pankk\\Desktop\\Python Training\\Session-6\\demofile.txt','a')
# f.write('\nprevious data not modified111')
# print("File Writing done")

# f1 = open('newFile.txt','r')
# print(f1.read())

import os
if os.path.exists('newFile.txt'):
    print("File Exist")
    os.remove('newFile.txt')
else:
    print('Not Exist')    

