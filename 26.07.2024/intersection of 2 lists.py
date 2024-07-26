def intersect_lists(list1, list2):
    return list(set(list1) & set(list2))

print(intersect_lists([1, 2, 3], [3, 4, 5]))  
