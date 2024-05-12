#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Q.11) Write a python program to find the factorial of a number. 

def fact(num):
    return 1 if (num==1 or num==0) else num * fact(num-1)
number = 6

fact(number)


# In[7]:


#Q.12) Write a python program to find whether a number is prime or composite.

number = int(input("Enter any number : "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "not a prime number")
            break
    else:
        print(number, "is prime number")
elif number == 0 or 1:
    print(number, "is a neither prime nor composite number")
else:
    print(num, "is not a prime number it is a composite number")


# In[11]:


#Q.13) Write a python program to check whether a given string is palindrome or not.

def isPalindrome(string):
    return string == string[::-1]
 
string = "AIBOHPHOBIA"
answer = isPalindrome(string)
 
if answer:
    print("Yes!, The string is palindrome.")
else:
    print("No!, The string is not palindrome")


# In[17]:


#Q.14)  Write a Python program to get the third side of right-angled triangle from two given sides. 

def test(a, b):
    
    hypotenuse = (a**2 + b**2)**0.5
    
    return hypotenuse

print(test(3, 4))


# In[20]:


#Q.15) Write a python program to print the frequency of each of the characters present in a given string.


def character_frequency(str1):
   
    dict = {}
    
    for n in str1:
        
        keys = dict.keys()
        
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1

    return dict

character_frequency('singh.abhijith')


# In[4]:


print(6|2)


# In[ ]:




