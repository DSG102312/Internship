#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[128]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[ ]:


# Question.1)


# In[2]:


driver = webdriver.Chrome()


# In[3]:


#opening the naukri page on automated chrome browser
driver.get("https://www.naukri.com/")


# In[4]:


#entering designation and location as required in the questions:

designation = driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')


# In[5]:


#clicking on search button
search = driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[9]:


#applying location filter and clicking on it
location_filter = driver.find_element(By.XPATH,'/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[6]/div[2]/div[3]/label/i')
location_filter.click()


# In[6]:


#applying salary filter and then clicking on it
salary_filter = driver.find_element(By.XPATH,"/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[6]/div[2]/div[2]/label/p/span[1]")
salary_filter.click()


# In[10]:


job_title = []
job_location = []
company_name = []
experience_required = []


# In[11]:


#scraping job title from the given page
title_tags = driver.find_elements(By.XPATH,'//div[@class="cust-job-tuple layout-wrapper lay-2 sjw__tuple "]/div/a')
title_tags[0:10]
for i in title_tags[0:10]:
    title = i.text
    job_title.append(title)


# In[12]:


#scraping job location from the given page
location_tags = driver.find_elements(By.CLASS_NAME,'locWdth')
location_tags[0:10]
for i in location_tags[0:10]:
    location = i.text
    job_location.append(location)


# In[13]:


#scraping Company name from the given page
company_tags = driver.find_elements(By.XPATH,'//div[@class=" row2"]/span/a[1]')
company_tags[0:10]
for i in company_tags[0:10]:
    company = i.text
    company_name.append(company)


# In[14]:


#scraping job Experience from the given page
experience_tags = driver.find_elements(By.CLASS_NAME,'expwdth')
experience_tags[0:10]
for i in experience_tags[0:10]:
    exp = i.text
    experience_required.append(exp)


# In[15]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[16]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company_name':company_name,'Experience':experience_required})
df


# In[ ]:


# Question.2)


# In[17]:


driver = webdriver.Chrome()


# In[18]:


#opening the shine.com page on automated chrome browser
driver.get(" https://www.shine.com/")


# In[19]:


#entering designation and location as required in the questions:

designation = driver.find_element(By.CLASS_NAME,"form-control  ")
designation.send_keys('Data Scientist')


# In[20]:


location = driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Bangalore')


# In[21]:


search = driver.find_element(By.CLASS_NAME,"searchForm_btnWrap_advance__VYBHN")
search.click()


# In[22]:


job_title = []
job_location = []
company_name = []
experience_required = []


# In[23]:


#scraping job title from the given page
title_tags = driver.find_elements(By.CLASS_NAME,'jobCard_pReplaceH2__xWmHg')
title_tags[0:10]
for i in title_tags[0:10]:
    title = i.text
    job_title.append(title)


# In[24]:


#scraping job location from the given page
location_tags = driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
location_tags[0:10]
for i in location_tags[0:10]:
    location = i.text
    job_location.append(location)


# In[25]:


#scraping Company name from the given page
company_tags = driver.find_elements(By.CLASS_NAME,'jobCard_jobCard_cName__mYnow')
company_tags[0:10]
for i in company_tags[0:10]:
    company = i.text
    company_name.append(company)


# In[26]:


#scraping job Experience from the given page
experience_tags = driver.find_elements(By.XPATH,'//div[@style="display:flex"]')
experience_tags[0:10]
for i in experience_tags[0:10]:
    exp = i.text
    experience_required.append(exp)


# In[27]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[28]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company_name':company_name,'Experience':experience_required})
df


# In[ ]:


# Question.3)


# In[189]:


driver = webdriver.Chrome()


# In[190]:


#opening the given link page on automated chrome browser
driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART")


# In[191]:


product_rating = []
product_review = []
product_full_review = []


# In[222]:


start=0
end=10
#scraping ratings from given page
rating_tags = driver.find_elements(By.XPATH,'//div[@class="XQDdHH Ga3i8K"]')
for i in rating_tags:
    rating = i.text
    product_rating.append(rating)

#scraping reviews from given page
review_tags = driver.find_elements(By.XPATH,'//p[@class="z9E0IG"]')
for i in review_tags:
    review = i.text
    product_review.append(review)
    
#scraping overall review from given page
fullreview_tags = driver.find_elements(By.CLASS_NAME,'ZmyHeo')
for i in fullreview_tags:
    fullreview = i.text
    product_full_review.append(fullreview)
    
next_button = driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]/span') #to scrap data from next page as well
next_button.click()
time.sleep(3)


# In[220]:


print(len(product_rating),len(product_review),len(product_full_review))


# In[221]:


import pandas as pd
df=pd.DataFrame({'Rating':product_rating,'Review':product_review,'Full_Review':product_full_review})
df


# In[ ]:


# Question.4)


# In[231]:


driver = webdriver.Chrome()


# In[232]:


#opening the www.flipkart.com page on automated chrome browser
driver.get("https://www.flipkart.com/")


# In[233]:


#entering the product name as required in question
product = driver.find_element(By.CLASS_NAME,"Pke_EE")
product.send_keys('sneakers')


# In[234]:


#applying search button
search = driver.find_element(By.CLASS_NAME,"_2iLD__")
search.click()


# In[235]:


Brand_Name = []
Product_Description = []
Product_Price = []


# In[236]:


#scraping Product Brand name from the given page

brand_tags = driver.find_elements(By.CLASS_NAME,'syl9yP')
for i in brand_tags:
    brand = i.text
    Brand_Name.append(brand)


# In[237]:


#scraping Product Description from the given page
description_tags = driver.find_elements(By.CLASS_NAME,'WKTcLC')
for i in description_tags:
    description = i.get_attribute('title')
    Product_Description.append(description)


# In[238]:


#scraping product price from the given page
price_tags = driver.find_elements(By.XPATH,'//div[@class="Nx9bqj"]')
for i in price_tags:
    price = i.text
    Product_Price.append(price)


# In[239]:


print(len(Brand_Name),len(Product_Description),len(Product_Price))


# In[240]:


import pandas as pd
df=pd.DataFrame({'Brand':Brand_Name,'Description':Product_Description,'Price':Product_Price})
df


# In[ ]:


# Question.5) 


# In[131]:


driver = webdriver.Chrome()


# In[132]:


#opening the www.amazon page on automated chrome browser
driver.get("https://www.amazon.in/")


# In[133]:


#entering product name as per question
product = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
product.send_keys('Laptop')


# In[134]:


#applying search button
search = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
search.click()


# In[136]:


#applying filter button to find cpu criteria as per question
cpu_type = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[5]/ul[18]/span/span[9]/li/span/a/div/label/i')
cpu_type.click()


# In[137]:


Laptop_title = []
Laptop_ratings = []
Laptop_price = []


# In[138]:


#scraping laptop title
title_tags = driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
title_tags[0:10]
for i in title_tags[0:10]:
    title = i.text
    Laptop_title.append(title)


# In[139]:


#scraping ratings of laptops
ratings_tags = driver.find_elements(By.XPATH,'//span[@class="a-icon-alt"]')
ratings_tags[0:10]
for i in ratings_tags[0:10]:
    ratings = i.text
    Laptop_ratings.append(ratings)


# In[140]:


#scraping price of laptops
price_tags = driver.find_elements(By.CLASS_NAME,'a-price-whole')
price_tags[0:10]
for i in price_tags[0:10]:
    price = i.text
    Laptop_price.append(price)


# In[141]:


print(len(Laptop_title),len(Laptop_ratings),len(Laptop_price))


# In[142]:


import pandas as pd
df=pd.DataFrame({'Title':Laptop_title,'Ratings':Laptop_ratings,'Price':Laptop_price})
df


# In[ ]:


# Question.6)


# In[81]:


driver = webdriver.Chrome()


# In[82]:


#opening the www.azquotes page on automated chrome browser
driver.get("https://www.azquotes.com/ ")


# In[83]:


#clicking on the topics of quotes given as per question
search = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a')
search.click()


# In[84]:


quote_content = []
quote_author = []
quote_type = []


# In[112]:


start=0
end=10
#scraping quotes contents
content_tags = driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in content_tags:
    quote = i.text
    quote_content.append(quote)
    
#scraping author name of quotes
author_tags = driver.find_elements(By.CLASS_NAME,'author')
for i in author_tags:
    author = i.text
    quote_author.append(author)
    
#scraping type of the quotes
type_tags = driver.find_elements(By.CLASS_NAME,'tags')
for i in type_tags:
    type = i.text
    quote_type.append(type)
    
next_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/li[12]/a') #to scrap data from next page as well
next_button.click()
time.sleep(3)


# In[113]:


print(len(quote_content),len(quote_author),len(quote_type))


# In[114]:


import pandas as pd
df=pd.DataFrame({'Quote':quote_content,'Author':quote_author,'Type':quote_type})
df


# In[ ]:


# Question.7) 


# In[54]:


driver = webdriver.Chrome()


# In[55]:


#opening the given link on automated chrome browser
driver.get("https://www.jagranjosh.com/general-knowledge/list-of-all-prime-ministers-of-india-1473165149-1")


# In[56]:


pm_name = []
pm_borndead = []
pm_term = []
pm_remarks = []


# In[69]:


#scraping names of pm
name_tags = driver.find_elements(By.XPATH,'/html/body/div[1]/main/div[1]/div[1]/article/div[4]/div[7]/div/table/tbody/tr[2]/td[2]')
for i in name_tags:
    name = i.text
    pm_name.append(name)


# In[71]:


#scraping born and dead dates of pm
borndead_tags = driver.find_elements(By.XPATH,'/html/body/div[1]/main/div[1]/div[1]/article/div[4]/div[7]/div/table/tbody/tr[2]/td[3]')
for i in borndead_tags:
    borndead = i.text
    pm_borndead.append(borndead)


# In[73]:


#scraping term of pm
term_tags = driver.find_elements(By.XPATH,'/html/body/div[1]/main/div[1]/div[1]/article/div[4]/div[7]/div/table/tbody/tr[2]/td[4]')
for i in term_tags:
    term = i.text
    pm_term.append(term)


# In[75]:


#scraping remarks of pm
remarks_tags = driver.find_elements(By.XPATH,'/html/body/div[1]/main/div[1]/div[1]/article/div[4]/div[7]/div/table/tbody/tr[2]/td[5]')
for i in remarks_tags:
    remarks = i.text
    pm_remarks.append(remarks)


# In[76]:


print(len(pm_name),len(pm_borndead),len(pm_term),len(pm_remarks))


# In[77]:


import pandas as pd
df=pd.DataFrame({'Name':pm_name,'BornDead':pm_borndead,'Term':pm_term,'Remarks':pm_remarks})
df


# In[ ]:


# Question.8)


# In[78]:


driver = webdriver.Chrome()


# In[79]:


#opening the www.motor1.com page on automated chrome browser
driver.get("https://www.motor1.com/")


# In[81]:


#entering the types of cars as per question on search button
cars = driver.find_element(By.XPATH,'/html/body/div[9]/div[2]/div/div/div[3]/div/div/button')
cars.send_keys('50 most expensive cars')


# In[82]:


#applying search 
search = driver.find_element(By.XPATH,'/html/body/div[9]/div[2]/div/div/div[3]/div/div/div/form/button[1]')
search.click()


# In[83]:


#clicking of the contents we want to scrap as per question
search = driver.find_element(By.XPATH,'/html/body/div[9]/div[9]/div[1]/div[1]/div/div/div[1]/div/div[1]/h3/a')
search.click()


# In[84]:


car_name = []
car_price = []


# In[85]:


#scraping car name
name_tags = driver.find_elements(By.XPATH,'/html/body/div[9]/div[7]/div[2]/div[1]/div[2]/div[2]/h3[1]')
for i in name_tags:
    name = i.text
    car_name.append(name)


# In[86]:


#scraping car price
price_tags = driver.find_elements(By.XPATH,'/html/body/div[9]/div[7]/div[2]/div[1]/div[2]/div[2]/p[4]')
for i in price_tags:
    price = i.text
    car_price.append(price)


# In[87]:


print(len(car_name),len(car_price))


# In[88]:


import pandas as pd
df=pd.DataFrame({'Car_Name':car_name,'Car_Price':car_price})
df


# In[ ]:




