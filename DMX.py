import numpy as np
import os

C=[]
T=[]

def binaire (n):                
    sortie = [0,0,0,0,0,0,0,0]
    q = -1
    r = 0
    i = 0    
    
    for i in range (0,8):
        print i
        q = n / 2
        r = n % 2
        sortie[i] =  r
        n = q
        
    return sortie

class Trame:
    def __init__(self,n, h=512):
        self.name = n
        self.height = h
        self.savepath = os.getcwd() + "\\Preps\\"
    
    def new(self):
       self.content = np.zeros((self.height,11))
       return self.content

    def nff(self, fic):
        return np.load(self.savepath + fic + '.npy')
    
    def save(self):
        np.save(self.savepath + self.name,self.content)
        return True
        


def modif_canal(Chn,Val):

    global C
    
    Set = binaire(Val)
    
    for j in range (0,8):
        C[Chn,j+1] = Set[j]


def trame_make():

    global C, T
    
    C = np.reshape(C,5632)

    B = np.loadtxt('break')
    MAB = np.loadtxt('MAB')

    T = np.concatenate((B,MAB,C))




