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


# # --------------------------------
# # Linear regression custom example

# In[44]:


from pyspark.sql import SparkSession


# In[46]:


spark=SparkSession.builder.appName('customlinearreg').getOrCreate()


# In[47]:


from pyspark.ml.regression import LinearRegression


# In[48]:


data=spark.read.csv('linear_reg.csv',inferSchema=True,header=True)


# In[49]:


data.printSchema()


# In[51]:


data.head(1)[0].asDict()


# In[53]:


#setup data frame for ML
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler


# In[55]:


data.columns


# In[56]:


#you take list of input column which are a list of columns.
#you have a output column which is a feature ,can be named anything.
#VectorAssembler grabs all the columns and turns them into a single vector.
assembler=VectorAssembler(inputCols=[
 'Avg Session Length',
 'Time on App',
 'Time on Website',
 'Length of Membership'],
 outputCol='features')


# In[57]:


output=assembler.transform(data)


# In[59]:


#has new features column
output.printSchema()


# In[61]:


output.head(1)[0].asDict()


# In[62]:


final_data=output.select('features','Yearly Amount Spent')


# In[63]:


final_data.show()


# In[64]:


train_data,test_data=final_data.randomSplit([0.7,0.3])


# In[66]:


train_data.describe().show()


# In[67]:


test_data.describe().show()


# In[68]:


lr=LinearRegression(labelCol='Yearly Amount Spent')


# In[69]:


lr_model=lr.fit(train_data)


# In[70]:


test_results=lr_model.evaluate(test_data)


# In[73]:


test_results.residuals.show()


# In[75]:


test_results.rootMeanSquaredError


# In[76]:


test_results.r2


# In[77]:


final_data.describe().show()


# In[78]:


unlabeled=test_data.select('features')


# In[79]:


unlabeled.show()


# In[83]:


predictions=lr_model.transform(unlabeled_data)


# In[89]:


predictions.show()


# In[ ]:




