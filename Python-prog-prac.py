#Reverse an integer
#Could be -ve as well

def reverse_int(given_val):
    #convert to string
    str_val = str(given_val)
    if (str_val[0]=="-"):
        temp_rev_str = str_val[:0:-1]
        rev_val="-"+temp_rev_str
        return int(rev_val)
    else:
        rev_str = str_val[::-1]
        rev_val=int(rev_str)
        return rev_val

while True:
    given_int = (input("Enter your integer\n"))
    rev_int=reverse_int(given_int)
    print ("Reversed value is ", rev_int)

# string [start:end:step]

#to reverse a string
#string[::-1]

#to print 

# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array

# a[start:stop:step] # start through not past stop, by step

#a[-1]    # last item in the array
# a[-2:]   # last two items in the array
# a[:-2]   # everything except the last two items