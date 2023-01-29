#given a string and an integer k
# split the string so that
# there are k groups
# each group should
# have exactly k characters
# only the first group can afford to have less
# Furthermore, the groups must be separated by ‘-‘(dash) and have only uppercase letters.

def license(intermediate_string,k):
    #create k lists
    length=len(intermediate_string)
    my_list=[]
    for i in range(1,length,k):
        #5F3Z2e9w
        my_list.append(intermediate_string[-(i):-(i+k):-1])
    return my_list

given_string="2-5g-3-J"
up_string=given_string.upper()
k=2

#Get the string without dashes
#split gives a list
actual_string_to_list=up_string.split("-")

#convert the list back to string
intermediate_string="".join(actual_string_to_list)

#call the function
ret_list = license(intermediate_string,k)

print(ret_list)

print ("reversing")
print (ret_list[::-1])



