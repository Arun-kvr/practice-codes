n=int(input("enter n :"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

for i in range(n-1,0,-1):
        for j in range(1,i+1):
            print(j,end=' ')
        for j in range(i,n):
            print(" ",end=' ')
        for j in range(i,n):
            print(" ",end=' ')
        for j in range(i,0,-1):
            print(j,end=' ')
        print()