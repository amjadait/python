#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
import random


window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("400x400") 
window.configure(bg="blue")  


title_label = tk.Label(window, text="Rock-Paper-Scissors", font=("Arial", 16))
title_label.pack(pady=20)


prompt_label = tk.Label(window, text="Choose: Rock, Paper  or Scissors", font=("Arial", 12))
prompt_label.pack()


user_choice_entry = tk.Entry(window, font=("Arial", 12))
user_choice_entry.pack()


choices = ["Rock", "Paper", "Scissors"]
comp_pick = random.choice(choices)

window.mainloop()


# In[ ]:




