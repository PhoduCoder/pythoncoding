#Generating random number

#Print random numbers between 0 and 1 
# 0 is inclusive, 1 is excluded

import random 
print (random.random())

#To print floating point random numbers in a given range
print (random.uniform(1, 5))

#To print a random integer between a given range [1-10]
print (random.randint(1,10))

#To print random values from a list
greetings = ["Hi", "Hello", "Hola", "Hey", "Ssup"]

value = random.choice(greetings)

print (value + "Gaurav")

