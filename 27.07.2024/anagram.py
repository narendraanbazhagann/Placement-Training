def anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
if anagrams(str1, str2):
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not anagrams.")
