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


