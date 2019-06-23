#!/usr/bin/env python
# coding: utf-8

# ARMSTRONG
# 

# In[4]:


num =int(input())
sum=0
d=num

while num!=0:
    rem=int(num%10)
    sum=sum+(rem**3)
    
    num=num//10
    
if sum==d:
    print(d," =IT is armstrong")
else:
    print("IT is not armstronh=",d)


# armstrong bteween 1-1000

# In[7]:


for i in range(1,1000):
    num=i
    sum=0
    d=num

    while num!=0:
        rem=int(num%10)
        sum=sum+(rem**3)

        num=num//10

    if sum==d:
        print(d," =IT is armstrong")
    else:
        print(end="")


# factorial

# In[17]:


num=int(input())
s=num
for i in range(1,num):
    s=s*i
print(s)


# sum of natural numbers

# In[20]:


sum=0
for i in range (1,100):
    sum=sum+i
print(sum)


# Multiplication table

# In[28]:


num=int(input())
for i in range(1,11):
     print(num,"*",i,"=",num*i)
    


# 2D list

# In[34]:


input_string=input("Enter the sting=")
list = input_string.split()
print("calculate the sum in list")
sum=0
for i in list:
    sum=sum+int(i)
print("sum=",sum)


# In[54]:



row=int(input("Enter the number of rows="))
col=int(input("Enter the number of cols="))

nmat=[[int(input()) for j in range(col)]for i in range(row)]
nmat


# In[55]:


mat=[[j for j in range(3)]for i in range(7)]
print(mat)


# In[ ]:




