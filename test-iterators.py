class test:
    def __init__(self, index):
        self.index = 2
        print ("My constructor")
    
    def __iter__(self):
        print ("This is from the iter method")
        return self

    def __next__(self):
        #index = 2
        if self.index <= 0:
            raise StopIteration
        print ("Am i qualified")
        self.index -= 1


test = test(0)

print (next(test))
print (next(test))
print (next(test))
