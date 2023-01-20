#Given a string 
#generate all substrings
# this time using generators

# note that there is no return statement in the function
# rather it just generates a new value when called

def get_substrings(string):
    for i in range(len(string)):
        for j in range(i+1, len(string) + 1):
            yield string[i:j]

string = "Shreya"
substrings = get_substrings(string)
print(list(substrings))

