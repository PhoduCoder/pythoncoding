code = [1,2,3,4]
import copy
shal_copy = copy.copy(code) 
print (shal_copy)
[1, 2, 3, 4]
print (id(shal_copy), id(code))
140679226593536 140679226526208 
deep_copy = copy.deepcopy(code)
>>> 
>>> print (id(shal_copy), id(code), id(deep_copy))
140679226593536 140679226526208 140679226579072