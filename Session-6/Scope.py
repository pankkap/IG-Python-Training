# There are 2 types of Scopes in Programming
# 1. Local 
# 2. Global

x = 15      # Global Variable 
def add():
    global x
    # x = 10     # local variable and scope is local to the function
    def innerFun():
        print(x)
    innerFun()    
    print(x)
add()
print(x)    