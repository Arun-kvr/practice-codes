#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("enter n :"))
for i in range(n):
    for j in range(i+1):
        print("A",end=' ')
    print()


# In[2]:


n= int(input("enter n :"))
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=' ')
    p+=1
    print()


# In[3]:


n=int(input("enter n :"))
p=69
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=' ')
    p-=1
    print()


# In[4]:


n= int(input("enter n :"))
p=65+n-1
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=' ')
    p=p-1
    print()


# In[5]:


n=int(input("enter n :"))
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=' ')
    p+=2
    print()


# In[6]:


n=int(input("enter n :"))
for i in range(n):
    for j in range(i+1):
        if i%2==0:
            print("A",end=' ')
        else:
            print("B",end=' ')
    print()


# In[7]:


n=int(input("enter n :"))
for i in range(n):
    for j in range(i,n):
        if i%2==0:
            print("A",end=' ')
        else:
            print("B",end=' ')
    print()


# In[8]:


n=int(input("enter n :"))
p=65
for i in range(n):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i):
        print(chr(p),end=' ')
    for j in range(i+1):
        print(chr(p),end=' ')
    p+=1
    print()
for i in range(n):
    for j in range(i+2):
        print(" ",end=' ')
    for j in range(i+1,n-1):
        print(chr(p),end=' ')
    for j in range(i+1,n):
        print(chr(p),end=' ')
    p+=1
    print()


# In[9]:


n=int(input("enter n :"))
p=65
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i):
        print(chr(p),end=' ')
    for j in range(i+1):
        print(chr(p),end=' ')
    p+=1
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i+1,n):
        print(chr(p),end=' ')
    for j in range(i,n):
        print(chr(p),end=' ')
    p+=1
    print()


# In[10]:


n=int(input("enter n :"))
p=65
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i):
        print(chr(p),end=' ')
    for j in range(i+1):
        print(chr(p),end=' ')
    p+=1
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n-1):
        print(chr(p),end=' ')
    for j in range(i,n):
        print(chr(p),end=' ')
    p-=1
    print()


# In[11]:


n=int(input("enter n :"))
for i in range(n):
    p=65
    for j in range(i+1):
        print(chr(p),end=' ')
        p+=1
    print()


# In[12]:


n=int(input("enter n :"))
for i in range(n):
    p=65
    for j in range(i,n):
        print(chr(p),end=' ')
        p+=1
    print()


# In[13]:


n=int(input("enter n :"))
for i in range(n):
    p=65
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n):
        print(chr(p),end=' ')
        p+=1
    print()


# In[14]:


n=int(input("enter n :"))
for i in range(n):
    p=65
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i):
        print(chr(p),end=' ')
        p+=1
    for j in range(i+1):
        print(chr(p),end=' ')
        p+=1
    print()


# In[15]:


n=int(input("enter n :"))
for i in range(n):
    p=65+n-1
    for j in range(i,n):
        print(chr(p),end=' ')
        p-=1
    print()


# In[16]:


n=int(input("enter n :"))
for i in range(n):
    p=65
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i):
        print(chr(p),end=' ')
        p+=1
    for j in range(i+1):
        print(chr(p),end=' ')
        p-=1
    print()


# In[17]:


s="coder"
n=len(s)
k=0
for i in range(n):
    for j in range(i+1):
        print(s[k],end=' ')
    k+=1
    print()


# In[18]:


s="coder"
n=len(s)
p=n-1
for i in range(n):
    for j in range(i+1):
        print(s[p],end=' ')
    p-=1
    print()


# In[19]:


s="coder"
n=len(s)
for i in range(n):
    p=0
    for j in range(i+1):
        print(s[p],end=' ')
        p+=1
    print()


# In[20]:


s="coder"
n=len(s)
for i in range(n):
    p=0
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i+1):
        print(s[p],end=' ')
        p+=1
    print()


# In[21]:


s="coder"
n=len(s)
for i in range(n):
    p=n-1
    for j in range(i+1):
        print(s[p],end=' ')
        p-=1
    print()


# In[22]:


s="coder"
n=len(s)
k=n-1
for i in range(n):
    p=k
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n):
        print(s[p],end=' ')
        p-=1
    print()
    k-=1


# In[ ]:




