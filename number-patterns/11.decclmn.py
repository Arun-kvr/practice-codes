n=int(input("enter n :"))
for i in range(n):
    p=n
    for j in range(i+1):
        print(p,end=' ')
        p-=1
    print()