n=int(input("enter n :"))
k=n
for i in range(n):
    p=k
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n):
        print(p,end=' ')
        p-=1
    k-=1
    print()
