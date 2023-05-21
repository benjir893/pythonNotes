#!/usr/bin/env python
# coding: utf-8

# In[6]:


a = int(input("value1 : "))
b = int(input("value2 : "))

def addition(a,b):
    z = a + b
    return z


def substruction(a,b):
    z = a - b
    return z

def multiplication(a,b):
    z = a*b
    return z

def division(a,b):
    z = a/b
    return z

print(addition(a,b))
print(substruction(a,b))
print(multiplication(a,b))
print(division(a,b))


# In[11]:


n1 = int(input("value1 : "))
n2 = int(input("value2 : "))

def addition(a,b):
    z = a + b
    return z


def substruction(a,b):
    z = a - b
    return z

def multiplication(a,b):
    z = a*b
    return z

def division(a,b):
    z = a/b
    return z

desire = int(input(' enter 1 for addition\n enter 2 for substruction\n enter 3 multiplication \n enter 4 for division\n '))
if desire ==1:
    addition(n1,n2)
    print('Addition of two numbers is : ',addition(n1,n2))
elif desire ==2:
    substruction(n1,n2)
    print('Substruction of two numbers is : ',substruction(n1,n2))
elif desire ==3:
    multiplication(n1,n2)
    print('Multiplication of two numbers is : ',multiplication(n1,n2))
elif desire ==4:
    if n2> 0:
        division(n1,n2)
    else:
        print("Undefined")
else:
    print(" select from the option given.\n Thank you")
    


# In[ ]:




