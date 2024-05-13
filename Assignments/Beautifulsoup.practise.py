#!/usr/bin/env python
# coding: utf-8

# # Beautiful soup practise assigment

# # First Install Libraries

# In[37]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[38]:


from bs4 import BeautifulSoup
import requests


# Ques1- Write a python program to display all the header tags from wikipedia.org.

# In[39]:


page=requests.get('https://www.wikipedia.org/')
page


# In[40]:


Soup=BeautifulSoup(page.content)
Soup


# In[41]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


# In[42]:


url = "https://en.wikipedia.org/wiki/Main_Page"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
header_tags = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
header_text = [tag.text for tag in header_tags]
df = pd.DataFrame(header_text, columns=["Header Tags"])


# In[43]:


df


# Question2-Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year
# of release) and make data frame.

# In[44]:


link='https://www.imdb.com/chart/top/'


# In[45]:


pager=requests.get('https://www.imdb.com/chart/top/', headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})


# In[46]:


pager


# In[47]:


##display the source code
pager.content


# In[48]:


Soup=BeautifulSoup(pager.content)
Soup


# In[62]:


movies= Soup.find('li',class_="ipc-metadata-list-summary-item").h3.text


# In[55]:


print(movies)


# In[108]:


moviess= Soup.find('li',class_="ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent").find_all('div',class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN cli-title")


# In[107]:


len(moviess)


# In[103]:


moviess


# In[131]:


name=Soup.find('div',class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN cli-title").find_all('h3')


# In[132]:


name


# In[151]:


names=Soup.find('h3',class_="ipc-title__text").text


# In[152]:


names


# In[157]:


m=Soup.find('a',class_="ipc-title-link-wrapper").h3.text


# In[158]:


m


# In[160]:


na=[]
for i in Soup.find_all('a',class_="ipc-title-link-wrapper"):
    na.append(i.text)
na


# In[162]:


year=Soup.find('span',class_="sc-b189961a-8 kLaxqf cli-title-metadata-item")


# In[164]:


year.text


# In[181]:


year=[]
for i in Soup.find_all('span',class_="sc-b189961a-8 kLaxqf cli-title-metadata-item"):
    year.append(i.text)
    
year
len(year)


# In[169]:


print(len(na))


# In[172]:


rating=Soup.find('span',class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").text


# In[173]:


rating


# In[180]:


rating=[]
for i in Soup.find_all('span',class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"):
    rating.append(i.text)
    
rating
len(rating)


# In[175]:


import pandas as pd


# In[183]:


df=pd.DataFrame({'name':na,})


# In[184]:


df


# Ques 3-Write a python program to scrape mentioned details from dineout.co.in : i) Restaurant name 
# ii) Cuisine iii) Location iv) Ratings v) Image URL.

# In[198]:


page=requests.get('https://www.dineout.co.in/delhi-restaurants/welcome-back')
page


# In[199]:


soup=BeautifulSoup(page.content)
soup


# In[200]:


name=[]
for i in soup.find_all('div',class_="restnt-info cursor"):
    name.append(i.text)
name


# In[201]:


cuisine=[]
for i in soup.find_all('span',class_="double-line-ellipsis"):
    cuisine.append(i.text)
cuisine


# In[202]:


location=[]
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
location


# In[206]:


df=pd.DataFrame({'name':name,'cuisine':cuisine,'Location':location})


# In[207]:


df


# Ques4-Write s python program to display list of respected former finance minister of India(i.e. 
# Name , Term of office) from https://presidentofindia.nic.in/former-presidents.htm and make 
# data frame

# In[188]:


page=requests.get('https://presidentofindia.nic.in/former-presidents')
page


# In[189]:


soup=BeautifulSoup(page.content)
soup


# In[192]:


names=soup.find('div',class_="desc-sec").text


# In[193]:


names


# In[195]:


name=[]
for i in soup.find_all('div',class_="desc-sec"):
    name.append(i.text.replace('\n',''))
name


# In[196]:


df=pd.DataFrame({'name':name})


# In[197]:


df


# In[ ]:





# In[ ]:





# In[ ]:




