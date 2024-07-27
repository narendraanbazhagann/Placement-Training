from collections import Counter

def most_frequent_element(lst):
    count = Counter(lst)
    return count.most_common(1)[0][0]

lst = [1, 2, 3, 2, 4, 2, 5]
print(f"The most frequent element is: {most_frequent_element(lst)}")
