#!/usr/bin/env python
# coding: utf-8

# In[40]:


data = list(map(int,input('enter the list').split()))

print('you have entered: ',data)
print()
print('To add/edit the list choose options from the list \n',
'press 1 to add data end of the list\n',
     'To pop out data press 2\n',
     'To insert data press 3\n','To remove data press 4')    
option = int(input())
if option == 1:
    apel = int(input('enter the number : '))
    data.append(apel)
    print(data)
    print()
elif option == 2:
    popel = int(input('enter the index of the element :'))
    data.pop(popel)
    print(data)
    print()
elif option == 3:
    ensind = int(input('enter the index : '))
    enel = int(input('enter the value : '))
    data.insert(ensind,enel)
    print(data)
    print()
    
elif option == 4:
    elrmv = int(input('enter the value to remove : '))
    data.remove(elrmv)
    print(data)
    print()


        


# 
