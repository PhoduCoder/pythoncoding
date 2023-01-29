#str-examples

#Given string, make another string of the first
#middle and last character

# str = input("Enter your string\n")

# first_char=str[0]
# last_char=str[-1] #Negative -1 to find the last element

# #Get the length of str
# length = len(str)
# print ("Length of string is ", length, type(length))

# print (length//2)
# print ((length+1)//2)

# if ((length%2)==0):
#     mid_char=str[length//2]
# else:
#     mid_char=str[((length-1)//2)]

# print (first_char+mid_char+last_char)


#Given string
#create another string of
# the middle three characters


def mid_three(given_string):
    length=len(given_string)
    mid_num1=int(length/2)
    mid_num2=int((length-1)/2)
    mid_num3=int((length+1)/2)
    
    mid_three_str=given_string[mid_num1]+given_string[mid_num2]+given_string[mid_num3]
    return mid_three_str

given_string = input("Enter your string\n")

mid_thr=mid_three(given_string)

print (mid_thr)
