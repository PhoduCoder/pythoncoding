num = [1,2,3,4,5,7]

#for i in num:
#    print (i)

i_num = iter(num)

print (next(i_num))
print (next(i_num))

#Imagine that 
# if this were an huge list
# then instead of holding the entire 
# big list in memory
# one could instead create an iterator
# of the list and call the next function
# on the iterator

# This way we are writing an 
#efficient python Program