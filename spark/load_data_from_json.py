#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession


# In[6]:


spark = SparkSession.builder.appName('somerandomname').getOrCreate()


# In[21]:


df = spark.read.json('sample.json')


# In[22]:


df.printSchema()


# In[23]:


df.show()


# In[24]:


df.columns


# In[25]:


df.describe()


# In[26]:


df.describe().show()


# In[28]:


from pyspark.sql.types import (StructField,
                               StringType,
                               IntegerType,
                               StructType)


# In[ ]:




