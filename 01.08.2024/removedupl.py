lst = [int(x) for x in input("Enter numbers separated by space: ").split()]
unique_lst = list(set(lst))
print("List without duplicates:", unique_lst)
