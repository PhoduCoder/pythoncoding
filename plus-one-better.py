#Plus one Problem

def plusone(list_num):
    #calculate the length of string
    length=len(list_num)

    #Use a while loop 
    # to travel through list [This should give you hint that we will be decreasing the value of n in every iteration]
    while length>0:
        #if the last digit is 9
        if(list_num[length-1]) == 9:
            # if the list contains only one number
            if length==1:
                list_num[length-1]=0
                temp = [1]+list_num
                return temp
            else:
                list_num[length-1]=0
                length-=1
        else:
            list_num[length-1] = list_num[length-1]+1
            return list_num

#given_list=[1,2,3,4,9]
#given_list=[9]
given_list=[9,9,9,9]

plusone_num=plusone(given_list)

print (plusone_num)
