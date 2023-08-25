#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
import random


window = tk.Tk()
window.title("Convertisseur Fahrenheit - Celsius")
window.geometry("400x400") 
window.configure(bg="blue")  


title_label = tk.Label(window, text="Convertisseur Fahrenheit - Celsius", font=("Arial", 16))
title_label.pack(pady=20)


prompt_label = tk.Label(window, text="Entrer en Celsius", font=("Arial", 12))
prompt1_label = tk.Label(window, text="Entrer en Fahrenheit", font=("Arial", 12))
prompt_label.pack()


user_choice_entry = tk.Entry(window, font=("Arial", 12))
user_choice_entry.pack()



window.mainloop()

# In[ ]:




