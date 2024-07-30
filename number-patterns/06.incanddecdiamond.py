n=int(input("enter n :"))
p=1
for i in range(n):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i+1):
        print(p,end=' ')
    for j in range(i):
        print(p,end=' ')
    p+=1
    print()
p=p-2
for i in range(n):
    for j in range(i+2):
        print(" ",end=' ')
    for j in range(i+2,n):
        print(p,end=' ')
    for j in range(i,n-1):
        print(p,end=' ')
    p-=1
    print()
