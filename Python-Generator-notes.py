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


===
The choice between using a generator or an iterator depends on the specific use case and the characteristics of the data you are working with.

Here are a few general guidelines:

Use an iterator when:

You have a small and well-defined collection of data that you want to iterate over.
You want to iterate over the same data multiple times.
You need to access individual elements of the data by index.
Use a generator when:

You have a large or infinite collection of data that you don't want to store in memory all at once.
You want to generate the data on-the-fly as you iterate over it.
The logic for generating the data is complex.
Iterators are more memory efficient as they only keep track of the current state of iteration and can be used multiple times, whereas generators generate the data on-the-fly, but once generator is exhausted, you can't use it again.

Generators are useful for working with large or infinite sequences of data, such as reading large files, data processing, or generating random data.

Iterators are useful for working with small, well-defined collections of data, such as lists, strings, or tuples, and for cases where you need to iterate over the same data multiple times.

It's worth noting that, you can always convert a generator to an iterator by passing it to the iter() function, but once the generator is exhausted, it can't be used again.
