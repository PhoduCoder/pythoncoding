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

you can have custom logic in your generator function to determine the next value to be yielded.
The yield statement is used to return a value from the generator function, but you can include any logic you want before or after the yield statement
to determine what value to return.

=================

def even_generator(max):
    current = 0
    while current <= max:
        if current % 2 == 0:
            yield current
        current += 1

for num in even_generator(10):
    print(num)

    
=================

In this example, the generator function uses a while loop to iterate through the numbers from 0 to max, and it checks if the current number is even. If it is, it yields the value, otherwise it increments the current number and continues the loop. Once the loop has finished and the current number is greater than the max, the generator function ends and no more values are returned.

You can implement any logic you want in the generator function to determine what value to yield next. This allows you to generate a sequence of values based on a specific algorithm or process.
