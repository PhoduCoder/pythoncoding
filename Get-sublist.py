def get_sublist(given_list):
    length=len(given_list)
    sub_lists=[[]]

    for i in range(length+1):
        for j in range(i):
            sub_lists.append(given_list[j:i])
    return sub_lists

given_list=[1,2,3,4,5]
sub_lists = get_sublist(given_list)

print (sub_lists)