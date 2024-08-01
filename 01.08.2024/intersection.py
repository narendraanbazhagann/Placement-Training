list1 = [int(x) for x in input("Enter first list elements separated by space: ").split()]
list2 = [int(x) for x in input("Enter second list elements separated by space: ").split()]
list3 = [int(x) for x in input("Enter third list elements separated by space: ").split()]
intersection = list(set(list1) & set(list2) & set(list3))
print("Intersection:", intersection)
