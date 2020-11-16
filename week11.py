#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1


# In[8]:


def introduce() :
    num = str(input("학번을 입력해주세요. : "))
    name = str(input("이름을 입력해주세요. : "))
    f = open("week11.txt", "a", encoding = "UTF-8")
    f.write(num)
    f.write(" ")
    f.write(name)
    f.write("\n")
    f.close()


# In[9]:


introduce()


# In[10]:


introduce()


# In[11]:


#2


# In[12]:


def read_week11() :
    f = open("week11.txt", "r", encoding = "UTF-8")
    lines = len(f.readlines()) 
    return(lines)


# In[13]:


read_week11()


# In[ ]:




