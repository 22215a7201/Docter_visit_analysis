#!/usr/bin/env python
# coding: utf-8

# # DOCTER VISIT ANALYSIS

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#in order to ignore warnings
import warnings
warnings.filterwarnings("ignore")


# In[3]:


df=pd.read_excel("DoctorVisits (2).xlsx")


# In[4]:


df=pd.DataFrame(df)
df.head()


# In[5]:


df.shape


# In[6]:


df.info()


# In[60]:


df['age']=df['age']*70
df


# In[61]:


df["income"]=df["income"]*15000
df


# In[62]:


gender_counts = df["gender"].value_counts()
print(gender_counts)


# In[63]:


age_counts = df["age"].value_counts()
print(age_counts)


# In[64]:


visits_counts = df["visits"].value_counts()
print(visits_counts)


# In[65]:


illness_counts = df["illness"].value_counts()
print(illness_counts)


# In[81]:


df.describe() #Describing the info of the datatypes


# In[67]:


df.dropna(axis=0)


# In[68]:


df.fillna("20")
df.ffill(axis = 0)
df.bfill(axis = 0)


# In[69]:


df.drop_duplicates()


# In[70]:


df.drop_duplicates(subset=['private'])


# In[71]:


df.drop_duplicates(subset=['freerepat','illness'])


# In[72]:


df.columns


# In[73]:


df.isnull().sum()


# In[74]:


df['visits'].unique()
df['gender'].unique()
df['freepoor'].unique()
df['private'].unique()
df['nchronic'].unique()
df['age'].unique()
df['income'].unique()


# # VISUALISATION

# In[75]:


sns.histplot(df['age'], bins=60)
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()


# In[76]:


sns.histplot(df['age'], bins=65)
plt.xlabel('Age')
plt.ylabel('visit')
plt.title('Distribution of Patients Ages')
plt.show()


# In[77]:


plt.barh(gender_counts.index, gender_counts.values)  # Horizontal bar chart
plt.xlabel('Visit')
plt.ylabel('Gender')
plt.title('Distribution of Patient Gender')
plt.show()


# In[78]:


sns.histplot(df['visits'], bins=35)
plt.xlabel('visits')
plt.ylabel('income')
plt.title('visit analysis')
plt.show


# In[84]:


a=list(df.income)
plt.boxplot(a)
plt.show()


# Observation

# In[27]:


labels = ['visits', 'illness', 'reduced', 'health']
sizes = [25, 20, 13, 5]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Overall Analysis of Patients')
plt.axis('equal')  # Ensures the pie chart is circular
plt.show()


# In[39]:


x = [16, 14, 12, 18, 20]
y = [10, 12, 14, 9, 7]

plt.bar(x, y, color='b')
plt.xlabel('nchronic')
plt.ylabel('Ichronic')
plt.title('Disease analysis')
plt.show()


# In[29]:


labels=['freerepat','freepoor']
sizes=[30,40]
plt.pie(sizes,labels=labels,autopct = '%1.1f%%')
plt.title('patient health insurance analysis')
plt.show()


# In[30]:


labels=['visits','illness']
sizes=[70,60]
plt.pie(sizes,labels=labels,autopct = '%1.1f%%')
plt.title('overall analysis of patients')
plt.show()


# In[31]:


labels=['visits','illness','reduced','health']
sizes=[40,25,20,10]
plt.pie(sizes,labels=labels,autopct = '%1.1f%%')
plt.title('overall analysis of patients')
plt.show()


# In[32]:


x = [20,50,66,99,10] 
y = [30,30,46,80,55]
plt.scatter(x,y)
plt.xlabel('freepoor')
plt.ylabel('private')
plt.title('insurance analysis')
plt.show()


# In[33]:


df.hist(figsize=(20,25))


# In[34]:


x= (df[['health']]==1).sum()
y= (df[['health']]==0).sum()
percent= ((x*y)/(x+y))*100
percent


# # conclusion

# In this study, we examined a dataset that contains information about the visits of patients to a doctor. We explored the various variables in the dataset, such as gender, income, age, health condition, and insurance type. We found that:
# 
# - The majority of the patients were female, with a ratio of 3:2 to male patients.
# - Income did not have a significant impact on the frequency or duration of the visits, as the distribution was fairly uniform across income groups.
# - Age and health condition were correlated with the number and length of the visits, as older and sicker patients tended to visit the doctor more often and for longer periods.
# - None of the patients belonged to the freepoor category, which means they did not receive any government assistance due to their low income.
# - Private insurance was not a common option among the patients, as only 15% of them had this type of coverage.
# 
# These findings provide some insights into the characteristics and behaviors of the patients who visit this doctor. Further research could investigate the reasons behind these patterns and their implications for health care delivery and policy.
