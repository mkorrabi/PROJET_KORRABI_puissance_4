# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from puissance4 import Plateau,Joueur_Aleatoire,monte_carlo


joueur1=Joueur_Aleatoire()
joueur2=Joueur_Aleatoire()
joueur1.initJoueur(1)
joueur2.initJoueur(-1)
nb_parties =100
"""
pla=Plateau()
pla.initPlateau(4,3)

res=pla.run(1,-1)
if res==1:
    print("Le joueur 1 a rempoté la partie!!!")
elif res==-1:
    print("Le joueur 2 a rempoté la partie!!!")
else :
    print("Match null!")
#res=pla.run2(1,-1)
"""
i=0
win1=[]
win2=[]

"""
#######parties aleatoires
def run_alea(plateau,joueur1,joueur2):
    cpt=0
    while (pla.is_finished()==False):


        joueur1.play_joueur(plateau)
        joueur2.play_joueur(plateau)
        cpt=cpt+1

    return pla.has_won(),cpt


cpt_p=0

res= run_alea(pla,joueur1,joueur2)
if res[0]==1:
    print("Le joueur 1 a rempoté la partie!!!")
elif res[0]==-1:
    print("Le joueur 2 a rempoté la partie!!!")
else :
    print("Match null!")



while i<nb_parties:
    pla=Plateau()
    pla.initPlateau(7,6)
    res=run_alea(pla,joueur1,joueur2)
    if res[0]==1:
        win1.append(res[1])
    elif res[0]==-1:
        win2.append(res[1])
    elif res[0]==0:
        cpt_p=cpt_p+1
    i=i+1
    print(i)
    print("win1:",win1)
    print("win2",win2)

    #pla.reset()
    pla=Plateau()
    pla.initPlateau(7,6)

print ("la probabilité d'un match null est de ",cpt_p/nb_parties)

print("win 1 proba:",len(win1)/nb_parties)
print("win 2 proba:",len(win2)/nb_parties)
# #histograme
plt.hist(win1)
plt.xlabel('coups')
plt.ylabel('nb_partie_gagn')
plt.title('winner1')
plt.show()

plt.hist(win2)
plt.xlabel('coups')
plt.ylabel('nb_partie_gagn')
plt.title('winner2')
plt.show()

"""



"""
####parties alea_vs_monte_carlo

pla2=Plateau()
pla2.initPlateau(7,6)
joueur_monte_carlo=monte_carlo()
joueur_monte_carlo._init_(1,20)


liste_coup_opt=[]

def run_alea_vs_monte(plateau,joueur2,joueur_monte_carlo):
    cpt=0
    while (plateau.is_finished()==False):


        joueur2.play_joueur(plateau)
        x_opt=joueur_monte_carlo.play_monte_carlo(plateau,joueur2)
        print("#########on joue le coup  ")
        plateau.play(x_opt,joueur_monte_carlo.num)
        print("#########on aaaa jouer le coup  ")
        liste_coup_opt.append(x_opt)

        cpt=cpt+1


    print ("le gagant est ",plateau.has_won())
    print ("nombre de coup du gagnant dans cette partie est",cpt)
    return plateau.has_won(),cpt


res2= run_alea_vs_monte(pla2,joueur2,joueur_monte_carlo)
if res2[0]==-1:
    print("Le joueur_alea a rempoté la partie!!!")
elif res2[0]==1:
    print("monte_carlo  a rempoté la partie!!!")
else :
    print("Match null!")
print ("liste_coup_opt",liste_coup_opt)


cpt=0
while i<nb_parties:
    pla=Plateau()
    pla.initPlateau(7,6)
    res2= run_alea_vs_monte(pla,joueur2,joueur_monte_carlo)
    if res2[0]==-1:
        win2.append(res2[1])

        print("Le joueur_alea a rempoté la partie!!!")
    elif res2[0]==1:
        win1.append(res2[1])
        print("monte_carlo  a rempoté la partie!!!")
    else :
        cpt=cpt+1
        print("Match null!")
        print ("nb match nul ",cpt)
    print ("liste_coup_opt",liste_coup_opt)
    i=i+1
print("win1_monte carlo ",win1)
print("win2_alea",win2)



#histograme et proba


    #pla.reset()

print ("la probabilité d'un match nul est de ",cpt/nb_parties
)
#plt.hist(win1, range = (0, max(win1)),bins = max(win2), color = 'yellow',
            #edgecolor = 'red')

print("win 1 proba:",len(win1)/nb_parties)
print("win 2 proba:",len(win2)/nb_parties)

plt.hist(win1)
plt.xlabel('coups')
plt.ylabel('nb_partie_gagn')
plt.title('monte_carlo')
plt.show()

plt.hist(win2)
plt.xlabel('coups')
plt.ylabel('nb_partie_gagn')
plt.title('alea')
plt.show()

"""


#####parties monte_carlo vs monte_carlo


pla3=Plateau()
pla3.initPlateau(7,6)
joueur1_monte_carlo=monte_carlo()
joueur1_monte_carlo._init_(1,20)

joueur2_monte_carlo=monte_carlo()
joueur2_monte_carlo._init_(-1,20)

def run_monte_vs_monte(plateau,joueur1_monte_carlo,joueur2_monte_carlo):
    cpt=0
    while (plateau.is_finished()==False):


        x1_opt=joueur1_monte_carlo.play_monte_carlo(plateau,joueur2_monte_carlo)
        print ("##########le joueur1 joue le coup x1_opt:",x1_opt)
        plateau.play(x1_opt,joueur1_monte_carlo.num)

        x2_opt=joueur2_monte_carlo.play_monte_carlo(plateau,joueur1_monte_carlo)
        print ("##########le joueur2 joue le coup x2_opt:",x2_opt)
        plateau.play(x2_opt,joueur2_monte_carlo.num)
        cpt=cpt+1



    return plateau.has_won(),cpt

"""
res2=run_monte_vs_monte(pla3,joueur1_monte_carlo,joueur2_monte_carlo)
if res2[0]==1:
    print("monte_carlo_1 a rempoté la partie!!!")
elif res2[0]==-1:
    print("monte_carlo_2  a rempoté la partie!!!")
else :
    print("Match null!")

"""

cpt=0
while i<nb_parties:
    pla=Plateau()
    pla.initPlateau(7,6)
    res2=run_monte_vs_monte(pla,joueur1_monte_carlo,joueur2_monte_carlo)
    if res2[0]==-1:
        win2.append(res2[1])

        print("monte_carlo_1 a rempoté la partie!!!")
    elif res2[0]==1:
        win1.append(res2[1])
        print("monte_carlo_2 a rempoté la partie!!!")
    else :
        cpt=cpt+1
        print("Match null!")
        print ("nb match nul ",cpt)

    i=i+1
    print("###########################",i)
print("win1_monte carlo 1",win1)
print("win1_monte carlo 2",win2)
print ("la probabilite d'un match nul est de ",cpt)

print("win 1 proba:",len(win1)/nb_parties)
print("win 2 proba:",len(win2)/nb_parties)

plt.hist(win1)
plt.xlabel('coups')
plt.ylabel('nb_partie_gagn')
plt.title('monte_carlo1')
plt.show()

plt.hist(win2)
plt.xlabel('coups')
plt.ylabel('nb_partie_gagn')
plt.title('monte_carlo2')
plt.show()