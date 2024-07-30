n=int(input("enter n :"))
for i in range(n):
    for j in range(i+1):
        if i%2==0:
            print("1",end=' ')
        else:
            print("2",end=' ')
    print()

# in this way alternative number patterns can be printed for any star patterns
