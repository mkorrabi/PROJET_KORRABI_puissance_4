import numpy as np 
import matplotlib 
from random import *
import copy

def nb_quadruplets(nb_colonnes,nb_lignes):
    res=[]
    quadr=()
    # i pour les lignes et j pour les colonnes
    # horizontalement
    for i in range(nb_lignes):
        for j in range(0,(nb_colonnes-4)+1):	
            quadr=quadr+( (i,j),(i,j+1),(i,j+2),(i,j+3))	
            res.append(quadr)
            quadr=()
    #verticalement
    for j in range(nb_colonnes):
        for i in range(0,nb_lignes-4+1):	
            quadr=quadr+((i,j),(i+1,j),(i+2,j),(i+3,j))	
            res.append(quadr)
            quadr=() 
    quadr_gauche=()
    quadr_droite=()
    #diagonal
    for j in range(nb_colonnes-4+1):
        for i in range(0,nb_lignes-4+1):	
            quadr_gauche=quadr_gauche+((i,j),(i+1,j+1),(i+2,j+2),(i+3,j+3))	
            quadr_droite=quadr_droite+((nb_lignes-(i+1),j),(nb_lignes-(i+2),j+1),(nb_lignes-(i+3),j+2),(nb_lignes-(i+4),j+3))
            res.append(quadr_gauche)
            res.append(quadr_droite)
            quadr_gauche=()
            quadr_droite=()
    
    return res

class Plateau :
    
    def initPlateau(self,nb_colonnes,nb_lignes):
        self.l=nb_lignes
        self.c=nb_colonnes
        self.tab=np.zeros((nb_lignes,nb_colonnes))
        self.nom="plateau"
        self.liste=nb_quadruplets(nb_colonnes,nb_lignes)
    
    def reset(self):
        self.tab=0
    
    def has_won(self):
        for ((x1,y1),(x2,y2),(x3,y3),(x4,y4)) in self.liste :
            if (np.abs(self.tab[(x1,x2,x3,x4),(y1,y2,y3,y4)].sum()==4)):
                return self.tab[x1][y1] #renvoie 1 si le gagnat est le joueur1 ou -1 si c'est le joueur2
            if (np.abs(self.tab[(x1,x2,x3,x4),(y1,y2,y3,y4)].sum()==(-4))):
                return self.tab[x1][y1]
        
        return 0 #on n a pas de gagnant

    def play(self,x,joueur):
        #x represente la colonne 
        #liste_ligne
        liste_ligne=np.where(self.tab[:,(x-1)]==0)[0]
        if(len(liste_ligne)==0):
            print("La colonne est pleine\n")
        else :
            l=np.where(self.tab[:,(x-1)]==0)[0].argmax()
            self.tab[l][x-1]=joueur #on place le jeton a la place designee
            print(self.tab)
            return l
    
    def is_finished(self):
        if(self.has_won()!=0):#on a un gagnant 
            return True
        return ((self.tab==0).sum())==0
    

    def run(self,joueur1,joueur2):
        while (self.is_finished()==False):
            #x=randint(0,self.c)
        
            x=int (input("jour1 choisissez la colonne :"))
            print(x)
            while (0>x) and (self.c<x):
                print("le nombre de colonne choisit est invalide recommencer!")
                x=int (input("jour1 choisissez la colonne :"))

            self.play(x,joueur1)
            #y=randint(0,self.c)

            print("jour1 choisissez la colonne :")
            y=int (input("jour2 choisissez la colonne :"))
            
            while (0>y) and (self.c<y):
                print("le nombre de colonne choisit est invalide recommencer!")
                y=int (input("jour2 choisissez la colonne :"))            
            self.play(y,joueur2)
        return self.has_won()
    
    
    


class Joueur_Aleatoire:
    def initJoueur(self,numero_joueur):
        self.num=numero_joueur 
        
    def play_joueur(self,plateau):
        
        x=randint(0,plateau.c)
        y=plateau.play(x,self.num)
       
  


class monte_carlo:
    def _init_(self,numero_joueur,nb_partie):
        self.num=numero_joueur 
        self.nb_partie=nb_partie
        
        self.monte_car_alea=Joueur_Aleatoire()
        self.monte_car_alea.initJoueur(self.num)


        
    def play_monte_carlo(self,plateau,joueuradverse ) :
        list_coup_gain={}
        list_coup_rend={}
        x_opt=0
        p_opt=0
        joueur_alea=Joueur_Aleatoire()
        joueur_alea.initJoueur(joueuradverse.num)
        i=0
        j=0
        while j <= plateau.c:
            list_coup_gain[j]=0
            list_coup_rend[j]=0
            j=j+1
    
    
        while i <self.nb_partie:
            x=randint(0,plateau.c)
            pla=plateau 
            pla.play(x,self.num)#on joue le coup
            while (pla.is_finished()==False):#tant que la pertie n'est pas fini 
            
                joueur_alea.play_joueur(pla)
                self.monte_car_alea.play_joueur(pla)
                

            #fin d'une parti
            print ("celui qui a gagner est ", pla.has_won())
            if( pla.has_won()==1):
                list_coup_gain[x]=list_coup_gain[x]+1
                
            i=i+1
        t=0
        print (list_coup_gain)
        while t<= plateau.c:
            list_coup_rend[t]= list_coup_gain[t]/self.nb_partie
            t=t+1
        for xx,p in list_coup_rend.items():
            if p > p_opt:
                p_opt=p
                x_opt=xx
        print (list_coup_rend)
        print("x optimale",x_opt)
        return x_opt
    

        
        


"""

      
    def play_monte_carlo(self,plateau,joueuradverse ) :
        list_coup_gain={}
        list_coup_rend={}
        x_opt=0
        p_opt=0
        joueur_alea=Joueur_Aleatoire()
        joueur_alea.initJoueur(joueuradverse.num)
        i=0
        j=0
        while j <= plateau.c:
            list_coup_gain[j]=0
            list_coup_rend[j]=0
            j=j+1
        while i <self.nb_partie:
            x=randint(0,plateau.c)
            pla=copy.deepcopy(plateau) 
            pla.play(x,self.num)#on joue le coup
            while (pla.is_finished()==False):#tant que la pertie n'est pas fini 
            
                joueur_alea.play_joueur(pla)
                self.monte_car_alea.play_joueur(pla)
                

            #fin d'une parti
            
            if( pla.has_won()==1):
                list_coup_gain[x]=list_coup_gain[x]+1
            i=i+1
        t=0
        print ("liste_coup_gain",list_coup_gain)
        while t<= plateau.c:
            list_coup_rend[t]= list_coup_gain[t]/self.nb_partie
            t=t+1
        for xx,p in list_coup_rend.items():
            if p > p_opt:
                p_opt=p
                x_opt=xx
        print ("xopt",x_opt)
        return x_opt

"""
   

    












                    
               
                


   








