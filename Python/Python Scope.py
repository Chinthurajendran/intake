#Local Scope
def my_function():
    local_var = 10
    print(local_var)

my_function()


#Global Scope
global_var = 30

def my_function():
    global_var = 10
    print(global_var) 

my_function()
print(global_var)