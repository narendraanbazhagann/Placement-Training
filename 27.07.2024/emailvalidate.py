import re

def validemail(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

email = input("Enter an email address: ")
if validemail(email):
    print("The email address is valid.")
else:
    print("The email address is invalid.")
