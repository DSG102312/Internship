#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[217]:


from bs4 import BeautifulSoup
import requests


# In[ ]:


# Q.1) Write a python program to display IMDB’s Top rated 100 Indian movies’ data 
#      https://www.imdb.com/list/ls056092300/ (i.e. name, rating, year ofrelease) and make data frame.


# In[284]:


info = requests.get("https://m.imdb.com/list/ls056092300/")


# In[285]:


info


# In[286]:


soup = BeautifulSoup(info.content)
soup


# In[238]:


html = '<html><div class="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN dli-title"><a href="/title/tt1773764/?ref_=ls_t_1" class="ipc-title-link-wrapper" tabindex="0"><h3 class="ipc-title__text">1. Ship of Theseus</h3></a></div></html>'
soup = BeautifulSoup(html, 'html.parser')
name = soup.find('div')
print(name.text)


# In[263]:


html = '<html><span class="sc-b189961a-8 kLaxqf dli-title-metadata-item">2012</span></html>'
soup = BeautifulSoup(html, 'html.parser')
year_of_release = soup.find('span')
print(year_of_release.text)


# In[264]:


html = '<html><span aria-label="IMDb rating: 8.0" class="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating" data-testid="ratingGroup--imdb-rating"><svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" class="ipc-icon ipc-icon--star-inline" viewBox="0 0 24 24" fill="currentColor" role="presentation"><path d="M12 20.1l5.82 3.682c1.066.675 2.37-.322 2.09-1.584l-1.543-6.926 5.146-4.667c.94-.85.435-2.465-.799-2.567l-6.773-.602L13.29.89a1.38 1.38 0 0 0-2.581 0l-2.65 6.53-6.774.602C.052 8.126-.453 9.74.486 10.59l5.147 4.666-1.542 6.926c-.28 1.262 1.023 2.26 2.09 1.585L12 20.099z"></path></svg>8.0<span class="ipc-rating-star--voteCount">&nbsp;(7.8K)</span></span></html>'
soup = BeautifulSoup(html, 'html.parser')
rating = soup.find('span')
print(rating.text)


# In[ ]:


# Q.2)   Write a python program to scrape details of all the posts from https://www.patreon.com/coreyms .Scrape the 
#        heading, date, content and the likes for the video from the link for the youtube video from the post. 


# In[270]:


page_information = requests.get("https://www.patreon.com/posts/python-tutorial-103296452")


# In[271]:


page_information


# In[165]:


soup = BeautifulSoup(page_information.content)
soup


# In[166]:


# heading

html = '<html><div class="sc-bYoBSM jnejQV"><span data-tag="post-title" elementtiming="post-title" class="sc-1cvoi1y-0 eGFfXM">Python Tutorial: Securely Manage Passwords and API Keys with DotEnv</span></div></html>'
soup = BeautifulSoup(html, 'html.parser')
heading = soup.find('span')
print(heading.text)


# In[171]:


#date

html = '<html><span><span>April 30</span></span></html>'
soup = BeautifulSoup(html, 'html.parser')
date = soup.find('span')
print(date.text)


# In[196]:


#likes

html = '<html><div class="sc-lkgTHX cqesBY"><span data-tag="like-count" class="sc-bdvvtL eHmEtx">1</span></div></html>'
soup = BeautifulSoup(html, 'html.parser')
likes = soup.find('span')
print(likes.text)


# In[276]:


#content

html = '<html><p><div class="sc-cfnzm4-0 daxSFj"><p>In this Python Programming video, we will be learning how to properly manage sensitive information within our scripts. We never want to add passwords, API Keys, Database information, or any other sensitive information directly to our code that others will be able to see. Instead, we want to store these away in Environment Variables. Python-DotEnv simplifies this process and makes it simple to do. Let's get started...</p></div></html>'
soup = BeautifulSoup(html, 'html.parser')
content = soup.find('p')
print(content.text)


# In[ ]:


# Q.3) Write a python program to scrape house details from mentioned URL. It should include house title, location, area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar, 
#      Rajaji Nagar.


# In[6]:


web_page_information = requests.get("https://www.nobroker.in/property/rent/chennai/multiple?searchParam=W3sibGF0IjoxMy4wNTIyMjY4LCJsb24iOjgwLjE4NTc2MjksInBsYWNlSWQiOiJDaElKdjlPLTVUUmhVam9STmhfVUdYNjJmZ3ciLCJwbGFjZU5hbWUiOiJJbmRpcmEgTmFnYXIifSx7ImxhdCI6MTMuMDM0MjExNiwibG9uIjo4MC4xNTE5Mjk0LCJwbGFjZUlkIjoiQ2hJSmR5a3c2UUpoVWpvUkpGR0JwYUFVM3NBIiwicGxhY2VOYW1lIjoiSmF5YSBOYWdhciJ9LHsibGF0IjoxMi45NjU5NjM3LCJsb24iOjgwLjE1MzMyNDkwMDAwMDAyLCJwbGFjZUlkIjoiQ2hJSkFZaHFPMDFlVWpvUmZMOUtCZUphVENjIiwicGxhY2VOYW1lIjoiUmFqYWppIE5hZ2FyIn1d&radius=2.0&sharedAccomodation=0&city=chennai&locality=Indira%20Nagar,Jaya%20Nagar,Rajaji%20Nagar")


# In[7]:


web_page_information


# In[8]:


soup = BeautifulSoup(web_page_information.content)
soup


# In[9]:


house_title = []

for i in soup.find_all('h2',class_="heading-6 flex items-center font-semi-bold m-0"):
    house_title.append(i.text)
    
house_title


# In[10]:


location = []

for i in soup.find_all('div',class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0.1p po:max-w-95"):
    location.append(i.text)
    
location


# In[11]:


area = []

for i in soup.find_all('div',class_="flex flex-col w-33pe items-center tp:w-half po:w-full"):
    area.append(i.text)
    
area


# In[38]:


emi = []

for i in soup.find_all('div',class_="font-semi-bold heading-6",id="roomType"):
    emi.append(i.text)
    
emi


# In[36]:


price = []

for i in soup.find_all('div',class_="flex",id="minimumRent"):
    price.append(i.text)
    
price


# In[39]:


import pandas as pd
df = pd.DataFrame({'Name':house_title, 'Location':location,'Built_up_Area':area,'Rent_per_Month':price,'EMI':emi})
df


# In[ ]:


# Q.4)  Write a python program to scrape first 10 product details which include product name , price , Image URL from 
#       https://www.bewakoof.com/bestseller?sort=popular . 


# In[2]:


page_info = requests.get("https://www.bewakoof.com/bestseller?sort=popular%20")


# In[3]:


page_info


# In[4]:


soup = BeautifulSoup(page_info.content)
soup


# In[5]:


products = []

for i in soup.find_all('div',class_="productNaming bkf-ellipsis"):
    products.append(i.text)
    
products


# In[6]:


price_tag = [] 

for i in soup.find_all('div',class_="discountedPriceText clr-p-black false"):
    price_tag.append(i.text)
    
price_tag


# In[7]:


images_url = []
for i in soup.find_all('img', class_="productImgTag"):
    images_url.append(i['src'])
    
images_url


# In[8]:


import pandas as pd
df = pd.DataFrame({'Product_Name':products, 'Product_Price_Tag':price_tag, 'Images_url':images_url})
df


# In[ ]:


# Q.5) Please visit https://www.cnbc.com/world/?region=world and scrap- 
#      a) headings 
#      b)  date 
#      c) News link


# In[150]:


page_info_cnbc = requests.get("https://www.cnbc.com/world/?region=world")


# In[151]:


page_info_cnbc


# In[152]:


soup = BeautifulSoup(page_info_cnbc.content)
soup


# In[153]:


# a) heading

html = '<html><div><h1 class="ArticleHeader-headline">Federal Reserve minutes indicate worries over lack of progress on inflation</h1></div></html>'
soup = BeautifulSoup(html, 'html.parser')
heading = soup.find('h1')
print(heading.text)


# In[154]:


# b) date

html = '<html><div class="ArticleHeader-time"><time data-testid="published-timestamp" datetime="2024-05-22T18:00:44+0000" itemprop="datePublished">Published Wed, May 22 2024<span class="ArticleHeader-datetimeDivider"></span>2:00 PM EDT</time><span class="ArticleHeader-timestampDivider"></span><time data-testid="lastpublished-timestamp" datetime="2024-05-22T20:01:43+0000" itemprop="dateModified">Updated Wed, May 22 2024<span class="ArticleHeader-datetimeDivider"></span>4:01 PM EDT</time></div></html>'
soup = BeautifulSoup(html, 'html.parser')
date = soup.find('time')
print(date.text)


# In[161]:


# c) news link

import re
for link in soup.find_all('a',attrs={'href': re.compile("^https://")}): 
    print(link.get('href')) 


# In[ ]:





# In[ ]:


# Q.6)   Please visit  https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded
#         articles/  and scrap- 
#         a) Paper title 
#         b) date 
#         c) Author


# In[26]:


web_info = requests.get("https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/")


# In[27]:


web_info


# In[28]:


soup = BeautifulSoup(web_info.content)
soup


# In[43]:


# a)paper title

paper_title = []

for i in soup.find_all('h2',class_="h5 article-title"):
    paper_title.append(i.text)
    
paper_title


# In[45]:


# b) date

date = []

for i in soup.find_all('p',class_="article-date"):
    date.append(i.text)
    
date


# In[46]:


# c) author

author = []

for i in soup.find_all('p',class_="article-authors"):
    author.append(i.text)
    
author


# In[47]:


import pandas as pd
df = pd.DataFrame({'Title':paper_title, 'Date_of_Publish':date, 'Author':author})
df


# In[ ]:




