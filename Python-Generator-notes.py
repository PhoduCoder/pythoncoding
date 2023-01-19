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


=======


In the case of an iterator, the __next__() method is responsible for returning the next value in the sequence, but it is typically implemented using a collection of data that has been created upfront. The method simply returns the next value in the collection.

On the other hand, in a generator, the yield statement is used to return a value from the generator function, but the function is typically implemented using logic or an algorithm to generate the data on the fly, rather than using a pre-existing collection of data.


For example, if you have a large file and you want to read it line by line and process it, you would use a generator function. With generator, you don't have to read the entire file into memory at once, but instead you can read one line at a time and process it, which is more memory efficient.

You can implement the same logic in the __next__() method of an iterator class, but it would not be as memory efficient as the generator function, because it would read the entire file into memory before processing it.

In summary, Generating data on the fly means that the data is not stored in memory all at once but rather generated as you iterate over it. This is different from creating an entire collection of data upfront and then iterating over it. Generators are more memory efficient than iterators when you have large or infinite collections of data to work with

======


def read_large_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line

for line in read_large_file("large_file.txt"):
    process_line(line)

    
In this example, the read_large_file generator function takes a file path as an argument and opens the file using a with statement. It then uses a for loop to iterate over the file line by line, using the yield statement to return each line as it is read. The yield statement allows the function to return a value without exiting, so that it can continue reading the file and yield the next line on the next iteration.

As you iterate over the generator, it reads the file one line at a time, so it doesn't have to load the entire file into memory at once. This is more memory efficient than loading the entire file into memory and then iterating over it.


Example of same functionality using iterators. 
=====

class FileIterator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        return line

it = FileIterator("large_file.txt")
for line in it:
    process_line(line)

 ======

In this example, we defined a class FileIterator that takes a file path as an argument and opens the file in its constructor. The __iter__ method returns the iterator object itself, which is self, and the __next__ method reads the next line from the file and returns it. If there are no more lines to read, it closes the file and raises a StopIteration exception to indicate the end of the iteration.

As you can see, this implementation uses more memory as it loads the entire file in memory, so it is less memory efficient compared to the generator function.
