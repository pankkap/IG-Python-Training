# Tuple is a constant data structure provided by List, it is Immutable

my_tuple1 = (1,2,3,4,5)   #integer tuple
my_tuple2 = ("apple", "banana", "cherry")   #string tuple
my_tuple3 = ("abc", 1,2, True)   #string tuple

# my_tuple1[0] = 5  tuble can not modify

print(my_tuple1[-2])
print(my_tuple2)
print(my_tuple3)
print(type(my_tuple3))


# I can update tuple indeirect way

temp_list = list(my_tuple1 )
print(temp_list)
temp_list.append(101)
my_tuple1 = tuple(temp_list)
print(my_tuple1)
print(type(temp_list))