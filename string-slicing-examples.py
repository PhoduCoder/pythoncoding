#String slice 

s="ABCDEFGHIJKLMN"

#s[start:stop:step]

print (s[0:]) 
# Whole string 
#Default end with positive or no step is 
#till the end of string

p=len(s)

#Another way to print the whole string
print(s[0:p])

#Note that the end slice goes uptil the end-1 position
# i.e. s[0,5]
# will print from the start till the 4th index


#Say if we wanted to print all the alternate char 
# in the string 
print (s[0:p:2])

#Say if we wanted to print every third character 
# in the string 
print (s[0:p:3])


#Now if we skipped the end in the slicing,
#it defaults to the end of the string
print(s[0::2])

#Similarly if we leave the start
#it defaults to 0
print(s[:p:1])

#If we don't specify the step,
#it defaults to 1


#Now say we wanted to print 
#all the char starting from 
#1st position till the end
# but every 3rd character
# i.e. 1st, 4th, 7th, 10th,13th
print(s[0:p:3])

#Negative in slicing
# "-1" represents the last char of string

#So another way to print the entire string 
#can be s[0:-1]
print(s[0:-1])

#Now if you wanted to start 
# printing from the last element, printing in reverse
# you can give -1 as the start
# leave the end as blank
# and make step as -1
s[-1::-1]

#Similarly if you wanted to print 
# every 2nd element from the end
print (s[-1::-2])

# note that if we don't specify the end
# it defaults to the last element of string
# however, if we make the step as -1
# and don't specify the string
# so it defaults to beginning of string
print (s[-1])  # this will default the end to 0

print (s[-1::-1])
# in this case, it defaults to start of string


