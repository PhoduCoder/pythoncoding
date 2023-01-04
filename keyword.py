#using kwargs
# and args

#a,b,_ = (2,3,4,5,6)
#The above line throws an error
#too many values to unpack

a,b,*arg= (2,3,4,5,6)

print (a)
print (b)
print (*arg)

######

def add(x, y, *args):
    total = x + y
    for arg in args:
        total += arg

    return total


result = add(10, 20, 30, 40)
# The way that we have defined the add 
# function, we can pass any number of 
# arguments to this and it will
# work as expected. 
print(result)

#Python assigns 10 to x, 20 to y, and a tuple (30, 40) to args.
# note that arg is a tuple, not a list

#If you use the *args argument, you cannot add more 
# positional arguments. However, you can use keyword arguments.

#When a function has a parameter preceded by an asterisk (*), 
# it can accept a variable number of arguments. And you can pass zero, one, or more arguments to the *args parameter.

#When a function has the **kwargs parameter, 
# it can accept a variable number of keyword arguments 
# as a dictionary.

def fn(*args, **kwargs):
    print(args)
    print(kwargs)

fn (2,3,4,{})
fn (2,3,4,5,{'name':'grv', 'age': 32})
fn (2,3,4,5,{'name':'grv', 'age': 32, 'company': 'aws' })
#**kwargs has to be the last argument