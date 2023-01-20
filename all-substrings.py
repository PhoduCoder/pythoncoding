#Given a string
# print all the valid substrings

def substring_func(input):
  substrings=[]
  for i in range(len(input)):
    for j in range(i+1, len(input)+ 1): 
      substrings.append(input[i:j])
  return substrings
    

my_string=input('Enter the string\n')

result = substring_func(my_string)

print (result)
