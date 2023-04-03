# Python Collection - List 

my_list1 = [1,2,3,4,5,5,3,2]                   # integer List 
  #  +ve    0 1 2 3 4    
  #  -ve   -5-4-3-2-1
my_list2 = ["apple", "banana", "cherry"] # str List 
my_list3 = ["abc", 1, 2, 3, True]        # mixed List
print(my_list1)
my_list1[0] = 5

# There are two types of Indexing: +ve index, -ve indexing
# print(my_list1[1])
# print(my_list1[-1])

# print(my_list2)
# print(my_list3)
# print(type(my_list3))                   # <class 'list'>

# Iterate the List
# i = 0
# while(i<len(my_list1)):
#     print(my_list1[i], end=" ")
#     i += 1


# for i in my_list2:
#     print(i)


# selective indexing    
# print(my_list3[1:4])
# print(my_list3[1:])
# print(my_list3[:])
# print(my_list3[:4])


# Updating List
temp = [2,3,5]
my_list4 = ['xyz', 1, 5, 10, 15, True, "abc"]
print(my_list4)
my_list4.append(100)   # will add the new element at the end of list

for i in temp:
    my_list4.insert(i+1,i)

my_list4.extend(['a','b','c'])
print(my_list4)

# remove data from list

my_list4.pop()   # remove last element from List
print(my_list4)


my_list4.remove(100)
print(my_list4)

del my_list4[0]
print(my_list4)

my_list4.clear()   # it will only clear the list, but list will be ther
print(my_list4)


del my_list4
print(my_list4)   #error, because list is longer there