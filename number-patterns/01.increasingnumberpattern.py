n=int(input("enter n :"))
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end=' ')
    p=p+1
    print()

#in this way any star pattern can be made in increasing pattern