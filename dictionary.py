person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

#ssn=person['ssn']

#instead of getting a key error
#using get function gives none or default value 
ssn = person.get('ssn', '000-00-0000')

person['gender']="Male"
print (person)

print("==========")
#Looping through dictionary

#use dict_name.items() => returns all key,values

#use dict_name.values() => returns all values

# use dict_name.keys() => returns all keys
# in fact looping over keys is default behavior
# so you can avoid .keys()

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

for key in person:
    #print(key)
    print (person[key])