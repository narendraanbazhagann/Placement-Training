from collections import Counter

def count_frequency(lst):
    return dict(Counter(lst))

print(count_frequency([1, 2, 2, 3, 3, 3]))  
