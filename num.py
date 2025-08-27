n = 5
for row in range(1,n+1):
    for col in range(1,row+1):
        if(col%2==0):
            print('*' , end='')
        else:
            print(col, end='')
    print()