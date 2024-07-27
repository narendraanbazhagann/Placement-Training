import random
import string

def genpass(l):
    c= string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(c) for i in range(l))
    return password

l = int(input("Enter the length of the password: "))
print(f"Generated password: {genpass(l)}")
