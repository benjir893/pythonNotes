#!/usr/bin/env python
# coding: utf-8

# In[ ]:


y=input('Does user have 4 wheeler ? please answer yes/no :')

if(y=='yes'):
    size = input('please enter the size of your pizza : small:medium:Large:Monster sizes : ')
    if(size == 'small' or size =='medium'or size =='large'or size =='monster'):
        qty=int(input('enter the quantity of pizza: '))
        if(size =='small'and qty>=4):
            print('500ml coke comes free with your order')
        else:
            print('you have order',qty,' pieces of ',size,' pizza')
        if(size == 'medium'and qty>=3):
            print("your order comes with 1ltr coke free")
        else:
            print('you have order',qty,' pieces of ',size,' pizza')
        if(size =='large'and qty>=2):
            print('your order comes with 1 ice cream and 500ml coke free')
        else:
            print('you have order',qty,' pieces of ',size,' pizza')
        if(size == 'monster'and qty>=1):
            print('your order comes with 1 small and 500ml coke free')
        else:
            print('you have order',qty,' pieces of ',size,' pizza')
    else:
        print('please enter sizes from the option')
        
        
    
elif(y=='no'):
    print('Sorry !! This service only for having four wheeler drive throu. Please order from the counter inside.Thank you')
else:
    print('Enter the correct answer..')

