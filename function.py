#!/usr/bin/env python
# coding: utf-8

# In[29]:


from math import *
import math


# In[150]:


def Nom_prenom():
    x=input("Ecrivez votre nom :")
    y=input("Ecrivez votre prénom :")
    
    if type(x)==int:
        return("error")
    else:
        return(x,y)


# In[10]:


def age():
    x=int(input("Quel âge avez vous ?"))
    resultat="Vous aurez 100 ans dans ",100-x,"ans"
    
    return(resultat)


# In[225]:


def volume(rayon,hauteur):
    if type(rayon)!=int or type(hauteur)!=int:
        return("error")
    else:
        return(pi*(rayon*rayon)*hauteur)/3


# In[222]:


def Pair_impaire():
    x=int(input("Entrez un chiffre : "))
    if x%2==0:
        return("Votre chiffre est pair")
    else:
        return("Votre chiffre est impair")


# In[76]:


def fibonacci(x):
    a=0
    b=1
    liste=[0,1]
    for i in range(x-2):
        c=a+b
        liste.append(c)
        a=b
        b=c
    return("La suite fibonacci est : ",liste)
        


# In[53]:


def pgcd_ppmc(a,b):
    div1=[i for i in range(1,a+1) if a%i==0]
    div2=[i for i in range(1,b+1) if b%i==0]
    divfinal=[]
    for j in div1:
        if j in div2:
            divfinal.append(j)
        
    return(max(divfinal),min(divfinal))


# In[220]:


def liste_commun(a,b):
    liste3=[]
    for i in a:
        if i in b:
            liste3.append(i)
    return(liste3)


# In[66]:


def palyndrome(phrase):
    a=[i for i in phrase]
    if a == a[::-1]:
        return("c'est un Palyndrome")
    else:
        return("ce n'est pas un Palyndrome")
    


# In[217]:


def doublon(liste):
    if type(liste)!=list:
        return("ce n'est pas une liste")
    else:
        for i in liste:
            if liste.count(i)>1:
                liste.remove(i)
        return(liste)


# In[207]:


def ip(x):
    try:
        liste=x.split(".")
        
        nombre1=int(liste[0])
        nombre2=int(liste[1])
        nombre3=int(liste[2])
        nombre4=int(liste[3])
        
        if len(liste)!=4:
            print("ce n'est pas bon")
        elif (nombre1>255) or (nombre2>255) or (nombre3>255) or (nombre4>255):
            print("ce chiffre est trop grand")
        elif (nombre1<0) or (nombre2<0) or (nombre3<0) or (nombre4<0):
            print("ce chiffre est trop petit")
        else:
            return ("C'est une addresse valide")
        
        
    except TypeError:
        print("Il y a une erreur dans le type") 
        
    except ValueError:
        print("Il y a une erreur")


# In[185]:


def binaire(x):
    liste=[]
    while (x!=0):
        liste.append(x%2)
        x=x//2        
        
    return(liste)
        
        

