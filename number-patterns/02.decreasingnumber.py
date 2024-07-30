n=int(input("enter n :"))
p=n
for i in range(n):
    for j in range(i+1):
        print(p,end=' ')
    p-=1
    print()
#in this way any star pattern can be made in decreasing pattern