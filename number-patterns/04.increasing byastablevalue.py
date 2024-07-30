n=int(input("enter n :"))
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end=' ')
    p+=2
    print()

#in this way any star pattern can be made 