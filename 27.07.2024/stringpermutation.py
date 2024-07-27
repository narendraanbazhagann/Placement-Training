def permutations(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
if permutations(str1, str2):
    print(f"{str1} and {str2} are permutations of each other.")
else:
    print(f"{str1} and {str2} are not permutations of each other.")
