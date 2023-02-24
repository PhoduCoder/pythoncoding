#Subsequence product less
# than a given number

def sub_list(li):
    new=[]
    for i in range(len(li)):
        new.append(li[i:])
    return new

li=[2,3,4,5]
all_sub=sub_list(li)

print (all_sub)
