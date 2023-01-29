#Shuffle string 

def shuffle_string(s, indices):
    shuffled=[]
    for i in range(len(indices)):
        ele=indices[i]
        shuffled.append(s[ele:(ele+1)])
    return shuffled

s = "codeleet"
indices = [4,5,6,7,0,1,2,3]

shuffled_str=shuffle_string(s,indices)
returned_string="".join(shuffled_str)
print (returned_string)
