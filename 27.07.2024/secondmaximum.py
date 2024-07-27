def seclargest(lst):
    first, second = float('-inf'), float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second

lst = [10, 20, 4, 45, 99]
print(f"The second largest number is: {seclargest(lst)}")
