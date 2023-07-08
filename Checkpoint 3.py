#!/usr/bin/env python
# coding: utf-8

# # EX 1

# In[ ]:


largeur = int(input("Entrez la largeur de la liste :"))
liste = []

for i in range(largeur):
    if i == 0:
        print("Entrez la", i+1, "ère valeur de la liste :")
    else:
        print("Entrez la", i+1, "ème valeur de la liste :")
    valeur = int(input())
    liste.append(valeur)
    
result = liste[0]
for i in range(1,largeur):
    result = result *liste[i]

print("Resultat =", result)


# # EX 2

# In[ ]:


def elem2(elem):
    return elem[1]

largeur = int(input("Entrez la largeur de la liste :"))
liste = []

for i in range(largeur):
        T=()
        print("Entrez la 1 ère valeur de tuple :")
        a=int(input())
        T=(a,)
        print("Entrez la 2 ème valeur de tuple :")
        b=int(input())
        T=T+(b,)
        

        liste.append(T)
    

liste.sort(reverse=True)
    
print(liste)


# # EX 3

# In[ ]:


d1 = {}
d2 = {}
d3 = {}

largeur1 = int(input("Entrez la largeur du dictionnaire :"))

for i in range(largeur1):
    if i == 0:
        print("Entrez le", i+1, "er key du dictionnaire :")
        k=input()
        print("Entrez la", i+1, "ère valeur du dictionnaire :")
        v=int(input())
        d1[k]=v
    else:
        print("Entrez le", i+1, "ème key du dictionnaire :")
        k=input()
        print("Entrez la", i+1, "ème valeur du dictionnaire :")
        v=int(input())
        d1[k]=v

largeur2 = int(input("Entrez la largeur du dictionnaire :"))

for i in range(largeur2):
    if i == 0:
        print("Entrez le", i+1, "er key du dictionnaire :")
        k=input()
        print("Entrez la", i+1, "ère valeur du dictionnaire :")
        v=int(input())
        d1[k]=v
    else:
        print("Entrez le", i+1, "ème key du dictionnaire :")
        k=input()
        print("Entrez la", i+1, "ème valeur du dictionnaire :")
        v=int(input())
        d1[k]=v
d3=d1
keys=d2.keys()
keys2=d3.keys()
for k in keys:
    if k in keys2:
          d3[k]+=d2[k]
    else:
          d3[k]=d2[k]


# # EX 4

# In[ ]:


nb = int(input("Entrer un nombre : "))
liste = {}

for i in range(1, nb+1):
    liste[i]= i*i
print(liste)


# # EX 5 

# In[ ]:


def elem2(elem):
    return elem[1]

largeur = int(input("Entrez la largeur de la liste :"))
liste = []

for i in range(largeur):
        T=()
        print("Entrez la 1 ère valeur de tuple :")
        a=input()
        T=(a,)
        print("Entrez la 2 ème valeur de tuple :")
        b=float(input())
        T=T+(b,)
        

        liste.append(T)
    

liste.sort(key=elem2)
    
print(liste)

