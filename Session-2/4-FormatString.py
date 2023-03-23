msg = "Welcome {} to Ingenuity Gaming"
name  = input("Enter your Name")
print(msg.format(name))

Qty = 5
itemno = 123
price = 49
my_order = "I want {} pieces of item number {} for {:.4f} Rupees"

print(my_order.format(Qty, itemno, price))
