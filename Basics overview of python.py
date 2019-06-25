#!/usr/bin/env python
# coding: utf-8

# In[2]:


#basics of python
#this is single line comment
'''this is multi line comment'''


# In[4]:


#input in python
input("enter the value")


# In[5]:


#output
print("hi i am the basics of python")


# In[31]:


# "=" assignment opperator
c=2
d=2.4
bollean=True
e="thjis isw string"
f=[1,1,1,3,"shiv"] #list
f[0]=21
f[2]=32
g=[1,2,3,4]    #array=similar type of data in the list
tup=(1,1,2,3,"shiv")
sets={1,1,2}



#types  of variables
print(c,d,f,sets) #concatenation
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(tup))
print(type(sets))
print(type(bollean))


# In[32]:


#mathe maticss operators
a1=2
a2=2
print(a1+a2)
print(a1-a2)
print(a1*a2)
print(a1/a2)
print(a1**a2)#power operators 
print(a1//a2)#print integer value
print(a1==a2)#comparisson operators
print(a1!=a2)
print(a1<=a2)
print(a1>=a2)


# In[38]:


#conditional operators
a1=2
a2=3
if (a1>a2):
    print("false")
else:
    print("true")


# In[53]:


#for loop =itteration=repetition
sum=0
for i in range(100):
    #print(i)
    sum=sum+i
   #print(i,end=",  ")
print("\n",sum)


# In[ ]:




