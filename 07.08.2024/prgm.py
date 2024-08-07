s = int(input("Enter the size: "))
alpha = 65
for i in range(s):
    for j in range(i):
        print(" ", end="")
    count = 0
    for k in range(0, 2 * (s - i) - 1):
        if k == 0 or k == 2 * (s - i) - 2:
            print(chr(count+alpha), end="")
            count += 1
        else:
            if i == 0:
                print(chr(count+alpha), end="")
                count += 1
            else:
                print(" ", end="")
    print()
