#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[3]:


from bs4 import BeautifulSoup
import requests


# # Ques1- Write a python program to display IMDB’s Top rated 100 Indian movies’ data
# # https://www.imdb.com/list/ls056092300/ (i.e. name, rating, year ofrelease) and make data frame

# In[6]:


page=requests.get('https://www.imdb.com/list/ls056092300/',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})
page


# In[7]:


soup=BeautifulSoup(page.content)
soup


# In[5]:


movies=soup.find_all('div',class_="lister-item-content")


# In[8]:


movies


# In[9]:


Name=[]
for i in movies:
    name=i.find('h3',class_="lister-item-header").a.text
    Name.append(name)
Name


# In[10]:


Rank=[]
for i in movies:
        rank=i.find('h3',class_="lister-item-header").get_text(strip=True).split('.')[0]
        Rank.append(rank)
Rank


# In[11]:


Year=[]
for i in movies:
        year=i.find('h3',class_="lister-item-header").find('span',class_="lister-item-year text-muted unbold").text.strip('()')
        Year.append(year)
Year


# In[12]:


Rating=[]
for i in movies:
        rating=i.find('div',class_="ipl-rating-widget").find('span',class_="ipl-rating-star__rating").text
        Rating.append(rating)
Rating


# In[13]:


print(len(Name),len(Rank),len(Year),len(Rating))


# In[15]:


import pandas as pd
df=pd.DataFrame({'rank':Rank,'name':Name,'year':Year,'rating':Rating})
df


# # Question2-Write a python program to scrape product name, price and discounts from
# https://peachmode.com/search?q=bags

# In[16]:


page=requests.get('https://peachmode.com/collections/new-arrival')
page


# In[17]:


soup=BeautifulSoup(page.content)
soup


# In[23]:


product=[]
for i in soup.find_all('div',class_="product-title"):
    product.append(i.text)
product


# In[29]:


a=soup.find('div',class_="product-title")


# In[30]:


a


# In[31]:


price=soup.find('span',class_="discounted_price st-money money done")


# In[32]:


price


# DATA NOT FETCHING FROM ABOVE WEBSITE

# # Ques3-Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# b) Top 10 ODI Batsmen along with the records of their team and rating.
# c) Top 10 ODI bowlers along with the records of their team and rating.
# 

# UNABLE TO DO IT.I HAVE PROBLEM INTO IT.

# # Ques4-Write a python program to scrape details of all the posts from https://www.patreon.com/coreyms .Scrape the
# heading, date, content and the likes for the video from the link for the youtube video from the post.

# In[33]:


page=requests.get('https://www.patreon.com/coreyms')
page


# In[34]:


soup=BeautifulSoup(page.content)
soup


# In[35]:


heading=[]
for i in soup.find_all('div',class_="sc-bUbRBg DYKxE"):
    heading.append(i.text)
heading


# #DATA NOT FETCHING FROM THE CONTENT FROM THE ABOVE PATREON WEBSITE

# # Question 5-Write a python program to scrape house details from mentioned URL. It should include house title, location,
# # area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar,
# # Rajaji Nagar.

# In[36]:


page=requests.get('https://www.nobroker.in/property/sale/bangalore/multiple?searchParam=W3sibGF0IjoxMi45NzgzNjkyLCJsb24iOjc3LjY0MDgzNTYsInBsYWNlSWQiOiJDaElKa1FOM0dLUVdyanNSTmhCUUpyaEdEN1UiLCJwbGFjZU5hbWUiOiJJbmRpcmFuYWdhciJ9LHsibGF0IjoxMi45MzA3NzM1LCJsb24iOjc3LjU4MzgzMDIsInBsYWNlSWQiOiJDaElKMmRkbFo1Z1ZyanNSaDFCT0FhZi1vcnMiLCJwbGFjZU5hbWUiOiJKYXlhbmFnYXIifSx7ImxhdCI6MTIuOTk4MTczMiwibG9uIjo3Ny41NTMwNDQ1OTk5OTk5OSwicGxhY2VJZCI6IkNoSUp4Zlc0RFBNOXJqc1JLc05URy01cF9RUSIsInBsYWNlTmFtZSI6IlJhamFqaW5hZ2FyIn1d&radius=2.0&city=bangalore&locality=Indiranagar,Jayanagar,Rajajinagar')
page


# In[37]:


soup=BeautifulSoup(page.content)
soup


# In[38]:


house=soup.find_all('div',class_="p-1.5p flex border-b border-b-solid border-cardbordercolor tp:py-1p tp:px-1.5p tp:border-b-0")
Price=[]
for i in house:
    price=i.find_all('div',class_="font-semi-bold heading-6")[0].text
    Price.append(price)
Price


# In[39]:


Title=[]
for i in soup.find_all('h2',class_="heading-6 flex items-center font-semi-bold m-0"):
    Title.append(i.text)
Title


# In[40]:


Location=[]
for i in soup.find_all('div',class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0.1p po:max-w-95"):
    Location.append(i.text)
Location


# In[41]:


house=soup.find_all('div',class_="p-1.5p flex border-b border-b-solid border-cardbordercolor tp:py-1p tp:px-1.5p tp:border-b-0")
Emi=[]

for i in house:
    emi=i.find_all('div',class_="font-semi-bold heading-6")[1].text
    Emi.append(emi)
Emi


# In[42]:


house=soup.find_all('div',class_="p-1.5p flex border-b border-b-solid border-cardbordercolor tp:py-1p tp:px-1.5p tp:border-b-0")
Area=[]

for i in house:
    area=i.find_all('div',class_="font-semi-bold heading-6")[2].text
    Area.append(area)
Area


# In[43]:


(len(Area),len(Price),len(Emi),len(Title),len(Location))


# In[44]:


df=pd.DataFrame({'Title':Title,'Location':Location,'Price':Price,'Emi':Emi,'Area':Area})
df


# # 6) Write a python program to scrape first 10 product details which include product name , price , Image URL from
# # https://www.bewakoof.com/bestseller?sort=popular

# In[45]:


page=requests.get('https://www.bewakoof.com/bestseller?sort=popular%20.')
page


# In[46]:


soup=BeautifulSoup(page.content)
soup


# In[47]:


name=[]
for i in soup.find_all('h2',class_="clr-shade4 h3-p-name undefined false"):
    name.append(i.text)
name


# In[48]:


price=[]
for i in soup.find_all('div',class_="discountedPriceText clr-p-black false"):
    price.append(i.text)
price


# In[49]:


image=[]
for i in soup.find_all('div',class_="productCardImg false"):
    image.append(i.img['src'])
image


# In[50]:


df=pd.DataFrame({'Name':name,"Price":price,'Image':image})
df


# # Question7-Please visit https://www.cnbc.com/world/?region=world and scrapa) headings
# b) date
# c) News link

# In[51]:


page=requests.get('https://www.cnbc.com/economy/')
page


# In[52]:


soup=BeautifulSoup(page.content)
soup


# In[53]:


Heading=[]
for i in soup.find_all('div',class_="Card-titleContainer"):
    Heading.append(i.text)
Heading   


# In[54]:


Date=[]
for i in soup.find_all('span',class_="Card-time"):
    Date.append(i.text)
Date   


# In[55]:


import numpy as np


# In[56]:


link=[]
for i in soup.find_all('div',class_="Card-mediaContainer"):
    link.append(i.img['src'])
link


# In[57]:


df=pd.DataFrame({'Heading':Heading,'Date':Date})
df


# # Question 8-Please visit https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloadedarticles/ and scrap-
#  a) Paper title
#  b) date
#  c) Author

# In[ ]:


page=requests.get('https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-%20%20%20%20%20articles/',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})
page


# In[62]:


page


# its not allowing to scrap

# In[ ]:




