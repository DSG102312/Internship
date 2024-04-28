#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


#Q.1) 

sample_text = "Python Exercises, PHP exercises."
x = re.sub("[ ,.]", ":", sample_text)
x


# In[3]:


#Q.2)

import pandas as pd
dict = {'SUMMARY':['hello, world!','***** test','123four, five:; six...']}

df = pd.DataFrame(dict)

df

df['SUMMARY'] = df['SUMMARY'].str.replace('[^a-zA-Z\s]','',regex=True)

df


# In[13]:


#Q.3)

def four_letter_words(string):
    pattern = re.compile(r"\b\w{4,}\b")
    text = pattern.findall(string)
    return text


# In[14]:


four_letter_words('My son and my wife is my love and my life line, my life partner')


# In[16]:


#Q.4) 

def three_to_five_letter_words(string):
    pattern = re.compile(r"\b\w{3,5}\b")
    text = pattern.findall(string)
    return text


# In[17]:


three_to_five_letter_words("My son and my wife is my love and my life line, my life partner")


# In[31]:


#Q.5)

sample_text = "example (.com), hr@fliprobo (.com), github (.com), Hello (Data Science World), Data (Scientist)"
x = re.sub(r'[()]', '', sample_text)

print(x)


# In[21]:


#Q.6)

texts = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
for text in texts:
    print(re.sub(r" ?\([^)]+\)", "", text))


# In[2]:


#Q.7) 

sample_text = "ImportanceOfRegularExpressionsInPython"
x = re.findall("[A-Z][^A-Z]*", sample_text)
print(x)


# In[42]:


#Q.8) 

def spaces_in_words(sample_text):
    pattern = r"([a-zA-Z])(\d)"
    result = re.sub(pattern, r"\1 \2", sample_text)
    return result


# In[43]:


sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
spaces_in_words(sample_text)


# In[34]:


#Q.9)

def insert_spaces_in_words(word):
    pattern = r"([A-Z][a-z0-9]+|\d+)"
    result = re.sub(pattern, r' \1', word)
    result = result.strip()
    return result


# In[35]:


insert_spaces_in_words("RegularExpression1IsAn2ImportantTopic3InPython")


# In[9]:


#Q.10)

import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv')

df


# In[10]:


print(df['Country'])


# In[12]:


df['first_five_letters'] = df['Country'].apply(lambda x: x[:6])
df


# In[14]:


#Q.11)

def match_string(text):
        pattern = "^[a-zA-Z0-9_]*$"
        if re.search(pattern,  text):
                return "matched"
        else:
                return "Not matched"

print(match_string("The sky is blue"))
print(match_string("The_Skys_Is_Blue_1234"))


# In[33]:


#Q.12)

def match_specific_number(word):
    text = re.compile(r"^5")
    if text.match(word):
        return "matched" 
    else:
        return "not matched"
print(match_specific_number("532"))
print(match_specific_number("632"))


# In[35]:


#Q.13) 

ip_address = " 122.062.231.038"
text = re.sub('\.[0]*', '.', ip_address)
text


# In[42]:


#Q.14) 

sample_text = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country."

pattern = r"\b([A-Z][a-z]+ \d{1,2}(?:st|nd|rd|th)? \d{4})\b"

matches = re.findall(pattern, sample_text)
string_and_date = matches[0] if matches else None

string_and_date


# In[54]:


#Q.15)

patterns = ["fox","dog","horse"]
sample_text = "The quick brown fox jumps over the lazy dog."
for pattern in patterns:
    x = re.search(pattern, sample_text)
    print(x)


# In[56]:


#Q.16)

pattern = "fox"
sample_text = "The quick brown fox jumps over the lazy dog."
x = re.search(pattern, sample_text)
print(x)


# In[57]:


#Q.17) 

sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, sample_text):
    print('Found "%s"' % match)


# In[58]:


#Q.18)

sample_text = "The quick brown fox jumps over the lazy dog"
pattern = "fox"
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))


# In[15]:


#Q.19) 

def date_format_conversion(date1):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date1)
date2 = "2024-04-25"
print("Existinf format of date : YYY-MM-DD Format: ",date2)
print("New formate of date : DD-MM-YYYY Format: ",date_format_conversion(date2))


# In[99]:


#Q.20) 

def find_one_to_two_precision(string):
    patterns = re.compile(r"\d+\.\d{1,2}")
    result = re.findall(patterns, string)
    return result


# In[100]:


find_one_to_two_precision("01.12 0132.123 2.31875 145.8 3.01 27.25 0.25")


# In[2]:


#Q.21) 

sample_text = "There are 12 months in a year."
for m in re.finditer("\d+", sample_text):
    print(m.group(0))
    print("Index position:", m.start())


# In[16]:


#Q.22)

sample_text = "My marks in each semester are: 947, 896, 926, 524, 734, 950, 642"
max_number = re.findall("\d+", sample_text)
max_number = map(int, max_number)
print("Max_value:", max(max_number))


# In[7]:


#Q.23) 

text = "RegularExpressionIsAnImportantTopicInPython"
x = re.sub(r"(\w)([A-Z])",r"\1 \2", text)

print(x)


# In[17]:


#Q.24)

sample_text = "Regular Expression Is An Important Topic In Python"
patterns = r"\b[A-Z][a-z]+\b"
x = re.findall(patterns, sample_text)
print(x)


# In[18]:


#Q.25)

sample_text = "Hello hello world world"
patterns = r"\b(\w+)(\s+\1\b)+"
x = re.sub(patterns, r"\1", sample_text)
print(x)


# In[16]:


#Q.26) 

text = "abc125"
patterns = r"[a-zA-Z0-9]$"
x = re.search(patterns, text)
print("The string end with alphanumeric character: x")


# In[20]:


#Q27) 

sample_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
extract_the_hastag = re.findall(r"#\w+", sample_text)
extract_the_hastag


# In[21]:


#Q.28)

sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
patterns = r"<U\+\w{4}>"
x = re.sub(patterns, "", sample_text)
x


# In[7]:


#Q.29)

sample_text = "Ron was born on 12-09-1992 and he was admitted to school 15-12-1999."
pattern = "\d{2}[/-]\d{2}[/-]\d{4}"
dates = re.findall(pattern, sample_text)
dates


# In[4]:


#Q.30)

sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
x = re.compile(r'\W*\b\w{2,4}\b')
result = x.sub('', sample_text)
result


# In[ ]:




