my_roman_dict={'I':1,'V':5,'X':10,'L':50, 'C':100,'D':500,'M':1000}

def substring(input):
    substr=[]
    for i in range(len(input)):
        substr.append(input[i])
    return substr

def convert_num(pass_string):
    # Get all the integers 
    all_elements = substring(pass_string)
    print (all_elements)
    sum = 0
    for j in all_elements:
        if (my_roman_dict[all_elements[j]] >= my_roman_dict[all_elements [j+1]]):
            sum = sum + my_roman_dict [j]
        else:
            sum = sum - my_roman_dict [j]

        #if j == "I" and (j+1) == "X"
        #sum = sum + my_roman_dict[j]
    return sum

given_roman="IX"

equi_num = convert_num(given_roman)
print (equi_num)

#Thought Process
#add all string
    
# Get the corresponding values from the dict 
#calculate the sum
#return the sum