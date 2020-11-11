#!/usr/bin/env python
# coding: utf-8

# In[3]:


def Game(player1, player2) :
    if str(player1) == '가위' :
        if str(player2) == '바위' : print("player2")
        elif str(player2) == '보' : print("player1")
        else : Game(player1, player2)
    if str(player1) == '바위' :
        if str(player2) == '가위' : print("player1")
        elif str(player2) == '보' : print("player2")
        else : Game(player1, player2)
    if str(player1) == '보' :
        if str(player2) == '가위' : print("player2")
        elif str(player2) == '바위' : print("player1")
        else : Game(player1, player2)#1


# In[4]:


Game('가위','보')


# In[4]:


#2


# In[6]:


def Fac(fac_number) :
    factorial = 1
    while fac_number > 0 :
        factorial = factorial * fac_number
        fac_number = fac_number - 1
    print(factorial)


# In[8]:


Fac(10)


# In[9]:


#3


# In[14]:


def avg_all(*args) :
    result = 0
    for i in args :
        result = result + i
    avg = result / len(args)
    print(float(avg))


# In[15]:


avg_all(2123,12619,1297426,191)


# In[ ]:




