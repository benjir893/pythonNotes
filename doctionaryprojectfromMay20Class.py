#!/usr/bin/env python
# coding: utf-8

# In[1]:


ecom = {
    "Mobile":{"samsun":4000, "Iphone":58000,"Xiomo":45000},
    "Men":{
        "footwear":["shoes","slipperes","Crocs"],
        "Clothes":("Tshits","Shirts"),
        "Watches":["Watches1","Watches2","Watches3"]
    },
    "women":{"footwear":["shoes","slipperes","Crocs"],
             "Clothes":("Tshits","Shirts"),
             "Jewellry":["j1","j2","j3",[70000,80000,90000]]},
    "Laptop":["HP","DELL","ACER"]
    
}
print('All keys and values from Mobile :',ecom["Mobile"])
print('Men-footwear-slippers : ',ecom["Men"]["footwear"][1])
print('Men-Clothes-shirts : ',ecom["Men"]["Clothes"][1])
print('Men-watches-watches2 : ',ecom["Men"]["Watches"][1])
print()
print('women footwear : ',ecom["women"]["footwear"][2])
print('women Clothes : ',ecom["women"]["Clothes"][1])
print('women jewellry : ',ecom["women"]["Jewellry"][0],' , ',ecom["women"]["Jewellry"][3])
print('Laptop : ',ecom["Laptop"][1])


# In[ ]:




