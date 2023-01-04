#Ternary Operation in Python

def canivote(age):
    if age>=18:
        return True
    else:
        return False

result = canivote(23)
print (f"Your voting status is {result}")

#Now instead of this you can 
#instead just use

#value-true if condition else value-false
# note that in this there is 
# no use of colons

age = 12
result_new = True if (age>=18) else False
print (f"Your voting status is {result_new}")