#!/usr/bin/env python
# coding: utf-8

# In[80]:


#1. Write a program that prompts the user to enter their name and age, 
#and then prints out a message that includes their name and their age.
Name  = input("Enter your name: ")
Age = input("Enter your age: ")
print("Hello World! I'm "+Name+" and I'm "+Age+"years Old.")


# In[6]:


#Problem 2:
User_Name = "Alex"
Age = "40"
print("My name is "+User_Name+" and I'm "+Age+" years old.")


# In[19]:


#problem 3:
N = int(input("Enter the number: "))

if (N % 2 == 0):
        print("The number is even")
else:
        print("The number is odd")


# In[79]:


#Problem 4:
A = int(input("Enter the number A: "))
B = int(input("Enter the numebr B: "))
temp = A
A = B
B = temp
print("A: ",A)
print("B: ",B)


# In[60]:


#Problem 5:
str1 = input("Enter the string: ")
list1 = (str1.strip())
print(list1)

for i in range(len(list1)):
    print(list1[i])
    


# In[47]:


#Problem 6:
Numbers  = input("Enter the numbers separated by ',':")
list1 = Numbers.split(",")

for i in range(len(list1)):
    list1[i] = int(list1[i])
    
sum_list = sum(list1)
Average = sum(list1)/len(list1)
print("Average = ",Average)


# In[54]:


#7.Write a program that prompts the user to enter a number 
#and then checks if the number is positive, negative, or zero.
Number = int(input("Enter the number:"))

if Number < 0:
    print("Number is negative")
elif Number > 0: 
    print("Number is positive")
else:
    print("Number is zero")


# In[72]:


# Write a program that takes a string as input and then checks if the string is a palindrome.

str1 = input("Enter the string: ")
#str2 = reversed(str1)
str2 = reversed(str1)
print(str2)


# In[78]:


# Program to check if a string is palindrome or not

str1 = input("Enter the string: ")

str2 = reversed(str1)

if list(str1) == list(str2):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")


# In[ ]:




