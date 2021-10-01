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


# In[14]:


df.withColumn('double_age',df['age']*2).show()


# In[18]:


df.withColumnRenamed('age','newage').show()


# In[19]:


df.show()


# In[20]:


df.createOrReplaceTempView('people')


# In[21]:


res=spark.sql("select * from people")


# In[22]:


res.show()


# In[23]:


res=spark.sql("select * from people where age=30")


# In[24]:


res.show()


# In[ ]:




