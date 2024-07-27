def decimalbinary(n):
    return bin(n).replace("0b", "")

number = int(input("Enter a decimal number: "))
print(f"The binary representation of {number} is: {decimalbinary(number)}")
