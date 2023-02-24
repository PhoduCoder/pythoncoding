# #Given a list 
# # find all sublist

def sub_lists (l):
    lists = [[]]
    for i in range(len(l)+1):
        for j in range(i):
            #print (f"The values are {i} and {j}")
            #print ('The values are {} and {}'.format(i,j))
            lists.append(l[j: i])
            print ( 'The list after {} iteration in {} outer loop'.format(j,i) )
            print (lists)
    return lists
 
# driver code
l1 = [1, 2, 3,4]
print(sub_lists(l1))








# given_list=[1,2,3]

# # All sublists are 
# # [], [1], [2], [3]
# # [1,2], [1,3], [2,3]
# # [1,2,3]

# #The number of sublist = pow(2,len(list))


# given_list_2=[1,2,3,4]
# length=4
# given_sublists = [],#len 0
# [1],[2],[3],[4] #len1
# [1,2],[1,3],[1,4] [2,3], [2,4], [3,4] #len 2
# [1,2,3],[1,2,4],[1,3,4], [2,3,4], #len 3
# [1,2,3,4] #len 4

# nested for loops
# 1st loop -> for i=0; 

