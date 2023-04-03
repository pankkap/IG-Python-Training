# Mutable, ordered with key
my_dic1 = { 
    "name": "Pankaj",
    "age": 32,
    "address":"Chandigarh"
}
print(my_dic1)
print(my_dic1["name"])


for i,j in my_dic1.items():
    print(i,j)

print(my_dic1.keys())    
print(my_dic1.values())    
print(my_dic1.items())    



# constructor 
my_dic2 = dict(designation="Manager", shift="hybrid", timing=8)
# duplicate keys not allow
print(my_dic2)