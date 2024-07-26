def sort_by_second_element(lst):
    return sorted(lst, key=lambda x: x[1])

print(sort_by_second_element([(1, 3), (2, 2), (3, 1)]))  
