def merge_lists(list1, list2):

    index_list1 = 0
    index_list2 = 0
    sorted_list = []
    while (index_list1<= len(list1)-1 and index_list2 <= len(list2)-1):

        if list1[index_list1] < list2[index_list2]:
            sorted_list.append(list1[index_list1])
            index_list1 += 1
        elif list1[index_list1] == list2[index_list2]:
            sorted_list.extend([list1[index_list1], list2[index_list2]])
            index_list1 += 1
            index_list2 += 1
        else:
            sorted_list.append(list2[index_list2])
            index_list2 += 1

    if index_list1 <= len(list1) -1:
        sorted_list.extend(list1[index_list1:])
    print (index_list2)
    print(len(list2))
    if index_list2 <= len(list2) -1:
        sorted_list.extend(list2[index_list2:])

    return sorted_list


my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]


merge_lists(my_list, alices_list)