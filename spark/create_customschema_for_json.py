#!/usr/bin/env python
# coding: utf-8

# In[9]:


from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('somerandomname').getOrCreate()


# In[2]:


from pyspark.sql.types import (StructField,StringType,IntegerType,StructType)


# In[6]:


data_schema=[StructField('firstName',StringType(),True),
             StructField('lastName',StringType(),True),
             StructField('gender',StringType(),True),
             StructField('age',IntegerType(),True)]


# In[7]:


final_struc =StructType(fields=data_schema)


# In[13]:


df=spark.read.json('sample.json',schema=final_struc)


# In[10]:


df=spark.read.json('sample.json',schema=final_struc)


# In[11]:


df.printSchema()


# In[12]:


df.show()


# In[ ]:




