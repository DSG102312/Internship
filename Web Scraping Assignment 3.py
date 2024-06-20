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


# In[25]:


# Question.1)


# In[69]:


driver = webdriver.Chrome()


# In[70]:


#opening the amazon web page on automated chrome browser
driver.get("https://www.amazon.com/")


# In[71]:


#entering product name as per question
product = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
product.send_keys('guitar')


# In[72]:


#applying search button
search = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
search.click()


# In[ ]:


#Question.2)


# In[154]:


product_name = []
product_url = []


# In[155]:


#scraping product name from the given page
name_tags = driver.find_elements(By.XPATH,'//span[@class="a-size-base-plus a-color-base a-text-normal"]')
for i in name_tags:
    name = i.text
    product_name.append(name)


# In[156]:


#scraping product url from the given page
url_tags = driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
for i in url_tags:
    url = i.get_attribute('href')
    product_url.append(url)


# In[157]:


print(len(product_name),len(product_url))


# In[158]:


import pandas as pd
df=pd.DataFrame({'Product':product_name,'URL':product_url})
df


# In[ ]:


#Question.3)


# In[2]:


driver = webdriver.Chrome()


# In[3]:


#opening the google image web page on automated chrome browser
driver.get("http://www.images.google.com/")


# In[ ]:


#Searching  for 'fruits' 


# In[4]:


#entering product name as per question
product = driver.find_element(By.CLASS_NAME,'gLFyf')
product.send_keys('fruits')


# In[5]:


#applying search button
search = driver.find_element(By.CLASS_NAME,'zgAlFc')
search.click()


# In[10]:


fruits_title = []


# In[11]:


#scraping ten fruits details from the given page
title_tags = driver.find_elements(By.XPATH,'//div[@class="toI8Rb OSrXXb"]')
title_tags[0:10]
for i in title_tags[0:10]:
    title = i.text
    fruits_title.append(title)


# In[12]:


print(len(fruits_title))


# In[6]:


image_url = []


# In[7]:


#scraping product url of the first ten image
url_tags = driver.find_elements(By.XPATH,'//h3[@class="ob5Hkd"]/a')
url_tags[0:10]
for i in url_tags[0:10]:
    url = i.get_attribute('href')
    image_url.append(url)


# In[8]:


print(len(image_url))


# In[13]:


import pandas as pd
df=pd.DataFrame({'Fruits':fruits_title,'URL':image_url})
df


# In[ ]:


#Search for 'cars'


# In[14]:


driver = webdriver.Chrome()


# In[15]:


#opening the google image web page on automated chrome browser
driver.get("http://www.images.google.com/")


# In[16]:


#entering product name: 'car' on search bar
product = driver.find_element(By.CLASS_NAME,'gLFyf')
product.send_keys('cars')


# In[17]:


#applying search button
search = driver.find_element(By.CLASS_NAME,'zgAlFc')
search.click()


# In[18]:


cars_title = []


# In[19]:


#scraping ten cars details from the given page
title_tags = driver.find_elements(By.XPATH,'//div[@class="toI8Rb OSrXXb"]')
title_tags[0:10]
for i in title_tags[0:10]:
    title = i.text
    cars_title.append(title)


# In[20]:


print(len(cars_title))


# In[31]:


image_url = []


# In[32]:


#scraping product url of the first ten image
url_tags = driver.find_elements(By.XPATH,'//h3[@class="ob5Hkd"]/a')
url_tags[0:10]
for i in url_tags[0:10]:
    url = i.get_attribute('href')
    image_url.append(url)


# In[33]:


print(len(image_url))


# In[34]:


import pandas as pd
df=pd.DataFrame({'Cars':cars_title,'URL':image_url})
df


# In[ ]:


#Search for 'Machine Learning'


# In[35]:


driver = webdriver.Chrome()


# In[36]:


#opening the google image web page on automated chrome browser
driver.get("http://www.images.google.com/")


# In[37]:


#entering product name: 'Machine Learning' as per question
product = driver.find_element(By.CLASS_NAME,'gLFyf')
product.send_keys('Machine Learning')


# In[38]:


#applying search button
search = driver.find_element(By.CLASS_NAME,'zgAlFc')
search.click()


# In[39]:


machine_learning_title = []


# In[40]:


#scraping ten Machine Learning details from the given page
title_tags = driver.find_elements(By.XPATH,'//div[@class="toI8Rb OSrXXb"]')
title_tags[0:10]
for i in title_tags[0:10]:
    title = i.text
    machine_learning_title.append(title)


# In[41]:


print(len(machine_learning_title))


# In[42]:


image_url = []


# In[43]:


#scraping product url of the first ten image
url_tags = driver.find_elements(By.XPATH,'//h3[@class="ob5Hkd"]/a')
url_tags[0:10]
for i in url_tags[0:10]:
    url = i.get_attribute('href')
    image_url.append(url)


# In[44]:


print(len(image_url))


# In[45]:


import pandas as pd
df=pd.DataFrame({'Machine_Learning':machine_learning_title,'URL':image_url})
df


# In[ ]:


#Search for 'Guitar'


# In[46]:


driver = webdriver.Chrome()


# In[47]:


#opening the google image web page on automated chrome browser
driver.get("http://www.images.google.com/")


# In[48]:


#entering product name:'Guitar' as per question
product = driver.find_element(By.CLASS_NAME,'gLFyf')
product.send_keys('Guitar')


# In[49]:


#applying search button
search = driver.find_element(By.CLASS_NAME,'zgAlFc')
search.click()


# In[50]:


guitar_title = []


# In[51]:


#scraping ten Guital details from the given page
title_tags = driver.find_elements(By.XPATH,'//div[@class="toI8Rb OSrXXb"]')
title_tags[0:10]
for i in title_tags[0:10]:
    title = i.text
    guitar_title.append(title)


# In[52]:


print(len(guitar_title))


# In[54]:


image_url = []


# In[55]:


#scraping product url of the first ten image
url_tags = driver.find_elements(By.XPATH,'//h3[@class="ob5Hkd"]/a')
url_tags[0:10]
for i in url_tags[0:10]:
    url = i.get_attribute('href')
    image_url.append(url)


# In[56]:


print(len(image_url))


# In[57]:


import pandas as pd
df=pd.DataFrame({'Guitar':guitar_title,'URL':image_url})
df


# In[ ]:


#Search 'Cakes'


# In[58]:


driver = webdriver.Chrome()


# In[59]:


#opening the google image web page on automated chrome browser
driver.get("http://www.images.google.com/")


# In[60]:


#entering product name:Cakes as per question
product = driver.find_element(By.CLASS_NAME,'gLFyf')
product.send_keys('Cakes')


# In[61]:


#applying search button
search = driver.find_element(By.CLASS_NAME,'zgAlFc')
search.click()


# In[62]:


cakes_title = []


# In[63]:


#scraping ten cakes details from the given page
title_tags = driver.find_elements(By.XPATH,'//div[@class="toI8Rb OSrXXb"]')
title_tags[0:10]
for i in title_tags[0:10]:
    title = i.text
    cakes_title.append(title)


# In[64]:


print(len(cakes_title))


# In[65]:


image_url = []


# In[66]:


#scraping product url of the first ten image
url_tags = driver.find_elements(By.XPATH,'//h3[@class="ob5Hkd"]/a')
url_tags[0:10]
for i in url_tags[0:10]:
    url = i.get_attribute('href')
    image_url.append(url)


# In[67]:


print(len(image_url))


# In[68]:


import pandas as pd
df=pd.DataFrame({'Cakes':cakes_title,'URL':image_url})
df


# In[ ]:


#Question.4)


# In[33]:


driver = webdriver.Chrome()


# In[34]:


#opening the www.flipkart.com page on automated chrome browser
driver.get("https://www.flipkart.com/")


# In[35]:


#entering the product name as required in question
product = driver.find_element(By.CLASS_NAME,"Pke_EE")
product.send_keys('smartphone')


# In[36]:


#applying search button
search = driver.find_element(By.CLASS_NAME,"_2iLD__")
search.click()


# In[66]:


phone_name = []
phone_brand = []
phone_price = []
phone_ram_rom = []
phone_camera = []
phone_battery = []
phone_display = []
phone_url = []


# In[67]:


#scraping phone name
name_tags = driver.find_elements(By.CLASS_NAME,'KzDlHZ')
for i in name_tags:
    name = i.text
    phone_name.append(name)


# In[68]:


#scraping phone brand
brand_tags = driver.find_elements(By.CLASS_NAME,'KzDlHZ')
for i in brand_tags:
    brand = i.text
    phone_brand.append(brand)


# In[69]:


#scraping phone price
price_tags = driver.find_elements(By.XPATH,'//div[@class="Nx9bqj _4b5DiR"]')
for i in price_tags:
    price = i.text
    phone_price.append(price)


# In[70]:


#scraping phone ram and rom
ram_rom_tags = driver.find_elements(By.XPATH,'//div[@class="_6NESgJ"]/ul/li[1]')
for i in ram_rom_tags:
    ram_rom = i.text
    phone_ram_rom.append(ram_rom)


# In[71]:


#scraping phone camera
camera_tags = driver.find_elements(By.XPATH,'//div[@class="_6NESgJ"]/ul/li[3]')
for i in camera_tags:
    camera = i.text
    phone_camera.append(camera)


# In[74]:


#scraping phone battery
battery_tags = driver.find_elements(By.XPATH,'//div[@class="_6NESgJ"]/ul/li[4]')
for i in battery_tags:
    battery = i.text
    phone_battery.append(battery)


# In[72]:


#scraping phone display
display_tags = driver.find_elements(By.XPATH,'//div[@class="_6NESgJ"]/ul/li[2]')
for i in display_tags:
    display = i.text
    phone_display.append(display)


# In[ ]:


#scraping phone display
display_tags = driver.find_elements(By.XPATH,'//div[@class="_6NESgJ"]/ul/li[2]')
for i in display_tags:
    display = i.text
    phone_display.append(display)


# In[76]:


#scraping phone url from the given page
url_tags = driver.find_elements(By.XPATH,'//a[@class="CGtC98"]')
for i in url_tags:
    url = i.get_attribute('href')
    phone_url.append(url)


# In[77]:


print(len(phone_name),
      len(phone_brand),
      len(phone_price),
      len(phone_ram_rom),
      len(phone_camera),
      len(phone_battery),
      len(phone_display),
      len(phone_url))


# In[78]:


import pandas as pd
df=pd.DataFrame({'Name':phone_name,'Brand':phone_brand,'Price':phone_price,'RAM and ROM':phone_ram_rom,'Camera Specification':phone_camera,'Battery Capacity':phone_battery,'Display Quality':phone_display,'Product Link':phone_url})
df


# In[ ]:


#Question.5)


# In[94]:


driver = webdriver.Chrome()


# In[95]:


#opening the google map link page on automated chrome browser
driver.get("https://www.google.com/maps")


# In[96]:


#entering location name as patna
product = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[1]/form/input')
product.send_keys('patna')


# In[97]:


#applying search button
search = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[1]/div[1]/button/span')
search.click()


# In[99]:


import re
try:
    url_string = driver.current_url
    print("URL Extracted: ", url_string)
    lat_lng = re.findall(r'@(.*)data',url_string)
    if len(lat_lng):
        lat_lng_list = lat_lng[0].split(",")
        if len(lat_lng_list)>=2:
            lat = lat_lng_list[0]
            lng = lat_lng_list[1]
        print("Latitude = {}, Longitude = {}".format(lat, lng))

except Exception as e:
        print("Error: ", str(e))


# In[ ]:


#Question.6)


# In[34]:


driver = webdriver.Chrome()


# In[35]:


#opening the digit.in link page on automated chrome browser
driver.get("https://www.digit.in/top-products/best-amd-gaming-laptops-for-students-4071.html")


# In[36]:


brand_name = []
screen_size = []
laptop_config = []


# In[37]:


#scraping laptop brand
brand_tags = driver.find_elements(By.XPATH,'//h3[@class="font130 mt0 mb10 mobilesblockdisplay "]')
for i in brand_tags:
    brand = i.text
    brand_name.append(brand)


# In[38]:


#scraping laptop screen size
screen_tags = driver.find_elements(By.XPATH,'//div[@class="rh_gr_middle_desc"]/div/div[2]')
for i in screen_tags:
    screen = i.text
    screen_size.append(screen)


# In[39]:


#scraping laptop configuration
config_tags = driver.find_elements(By.XPATH,'//div[@class="rh_gr_middle_desc"]/div/div[4]')
for i in config_tags:
    config = i.text
    laptop_config.append(config)


# In[42]:


print(len(brand_name),len(screen_size),len(laptop_config))


# In[44]:


import pandas as pd
df=pd.DataFrame({'Brand':brand_name,'Screen':screen_size,'Configuration':laptop_config})
df


# In[ ]:


#Question.7)


# In[64]:


driver = webdriver.Chrome()


# In[65]:


#opening the forbes.com link page on automated chrome browser
driver.get("https://www.forbes.com/billionaires/")


# In[66]:


person_rank = []
person_name = []
person_networth = []


# In[67]:


#scraping person rank
rank_tags = driver.find_elements(By.XPATH,'//div[@class="Table_rank__X4MKf"]/div')
for i in rank_tags:
    rank = i.text
    person_rank.append(rank)


# In[68]:


#scraping person name
name_tags = driver.find_elements(By.XPATH,'//div[@class="Table_personName__Bus2E"]')
for i in name_tags:
    name = i.text
    person_name.append(name)


# In[69]:


#scraping person networth
networth_tags = driver.find_elements(By.XPATH,'//div[@class="Table_finalWorth__UZA6k"]/span')
for i in networth_tags:
    networth = i.text
    person_networth.append(networth)


# In[70]:


print(len(person_rank),
      len(person_name),
      len(person_networth))


# In[72]:


person_industry = []


# In[74]:


#scraping person networth
industry_tags = driver.find_elements(By.XPATH,'//div[@class="Table_tableRow__lF_cY"]/div[4]')
for i in industry_tags:
    industry = i.text
    person_industry.append(industry)


# In[75]:


print(len(person_industry))


# In[107]:


import pandas as pd
df=pd.DataFrame({'Rank':person_rank,'Name':person_name,'Networth':person_networth,'Industry':person_industry})
df


# In[ ]:


#Question.8)


# In[48]:


driver = webdriver.Chrome()


# In[49]:


#opening the forbes.com link page on automated chrome browser
driver.get("https://www.youtube.com/watch?v=OzI9M74IfR0")


# In[50]:


# Scroll down to load comments and other details
scroll_pause_time = 5  #pause time as needed
scrolls = 30  #number of scrolls as needed

for _ in range(scrolls):
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(scroll_pause_time)


# In[51]:


public_comments = []


# In[52]:


#scraping comments on particular video
comments_tags = driver.find_elements(By.XPATH,'//yt-attributed-string[@id="content-text"]/span[1]')
comments_tags[0:500]
for i in comments_tags[0:500]:
    comments = i.text
    public_comments.append(comments)


# In[53]:


print(len(public_comments))


# In[54]:


# Scroll down to load comments and other details
scroll_pause_time = 5  #pause time as needed
scrolls = 30  #number of scrolls as needed

for _ in range(scrolls):
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(scroll_pause_time)


# In[55]:


public_upvotes =[]


# In[56]:


#scraping upvotes of comments
upvotes_tags = driver.find_elements(By.XPATH,'//span[@id="vote-count-middle"]')
upvotes_tags[0:500]
for i in upvotes_tags[0:500]:
    upvotes = i.text
    public_upvotes.append(upvotes)


# In[57]:


print(len(public_upvotes))


# In[58]:


# Scroll down to load comments and other details
scroll_pause_time = 5  #pause time as needed
scrolls = 30  #number of scrolls as needed

for _ in range(scrolls):
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(scroll_pause_time)


# In[59]:


post_time = []


# In[60]:


#scraping time of posting
time_tags = driver.find_elements(By.XPATH,'//span[@class="style-scope ytd-comment-view-model"]/a')
time_tags[0:500]
for i in time_tags[0:500]:
    time = i.text
    post_time.append(time)


# In[61]:


print(len(post_time))


# In[62]:


import pandas as pd
df=pd.DataFrame({'Comments':public_comments,'Upvotes':public_upvotes,'Time':post_time})
df


# In[ ]:


#Question.9)


# In[148]:


driver = webdriver.Chrome()


# In[149]:


#opening the www.hostelworld.com link page on automated chrome browser
driver.get("https://www.hostelworld.com/")


# In[150]:


#entering the location 'London' as per question
product = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/main/header/div/div[2]/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/label/input')
product.send_keys('London')


# In[151]:


#clicking on London Location button
search = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/main/header/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/ul/li[2]/button/div[2]/div[1]')
search.click()


# In[152]:


#applying search button
search = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/main/header/div/div[2]/div[1]/div[1]/div/div[5]/button[1]')
search.click()


# In[153]:


hostel_name = []


# In[154]:


#scraping hostels names
name_tags = driver.find_elements(By.XPATH,'//div[@class="property-name"]/span')
for i in name_tags:
    name = i.text
    hostel_name.append(name)


# In[155]:


print(len(hostel_name))


# In[156]:


hostel_distance = []


# In[157]:


#scraping hostels distance
distance_tags = driver.find_elements(By.XPATH,'//div[@class="property-distance"]/span[2]')
for i in distance_tags:
    distance = i.text
    hostel_distance.append(distance)


# In[158]:


print(len(hostel_distance))


# In[159]:


hostel_ratings = []


# In[160]:


#scraping hostels ratings
ratings_tags = driver.find_elements(By.XPATH,'//span[@class="number"]')
for i in ratings_tags:
    ratings = i.text
    hostel_ratings.append(ratings)


# In[161]:


print(len(hostel_ratings))


# In[162]:


hostel_review = []                  


# In[163]:


#scraping hostels review
review_tags = driver.find_elements(By.XPATH,'//div[@class="review"]')
for i in review_tags:
    review = i.text
    hostel_review.append(review)


# In[164]:


print(len(hostel_review))


# In[168]:


import pandas as pd
df=pd.DataFrame({'Hostel Name':hostel_name,'Distance from City Centre':hostel_distance,'Ratings':hostel_ratings,'Number of Reviews':hostel_review})
df


# In[ ]:




