#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LinearRegression


# In[38]:


pip install -U scikit-learn


# In[39]:


# Linear Regression with single variable
df=pd.read_excel("C:/Users/Windows10/Documents/Book1.xlsx")
df


# In[40]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel('area(sqr ft)')
plt.ylabel('price(US)')
plt.scatter(df.area,df.price,color="red",marker="+")
plt.plot(df.area,reg.predict(df[['area']].values),color='blue')


# In[41]:


reg=linear_model.LinearRegression()
reg.fit(df[['area']].values,df.price)


# In[42]:


# to predict certain area price
reg.predict([[3500]])


# In[43]:


reg.coef_


# In[44]:


reg.intercept_


# In[45]:


#y=m*x+c
164.89726027*3500+75136.98630136985


# In[46]:


# Linear Regression with multiple variable
df2=pd.read_excel("C:/Users/Windows10/Documents/Book2.xlsx")
df2


# In[47]:


import math
median_bedrooms=math.floor(df2.bedrooms.median())
median_bedrooms


# In[48]:


df2.bedrooms=df2.bedrooms.fillna(median_bedrooms)
df2


# In[49]:


reg=linear_model.LinearRegression()
reg.fit(df2[["area","bedrooms","age"]].values,df2.price)


# In[50]:


reg.coef_


# In[51]:


reg.intercept_


# In[52]:


reg.predict([[3000,3,40]])


# In[53]:


3000*137.25+(-26025*3)+(-6825)*40+383724.9999999998


# In[54]:


# read the multiple independent variable data
df3=pd.read_excel("C:/Users/Windows10/Documents/Book3.xlsx")
df3


# In[55]:


pip install word2number


# In[56]:


df3.experience = df3.experience.fillna("zero")
df3


# In[57]:


from word2number import w2n
df3.experience=df3.experience.apply(w2n.word_to_num)


# In[58]:


import math
median_test_score = math.floor(df3['test_score'].mean())
median_test_score


# In[59]:


df3['test_score'] = df3['test_score'].fillna(median_test_score)
df3


# In[60]:


reg=linear_model.LinearRegression()
reg.fit(df3[['experience','test_score','interview_score']].values,df3['salary($)'])


# In[61]:


reg.predict([[2,9,6]])


# In[62]:


reg.predict([[12,10,10]])


# In[ ]:




