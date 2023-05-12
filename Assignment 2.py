#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Create an empty list
data_list = []


# In[2]:


# Enter the five numbers
1,2,3,4,5


# In[4]:


# Append the number to the list
for i in range(5):
    num = float(input('Enter a number:'))
    data_list.append(num)


# In[6]:


# Print the original 'data_list'
print("Original list:", data_list)


# In[7]:


# Sort the list in ascending order and print it
data_list.sort()
print("sorted list:", data_list)


# In[8]:


# Calculate and print the sum, mean and median of the number in the list
sum_list = sum(data_list)
mean_list = sum_list / len(data_list)


# In[11]:


if len(data_list) % 2 == 0:
    median_list = (data_list[len(data_list)//2] + data_list[len(data_list)//2 - 1]) / 2
else: 
    median_list = data_list[len(data_list)//2]


# In[12]:


print("sum:", sum_list)


# In[13]:


print("mean:", mean_list)


# In[14]:


print("median:", median_list)


# In[15]:


# Remove the first and last element from the 'data_list' and print the modified list
data_list.pop(0)


# In[16]:


data_list.pop()


# In[17]:


print("modified list:", data_list)


# In[ ]:




