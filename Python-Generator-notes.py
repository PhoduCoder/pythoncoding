So what is a generator then? 
How is it different from iterator

A generator is a special type of iterator in Python that is defined using a function rather than a class.
It allows you to generate a sequence of values on the fly, rather than having to create an entire collection of values upfront.

A generator function is defined like a normal function, but it uses the yield statement to return a value,
instead of the return statement. 
When the function is called, it returns a generator object, which can be iterated over using a for loop or the next() function.

Example - Generator function for fibonnaci 

def fibonacci_generator(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

for n in fibonacci_generator(100):
    print(n)

==================

