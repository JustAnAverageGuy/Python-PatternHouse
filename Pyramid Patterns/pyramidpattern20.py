print("Enter the number of rows: ")
n = int(input())
spaces = n + (n - 1)
counter = 1
f = 1
for i in range(0, n):
    for k in range(0, spaces):
        print(" ", end="")
    for j in range(0, counter):
        print(f, end=" ")
        f = f + 1
    counter = counter + 2
    print()
    spaces = spaces - 2
