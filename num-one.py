#Problem PlusOne the number and return

def generate_num(input_list):
    num = 0
    length=len(input_list)
    for i in range(length):
        num +=input_list[i]*pow(10,(length-i-1))
    return num

def plusone(given_list):
    return (generate_num(given_list)+1)

given_list=[9,9,9,9]
#num=generate_num(given_list)
#print (num)
plusonenum = plusone(given_list)
print ("Original list was", given_list)
print ("Plus one number is ", plusonenum)

print ("What if i wanted to return as a list")

print ("convert the num to str and have a list comprehension")

list_plus_one=[int(i) for i in str(plusonenum)]

print (list_plus_one)



# new_num=plusone(given_list)
# print (new_num)
