#Collections Dequeue example

#Note that deque allows to add and remove
#elements from both ends i.e. from the 
#front and back

#Deque can be useful in scenarios where you need a data
# structure that can efficiently add and remove elements
#  from both ends

#efficient at adding and removing elements from both ends but 
# less efficient than list or array 
# when it comes to accessing elements by index.

from collections import deque

# Create a new deque
d = deque()

# Add elements to the deque
d.append(1)
d.appendleft(2)
d.extend([3, 4, 5])

print (d)
print ("Deque output")

# Remove elements from the deque
print(d.pop()) # prints 5
print(d.popleft()) # prints 2

# Access elements in the deque
print(d[0]) # prints 1
print(d[-1]) # prints 4







