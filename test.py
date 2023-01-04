num = [1,2,3]

#print (dir(num))

list_iterator=(iter(num))

print (list_iterator)

#Another way to call the iterator
another_iterator = num.__iter__()

#print (another_iterator, dir(another_iterator))

print (another_iterator.next())


#For loop explained via iteration
#A for loop is doing this behind the scenes.
#Getting a iterator of our object
#Then calling a next method on the iterator
#until it gets the StopIteration Exception
iter_num = iter(num)

while True:
    try:
        item = next(iter_num)
        print (item)
    except StopIteration:
        break
