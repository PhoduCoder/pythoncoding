#Collections Examples
#NamedTuples
#Just like tuples, namedtuples are also 
#immutable, but help if you wanted to access
#tuples using named attributes rather than indexes

from collections import namedtuple

#The collections module in Python provides a namedtuple() 
# function that you can use to create a new named tuple class.
#  You pass the name of the class and a list of field names as
#  arguments to the function.

Point = namedtuple("Point", ["latitude","longitude"])

p = Point(1,2)

print(p.latitude)


# 
#Person = namedtuple("Person", ["fname","lname","age"])
#Either works 
#either passed as list of string or tuple of string

Person = namedtuple("Person", ("fname","lname","age"))
new_person=Person("Gaurav","Parashar",32)

print (new_person.age)


#More complex example

from collections import namedtuple

# Create a named tuple class called 'Person' with fields 'name', 'age' and 'gender'
Person = namedtuple("Person", ["name", "age", "gender"])

# Create a list of Person named tuples
people = [Person("Alice", 25, "female"), Person("Bob", 30, "male"), Person("Charlie", 35, "male")]

# Access the fields of a specific person
print(people[0].name) # prints 'Alice'
print(people[0].age) # prints 25
print(people[0].gender) # prints 'female'

# Iterate over the list of people and print their names
for person in people:
    print(person.name)

