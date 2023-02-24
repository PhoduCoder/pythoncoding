#Count pair of similar string
#given an input of list of array

li=["aba","aabb","abcd","bac","aabc"]

match_list=[]
for i in range(len(li)):
    my_dict=set(li[i])
    match_list.append(my_dict)

print (match_list)
count=0
for i in range(len(match_list)):
    for j in range(len(match_list[i:])):
        if (match_list[i]==match_list[j]):
            print (match_list[i])
            print (match_list[j])
            print ("End of iteration", j)
            print ("======Inner====")
            count+=1
    #print(match_list[i])
    print ("===Outer=====")
    print ("end of iteration", i)
print (count) 

