Iterators and Iterable 

List is iterable 
But it is not an Iterator

What does that mean?

An iterable is anything that can be looped over
Examples include list, string, dictionaries 

More deeply, it means that
the object needs to return an
iterator object from its __iter__ method

and the iterator that is returned from the 
__iter__method must define a __next__ method 
which acccesses elements in the container 
one at  a time

====
Iterator
An Object with state so that it remembers
where it is at during its iteration
and knows how to fetch its next value using the __next__
method
And when it doesn't have the next value 
then it raises a StopIteration Exception

====


What about tuples, sets?

If something is iterable, then it should have 
a special method are __iter__ method 

__ method are dunder or magic method 

So what is an iterator?

An iterator is an object with state
so that it remembers its state 
during iteration.

Iterator knows how to gets its value
using a __next__ method 

A for loop is doing this behind the scenes.
Getting a iterator of our object
Then calling a next method on the iterator
until it gets the StopIteration Exception

Iterators can only go forward

====

So we can add these methods to our own classes
and make them iterable 

===
Itertor can go on for ever
but still fetches one value at a time

So they are hugely efficient when
you want to write memory efficient programs

This means that the iterator does know
its last state and thus we 
don't need to load the entire list 
in the memory

===
Coding Problem 
Creating your own Iterators 

Create a sentence object 
and when we loop over 
we loop over the words in the sentence

To create the class as iterable
we have to have an __iter__ method
and that __iter__ method
has to return an object 
that has a __next__ method 

=====

The iter function can be used to create an iterator for most types of Python objects that are iterable, such as lists, strings, tuples, and some other built-in types like dicts. When you pass an iterable object to the iter function, it returns an iterator object that can be used to loop over the elements of the iterable.

However, not all objects in Python are iterable. For example, a single number or a scalar value is not iterable, and trying to pass it to the iter function will raise a TypeError.

Additionally, while the iter function can be used to create an iterator for many types of objects, there are some types of objects that have built-in iterator functionality that don't need to be passed to the iter function. For example, when you use a for loop to iterate over a list, the list itself is automatically converted to an iterator by Python, so you don't need to use the iter function.

It's also worth noting that some types of objects, like file objects, have both an iterator interface and a non-iterator interface. For example, a file object can be read one line at a time using the file.readline() method, or it can be converted to an iterator using the iter function and read one line at a time using a for loop.

In summary, the iter function can be used to create an iterator for most types of iterable objects in Python, but it cannot be used to create an iterator for non-iterable objects or objects that already have a built-in iterator interface.




===
Now generators are more simpler
to create the iterator
because they take care of 
the iter and next methods
====

Ternary operation
value_if_true condition value_if_false

====
break is to break out of the loop [for, while]

continue is to continue the loop to the next iteration

====

Default params
def function (param1, param2=value2):
In the above function, 
we have the param2 as a default argument
If we don't pass the value for the second param2
then it will get the value2
**Note that default param will be always after 
other params**
===

A value in the key-value pair can be a number, a string, a list, a tuple, or even another dictionary. In fact, you can use a value of any valid type in Python as the value in the key-value pair.

A key in the key-value pair must be immutable. In other words, the key cannot be changed, for example, a number, a string, a tuple, etc.
====

QUESTIONS:

How is iterator different from paging and virtual memory?

You are correct that virtual memory, specifically paging, only loads the currently used pages of data into memory and pages out the ones that are not being used. This is similar to how an iterator works, in that it only loads a small piece of data into memory at a time.

The difference is in the way the data is accessed and processed:

With virtual memory and paging, the operating system is responsible for managing the pages of data that are in memory and swapping them in and out as needed. The program accesses the data in memory as it would normally, with no need to be aware of the fact that it is using virtual memory.

With an iterator, the program has explicit control over how the data is accessed and when the next piece of data is loaded. The program can choose to load the next piece of data only when it needs it, and can process the current piece of data before loading the next one. This allows for more fine-grained control over memory usage, and can make it easier to work with very large data sets.

In summary, virtual memory and paging are a way for the operating system to manage the memory of the computer to allow programs to work with larger data sets, whereas an iterator is a way for a program to explicitly manage the way it accesses and processes a sequence of data. Both have their own advantages and use cases, but an iterator gives more control over the data being processed.

=========
