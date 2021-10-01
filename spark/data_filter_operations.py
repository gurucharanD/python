#!/usr/bin/env python
# coding: utf-8

# In[9]:


from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('somerandomname').getOrCreate()


# In[25]:


df=spark.read.csv('sample.csv',inferSchema=True,header=True)


# In[26]:


df.printSchema()


# In[27]:


df.show()


# In[28]:


df.head(3)


# In[31]:


df.head(2)[0]


# In[35]:


df.filter('year>2017').show()


# In[38]:


df.filter('year>2016').select(['year','Industry_aggregation_NZSIOC']).show()


# In[41]:


# data frame syntax
df.filter(df['year']<2017).select(['year']).show()


# In[44]:


df.filter((df['year']<2017) & (df['Value']>300000)).select(['year','Value']).show()


# In[46]:


df.filter(df['year']==2017).show()


# In[47]:


# returns data as list
res=df.filter(df['year']==2017).collect()


# In[49]:


res


# In[50]:


res[0]


# In[51]:


res[0].asDict()


# In[52]:


res[0].asDict()['Value']


# In[ ]:




