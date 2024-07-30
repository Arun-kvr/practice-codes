'''print("*")
n=5
print("*"*n)
print("* "*n)

n=5
for i in range(n):
    print("*")
for j in range(n):
    print("*",end='')
'''
n=5
for i in range(n):
    for j in range(n):
        print("*",end=' ')
    print()