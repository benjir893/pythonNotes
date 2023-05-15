#!/usr/bin/env python
# coding: utf-8

# In[3]:


Ecommerce = [
    "Mobiles",["Samsung","OnePlus","Iphone",[14000,20000,40000]],
    "Laptop",["Dell","Hp","Acer",[25000,35000,45000]],
    "Clothes",["Men","Women",[50,100]]
]
print(Ecommerce)


# In[4]:


print(len(Ecommerce))


# In[5]:


for row in Ecommerce:
    print(row)


# In[6]:


print(Ecommerce[1][0],"Mobile Price",Ecommerce[1][3][1],",",Ecommerce[1][3][2])
print(Ecommerce[3][1]," Price ",Ecommerce[3][3][1])
print(Ecommerce[5][0]," quantity ",Ecommerce[5][2][0])


# In[ ]:




