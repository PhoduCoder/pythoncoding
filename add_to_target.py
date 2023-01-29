#Problem Statement
#Given an array of integers nums and an integer target,
# return indices of the two numbers such that they
#  add up to target.

def return_index(inp_list, target):
    # get the target 
    # find all numbers in the list < target 
    # create a dictionary with index and values 
    #{(0,2), (1,3), (2,4), (3,5)}
    # sort the list 
    # try adding the numbers of the list 
    # and if this equals target
    # then return thos
    for i in inp_list:
        for j in range((i+1),len(inp_list)):
            if ( (inp_list[i] + inp_list [j]) == target):
                return (i,j)
            else:
                continue
            
given_list = [2,3,4,5,78]
target_integer=int(input("Enter your target\n"))
value1,value2 = return_index(given_list, target_integer)

print (value1,value2)
