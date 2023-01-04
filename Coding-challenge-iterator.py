class Sentence:
    
    def __init__(self, sentence):
        self.sentence = sentence
        #Now because iterators need to remember their
        #state so we define another variable
        # called index
        self.index = 0
        self.words = self.sentence.split()
  
    def __iter__(self):
        return self
        #because remember for a class 
        # to be iterable, it has to have 
        # an __iter__ method
        # and that __iter__method 
        # has to return an object
        # that has a __next__ method

    def __next__(self):
        #this should return each word
        # in the passed sentence
        print("From the next function")
        # The next method should 
        # raise a StopIteration Exception
        # once the looping is finished
        if (self.index >= len(self.words)):
            raise StopIteration
        index = self.index # Remembering the state 
        self.index += 1 
        return self.words[index]

my_sentence = Sentence("This is a new sentence")

print (dir(my_sentence))

print (next(my_sentence))

#for word in my_sentence:
#    print (word)


#for word in my_sentence:
#    print (word)

#Output should be
# like each word 
# with a new line character
#this
#is
#a 
#sentence

#==============
# Doing the same via generators function
# is much more simpler
# because we no longer have to 
# define the iter and next methods
# generator takes care of that
# neither raising the stopIteration Exception

def sentence(sentence):
    for word in sentence.split():
        yield word

my_decorator_sentence = sentence("This is through decorator")

for word in my_decorator_sentence:
    print (word)
