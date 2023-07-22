#!/usr/bin/env python
# coding: utf-8

# In[20]:


#1)

class Point3D: 
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

my_point = Point3D(1, 2, 3)

print(my_point)


# In[17]:


#2)

class Rectangle: 
    def __init__(self, length , width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

my_rectangle = Rectangle(4, 3)

print(my_rectangle.area())
print(my_rectangle.perimeter())


# In[33]:


#3)

import math

class Circle:
    def __init__(self, x_center,y_center, radius):
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def is_inside(self, x, y):
           if  (( self.x_center - x) **2 + (self.y_center - y) **2 - self.radius ** 2) == 0:
                return True
           else :  
                return False
            
my_circle = Circle(3,4,5)

        
print(my_circle.area())
print(my_circle.perimeter())
print(my_circle.is_inside(3,5))


# In[44]:


#4)

class Bank: 
    def __init__(self, balance = 0):
        self.balance = balance
    def deposit(self, amount):
        self.balance =  self.balance + amount
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
    def Balance(self):
        return self.balance
        
my_bank = Bank(10)

my_bank.withdraw(15)
my_bank.Balance()


# In[ ]:




