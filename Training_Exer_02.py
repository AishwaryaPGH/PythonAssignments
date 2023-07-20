#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Write a Python program to display your details like name, age, address in three different lines.
def Name_Address():
    Name = input("Enter your name: ")
    Age = input("Enter your age: ")
    Address = input("Enter your adress: ")
    print("Name: {}\nAge: {}\nAddress: {}".format(Name, Age, Address))

Name_Address()


# In[4]:


#Write a Python program to display the current date and time.
from datetime import date
from datetime import datetime

Today = date.today()
Today_date = Today.strftime("%m/%d/%y")
Time = datetime.now()
print("Date: ",Today_date)
print("Time: ",Time)


# In[7]:


#Write a Python program which accepts the radius of a circle from the user and compute the area.
import math
def Area_Circle(R):
    Area = (math.pi*(R*R))
    return Area

R = int(input("Enter the radius: "))
Area = Area_Circle(R)
print("Area of the circle:", Area)


# In[9]:


#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

def Value_N(N):
    Val = (N+(N*N)+(N*N*N))
    return Val

N = int(input("Enter the value of N: "))
Val = Value_N(N)
print("Value of N:",Val)


# In[ ]:




