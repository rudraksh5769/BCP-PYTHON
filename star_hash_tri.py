n = 5
for i in range(n):
    for j in range(n-i+2):
        if (j==0 or j==n-i+1):
            print("*", end="")
        else:
            print("_", end="")
    print()