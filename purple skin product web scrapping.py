#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


URL='https://www.purplle.com/skin/mom-baby'
URL


# In[3]:


r=requests.get(URL)
htmldata=r.content
htmldata


# In[4]:


soup=BeautifulSoup(htmldata,'html.parser')
soup.prettify


# In[5]:


title=soup.find_all(class_="pro-name el2 fanB")
print(title)


# In[44]:


Name=[]
for i in range (0,26):
    Name.append(title[i].get_text())
print(Name)


# In[7]:


price=soup.find_all(class_="tx-0 f14 f18-d fanB")
print(price)


# In[46]:


sellprice=[]
for i in range (0,26):
    sellprice.append(price[i].get_text())
print(sellprice)


# In[18]:


mp=soup.find_all(class_="tx-del mrl3 fanR fanM-d ng-star-inserted")
print(mp)


# In[47]:


MRP=[]
for i in range(0,26):
    MRP.append(mp[i].get_text())
print(MRP)


# In[11]:


Rev=soup.find_all(class_="tx-med1 mrl5 f10 fanB f13-d ng-star-inserted")
print(Rev)


# In[48]:


Rev_count=[]
for i in range (0,26):
    Rev_count.append(Rev[i].get_text())
print(Rev_count)


# In[13]:


str=soup.find_all(class_="listTheme tr-box bg-green2i ng-star-inserted")
print(str)


# In[35]:


star=[]
for i in range(0,len(str)):
    star.append(str[i].get_text())
print(star)
len(star)


# In[15]:


dis=soup.find_all(class_="tx-Grn fanR mrl3 fanM-d")
print(dis)


# In[40]:


Discount=[]
for i in range(0,26):
    Discount.append(dis[i].get_text())
print(Discount)


# In[42]:


SKIN_Product=pd.DataFrame({"Product_Name":Name,"Price":sellprice,"MRP":MRP,"DISCOUNT":Discount,"Reviews_count":Rev_count,"Review_Stars":star},index=range(1,27))
print(SKIN_Product)


# In[43]:


import os
os.getcwd()
SKIN_Product.to_csv("SKIN_Product.csv",index=False)
a=pd.read_csv("SKIN_Product.csv")
a

