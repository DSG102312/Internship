#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[1]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[ ]:


# Question.1)


# In[18]:


driver = webdriver.Chrome()


# In[19]:


#opening the link on automated chrome browser
driver.get("https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos")


# In[38]:


videos_name=[]
videos_artist=[]
upload_date=[]
videos_views=[]


# In[39]:


#scraping name of the videos from the given page
name_tags = driver.find_elements(By.XPATH,'//div[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[1]')
for i in name_tags:
    name = i.text
    videos_name.append(name)


# In[40]:


#scraping artist of the videos from the given page
artist_tags = driver.find_elements(By.XPATH,'//div[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[2]')
for i in artist_tags:
    artist = i.text
    videos_artist.append(artist)


# In[41]:


#scraping upload date of videos from the given page
date_tags = driver.find_elements(By.XPATH,'//div[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[4]')
for i in date_tags:
    date = i.text
    upload_date.append(date)


# In[42]:


#scraping name of the videos from the given page
views_tags = driver.find_elements(By.XPATH,'//div[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[3]')
for i in views_tags:
    views = i.text
    videos_views.append(views)


# In[43]:


print(len(videos_name),len(videos_artist),len(upload_date),len(videos_views))


# In[45]:


import pandas as pd
df=pd.DataFrame({'NAME':videos_name,'ARTIST':videos_artist,'UPLOAD DATE':upload_date,'VIEWS(Billions)':videos_views})
df


# In[ ]:


#Question.2)


# In[65]:


driver = webdriver.Chrome()


# In[66]:


#opening the link on automated chrome browser
driver.get("https://www.bcci.tv/")


# In[67]:


#clicking on close button to close the ad displaying on front page
search = driver.find_element(By.XPATH,'/html/body/div[4]/div/div/button')
search.click()


# In[68]:


#clicking on international fixture button
search = driver.find_element(By.XPATH,'/html/body/header/div[3]/div[2]/ul/div[1]/a[2]')
search.click()


# In[70]:


#clicking on upcoming international fixture details
search = driver.find_element(By.XPATH,'//div[@class="tab-link upcoming current"]')
search.click()


# In[71]:


#clicking on more matches on upcoming international fixture details
search = driver.find_element(By.XPATH,'/html/body/section/div/div/div/div/div/div[2]/div[3]/div[2]/div/button')
search.click()


# In[72]:


match_series = []
match_date = []
match_time = []
match_place = []


# In[73]:


#scraping type of the matches name from the given page
series_tags = driver.find_elements(By.XPATH,'//h5[@class="match-tournament-name ng-binding"]')
for i in series_tags:
    series = i.text
    match_series.append(series)


# In[74]:


#scraping date of the matches from the given page
date_tags = driver.find_elements(By.XPATH,'//div[@class="match-dates ng-binding"]')
for i in date_tags:
    date = i.text
    match_date.append(date)


# In[75]:


#scraping time of the matches from the given page
time_tags = driver.find_elements(By.XPATH,'//div[@class="match-time no-margin ng-binding"]')
for i in time_tags:
    time = i.text
    match_time.append(time)


# In[76]:


#scraping place of the matches from the given page
place_tags = driver.find_elements(By.XPATH,'//div[@class="match-venue ng-scope"]')
for i in place_tags:
    place = i.text
    match_place.append(place)


# In[77]:


print(len(match_series),len(match_date),len(match_time),len(match_place))


# In[78]:


import pandas as pd
df=pd.DataFrame({'Series':match_series,'Date':match_date,'Time':match_time,'Place':match_place})
df


# In[ ]:


#Question.3)


# In[110]:


driver = webdriver.Chrome()


# In[111]:


#opening the link on automated chrome browser
driver.get("http://statisticstimes.com/ ")


# In[112]:


#clicking on economy  button on page
search = driver.find_element(By.XPATH,'//div[@id="top"]/div[2]/div[2]/button')
search.click()


# In[113]:


#clicking on India button in economy section in page
search = driver.find_element(By.XPATH,'//div[@id="top"]/div[2]/div[2]/div/a[3]')
search.click()


# In[114]:


#clicking on GDP of Indian states button in economy section in page
search = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/ul/li[1]/a')
search.click()


# In[115]:


state_rank = []
state_name = []
gsdp_current = []
gsdp_previous = []
state_share = []
state_gdp = []


# In[116]:


#scraping the rank of the states as per GDP from given page
rank_tags = driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[1]')
for i in rank_tags:
    rank = i.text
    state_rank.append(rank)


# In[117]:


#scraping the name of the states as per GDP from given page
name_tags = driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[2]')
for i in name_tags:
    name = i.text
    state_name.append(name)


# In[118]:


#scraping the GSDP(current year) of the states as per GDP from given page
current_tags = driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[4]')
for i in current_tags:
    current = i.text
    gsdp_current.append(current)


# In[119]:


#scraping the GSDP(previous year) of the states as per GDP from given page
previous_tags = driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[5]')
for i in previous_tags:
    previous = i.text
    gsdp_previous.append(previous)


# In[120]:


#scraping the share of the states as per GDP from given page
share_tags = driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[6]')
for i in share_tags:
    share = i.text
    state_share.append(share)


# In[121]:


#scraping the GDP of the states as per GDP from given page
gdp_tags = driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[7]')
for i in gdp_tags:
    gdp = i.text
    state_gdp.append(gdp)


# In[122]:


print(len(state_rank),len(state_name),len(gsdp_current),len(gsdp_previous),len(state_share),len(state_gdp))


# In[124]:


import pandas as pd
df=pd.DataFrame({'Rank':state_rank,'State Name':state_name,'GSDP Current Year':gsdp_current,'GSDP Previous Year':gsdp_previous,'Share':state_share,'GDP($billions)':state_gdp})
df


# In[ ]:


#Question.4)


# In[30]:


driver = webdriver.Chrome()


# In[31]:


#opening the link on automated chrome browser
driver.get("https://github.com/")


# In[32]:


#clicking on open source button on page
search = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[4]/button')
search.click()


# In[33]:


#clicking on trending  button on page
search = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[4]/div/div[3]/ul/li[2]/a')
search.click()


# In[47]:


repository_title = []
repository_description = []
repository_count = []
repository_language = []


# In[50]:


#scraping the title of the repository from the given page
title_tags = driver.find_elements(By.XPATH,'//h2[@class="h3 lh-condensed"]')
for i in title_tags:
    title = i.text
    repository_title.append(title)


# In[51]:


#scraping the description of the repository from the given page
description_tags = driver.find_elements(By.XPATH,'//p[@class="col-9 color-fg-muted my-1 pr-4"]')
for i in description_tags:
    description = i.text
    repository_description.append(description)


# In[48]:


#scraping the count of the repository from the given page
count_tags = driver.find_elements(By.XPATH,'//a[@class="Link Link--muted d-inline-block mr-3"]')
for i in count_tags:
    count = i.text
    repository_count.append(count)


# In[52]:


#scraping the language of the repository from the given page
language_tags = driver.find_elements(By.XPATH,'//span[@itemprop="programmingLanguage"]')
for i in language_tags:
    language = i.text
    repository_language.append(language)


# In[53]:


print(len(repository_title),len(repository_description),len(repository_count),len(repository_language))


# In[54]:


Muted=[]
for i in range(1,len(repository_count),2):
    Muted.append(repository_count[i])
    
print(len(Muted),Muted)


# In[55]:


Muted_Star=[]
for i in range(0,len(repository_count),2):
    Muted_Star.append(repository_count[i])
    
print(len(Muted_Star),Muted_Star)


# In[57]:


import pandas as pd
df=pd.DataFrame({'Title':repository_title,'Description':repository_description,'Count':Muted,'Star':Muted_Star,'Language Used':repository_language})
df


# In[ ]:


#Question.5)


# In[64]:


driver = webdriver.Chrome()


# In[65]:


#opening the link on automated chrome browser
driver.get("https:/www.billboard.com/")


# In[66]:


#clicking on top 100 hot songs button on page
search = driver.find_element(By.XPATH,'/html/body/div[3]/header/div/div[3]/div/nav/ul/li[1]/a')
search.click()


# In[67]:


song_name = []
artist_name = []
lastweek_rank = []
peak_pos = []
weekson_chart = []


# In[69]:


#scraping the name of the song from given page
name_tags = driver.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]/ul/li/h3')
for i in name_tags:
    name = i.text
    song_name.append(name)


# In[70]:


#scraping the artist name of the song from given page
name_tags = driver.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]/ul/li[1]/span')
for i in name_tags:
    name = i.text
    artist_name.append(name)


# In[71]:


#scraping the rank of the song from given page
rank_tags = driver.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]/ul/li[4]/span')
for i in rank_tags:
    rank = i.text
    lastweek_rank.append(rank)


# In[72]:


#scraping the peak position name of the song from given page
pos_tags = driver.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]/ul/li[5]/span')
for i in pos_tags:
    pos = i.text
    peak_pos.append(pos)


# In[73]:


#scraping the weeks on chart of the song from given page
chart_tags = driver.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]/ul/li[6]/span')
for i in chart_tags:
    chart = i.text
    weekson_chart.append(chart)


# In[74]:


print(len(song_name),len(artist_name),len(lastweek_rank),len(peak_pos),len(weekson_chart))


# In[76]:


import pandas as pd
df=pd.DataFrame({'Song Name':song_name,'Artist':artist_name,'Last Week Rank':lastweek_rank,'Peak Position':peak_pos,'Weeks on Chart':weekson_chart})
df


# In[ ]:


#Question.6)


# In[58]:


driver = webdriver.Chrome()


# In[59]:


#opening the link on automated chrome browser
driver.get("https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare")


# In[64]:


book_name = []
author_name = []
volumes_sold = []
book_pub = []
book_genre = []


# In[65]:


#scraping the name of the book from given page
name_tags = driver.find_elements(By.XPATH,'/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[2]')
for i in name_tags:
    name = i.text
    book_name.append(name)


# In[66]:


#scraping the author of the book from given page
name_tags = driver.find_elements(By.XPATH,'/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]')
for i in name_tags:
    name = i.text
    author_name.append(name)


# In[67]:


#scraping the volumes of the book sold from given page
sold_tags = driver.find_elements(By.XPATH,'/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[4]')
for i in sold_tags:
    sold = i.text
    volumes_sold.append(sold)


# In[68]:


#scraping the name of the Publisher of the book from given page
pub_tags = driver.find_elements(By.XPATH,'/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[5]')
for i in pub_tags:
    pub = i.text
    book_pub.append(pub)


# In[69]:


#scraping the Genre of the book from given page
genre_tags = driver.find_elements(By.XPATH,'/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[6]')
for i in genre_tags:
    genre = i.text
    book_genre.append(genre)


# In[70]:


print(len(book_name),len(author_name),len(volumes_sold),len(book_pub),len(book_genre))


# In[71]:


import pandas as pd
df=pd.DataFrame({'Book Name':book_name,'Author':author_name,'Volumes Sold':volumes_sold,'Publisher':book_pub,'Genre':book_genre})
df


# In[ ]:


#Question.7)


# In[12]:


driver = webdriver.Chrome()


# In[13]:


#opening the link on automated chrome browser
driver.get("https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv")


# In[14]:


series_name = []
series_yearspan = []
series_runtime = []
series_ratings = []
series_votes = []


# In[15]:


#scraping the name of the series from given page
name_tags = driver.find_elements(By.XPATH,'//div[@class="sc-b189961a-0 hBZnfJ cli-children"]/div[2]/a/h3')
for i in name_tags:
    name = i.text
    series_name.append(name)


# In[16]:


#scraping the year span of the series from given page
span_tags = driver.find_elements(By.XPATH,'//div[@class="sc-b189961a-0 hBZnfJ cli-children"]/div[3]/span[1]')
for i in span_tags:
    span = i.text
    series_yearspan.append(span)


# In[17]:


#scraping the runtime of the series from given page
runtime_tags = driver.find_elements(By.XPATH,'//div[@class="sc-b189961a-0 hBZnfJ cli-children"]/div[3]/span[2]')
for i in runtime_tags:
    runtime = i.text
    series_runtime.append(runtime)


# In[18]:


#scraping the Ratings of the series from given page
ratings_tags = driver.find_elements(By.XPATH,'//span[@class="sc-b189961a-1 kcfvgk"]/div/span')
for i in ratings_tags:
    ratings = i.text
    series_ratings.append(ratings)


# In[19]:


#scraping the Votes of the series from given page
votes_tags = driver.find_elements(By.XPATH,'//span[@class="sc-b189961a-1 kcfvgk"]/div/span')
for i in votes_tags:
    votes = i.text
    series_votes.append(votes)


# In[20]:


print(len(series_name),len(series_yearspan),len(series_runtime),len(series_ratings),len(series_votes))


# In[22]:


import pandas as pd
df=pd.DataFrame({'Name of Series':series_name,'Year Span':series_yearspan,'Runtime':series_runtime,'Ratings':series_ratings,'Votes':series_votes})
df


# In[ ]:


#Question.8)


# In[47]:


driver = webdriver.Chrome()


# In[48]:


#opening the link on automated chrome browser
driver.get("https://archive.ics.uci.edu/")


# In[49]:


#clicking on dataset button to view dataset on page
search = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/main/div/div[1]/div/div/div/a[1]')
search.click()


# In[50]:


dataset_name = []
data_type = []
task_todo = []
attribute_type = []
instances_count = []
attribute_count = []


# In[51]:


#scraping the name of the data set from given page
name_tags = driver.find_elements(By.XPATH,'//div[@class="relative col-span-8 sm:col-span-7"]/h2/a')
for i in name_tags:
    name = i.text
    dataset_name.append(name)


# In[52]:


#scraping the type of the data set from given page
type_tags = driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[2]/span')
for i in type_tags:
    Type = i.text
    data_type.append(Type)


# In[53]:


#scraping the task to do from the data set from given page
task_tags = driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[1]/span')
for i in task_tags:
    task = i.text
    task_todo.append(task)


# In[54]:


#scraping the number of instances of the data set from given page
count_tags = driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[3]/span')
for i in count_tags:
    count = i.text
    instances_count.append(count)


# In[55]:


#scraping the number of attribute of the data set from given page
count_tags = driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[4]/span')
for i in count_tags:
    count = i.text
    attribute_count.append(count)


# In[56]:


print(len(dataset_name),len(data_type),len(task_todo),len(instances_count),len(attribute_count))


# In[57]:


import pandas as pd
df=pd.DataFrame({'Dataset Name':dataset_name,'Data Type':data_type,'Task':task_todo,'No of Instances':instances_count,'No of Attribute':attribute_count})
df


# In[ ]:




