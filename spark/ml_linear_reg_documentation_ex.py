#!/usr/bin/env python
# coding: utf-8

# #  linear regression documentation example

# In[1]:


from pyspark.sql import SparkSession


# In[2]:


spark=SparkSession.builder.appName('linearreg').getOrCreate()


# In[5]:


from pyspark.ml.regression import LinearRegression


# In[9]:


#load training data which is in libsvm format
trainingdata=spark.read.format('libsvm').load('linear_reg.txt')


# In[11]:


trainingdata.show()


# In[13]:


#create instance of our model
#parameters are taken from dataframe
lr=LinearRegression(featuresCol='features',labelCol='label',predictionCol='prediction')


# In[14]:


#training the model
lrModel=lr.fit(trainingdata)


# In[15]:


lrModel.coefficients


# In[16]:


lrModel.intercept


# In[17]:


training_summary=lrModel.summary


# In[18]:


training_summary.r2


# In[19]:


training_summary.rootMeanSquaredError


# In[20]:


#train and test data split
all_data=spark.read.format('libsvm').load('linear_reg.txt')


# In[25]:


#split dataframe into two dataframes randomly
#first one has 70% and 30% is in next
#below syntax is called tuple unpcking
train_data,test_data=all_data.randomSplit([0.7,0.3])


# In[32]:


train_data


# In[27]:


test_data


# In[33]:


train_data.describe().show()
test_data.describe().show()


# In[34]:


correct_model=lr.fit(train_data)


# In[35]:


test_results=correct_model.evaluate(test_data)


# In[36]:


test_results.residuals.show()


# In[37]:


test_results.rootMeanSquaredError


# In[38]:


#using evaluate on test data,we are comparing predictions on labels that are already assigned in test data


# In[39]:


#deploying model on unlabeld data
unlabeled_data= test_data.select('features')


# In[40]:


unlabeled_data.show()


# In[41]:


predictions=correct_model.transform(unlabeled_data)


# In[42]:


predictions.show()


# In[43]:


#our model predicted the labels


# In[ ]:




