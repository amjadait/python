#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np

def grade(notes,totalnotes):
    pr = (notes/totalnotes)*100
    if pr >= 90:
        print("A+") 
    elif pr >= 80:
        print("A")
    elif pr>= 70:
        print("B+") 
    elif pr >= 60:
        print("B") 
    elif pr >= 50:
        print("C") 
    else:
        print("F") 
    

subjects = int(input("Entrer le nombre de matières: "))
students = int(input("Entrer le nombre d'élèves: "))


notes = np.zeros((students, subjects))


for i in range(students):
    print("Entrer la note d étudiant", i+1)
    for j in range(subjects):
        notes[i,j] = float(input("entrer la note"))

totalnotes = np.sum(notes, axis = 1)
percentage = (totalnotes /  (subjects * 100)) * 100
grades_array = np.array([grade(total,subjects * 100) for total in totalnotes])





print("\nResult:")
print("--------------------------------------------------------------")
print("Student\tTotal Notes\tPercentage\tGrade")
print("--------------------------------------------------------------")
for i in range(students):
    print(f"{i + 1}\t\t{totalnotes[i]}\t\t{percentage[i]:.2f}%\t\t", grades_array[i])
print("--------------------------------------------------------------")


# In[6]:


print("Enter Marks Obtained in 5 Subjects: ")
total1 = 44
total2 = 67
total3 = 76
total4 = 99
total5 = 58

tot = total1 + total2 + total3 + total4 + total4
avg = tot / 5

if avg >= 91 and avg <= 100:
	print("Your Grade is A1")
elif avg >= 81 and avg < 91:
	print("Your Grade is A2")
elif avg >= 71 and avg < 81:
	print("Your Grade is B1")
elif avg >= 61 and avg < 71:
	print("Your Grade is B2")
elif avg >= 51 and avg < 61:
	print("Your Grade is C1")
elif avg >= 41 and avg < 51:
	print("Your Grade is C2")
elif avg >= 33 and avg < 41:
	print("Your Grade is D")
elif avg >= 21 and avg < 33:
	print("Your Grade is E1")
elif avg >= 0 and avg < 21:
	print("Your Grade is E2")
else:
	print("Invalid Input!")


# In[12]:


import numpy as np

np.array = np.zero


# In[ ]:





# In[ ]:




