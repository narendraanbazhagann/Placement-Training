import re
check=str(input("Enter your mail-id : "))
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
if re.match(pattern, check):
    print("Valid Email")
else:
    print("Invalid Email")
