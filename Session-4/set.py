# Python Collection - Set
# It doesn't contain duplicate data (Unordered as well)

my_set1 = {1,2,3,4,15,5,3,2,1}
my_set2 = {11,2,3,}
my_set1.add(14)
print(my_set1)

item = 15
if item in my_set1:
    my_set1.remove(item)

# my_set1.remove(15)
my_set1.discard(15)
# remove() may throw an error, if element value not present
# discard() not throw an error, if element value not present
print(my_set1)
# pop, clear, del will also work for set
# Union and Intersaction 
print("Merging of set: ", my_set1 | my_set2)
print("Common elements of set: ", my_set1 & my_set2)


