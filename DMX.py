import numpy as np
import os

def binaire (n):                
    sortie = [0,0,0,0,0,0,0,0]
    q = -1
    r = 0
    i = 0    
    for i in range (0,8):
        print i
        q = n / 2
        r = n % 2
        sortie[i] =  int(r)
        n = q   
    return sortie

def decimal(a):
    sortie = 0
    for i in range(0,len(a)):
        sortie = sortie + a[i]*2**i
    return str(sortie)



class Trame:
    def __init__(self,nom, selecteur, h=512):
        self.name = nom
        self.height = h
        self.lenght = self.height*11
        self.savepath = os.getcwd() + "\\Preps\\"
        self.content = []
        self.selecteur = selecteur
    
    def new(self):
       self.content = np.zeros((self.height+1,11),int)
       for i in range(0,513):
           self.content[(i,0)] = 1                      
       return self.content

    def nff(self, fic):
        return np.load(self.savepath + fic + '.npy')
    
    def save(self, nom):
        self.name=nom
        np.save(self.savepath + self.name,self.content)
        return True

    def relire(self):
        return np.load(self.savepath + self.name + '.npy')

    def modif_canal(self, Chn, Val):
        if (Chn in range (0,513)):
            Set = binaire(Val)
            for j in range (0,8):
                self.content[Chn,j+1] = Set[j]
            return self.content
        else:
            return False

    def lire_canal(self, Chn):
        return decimal(self.content[Chn,1:9])

    def make(self):
        self.go = np.concatenate((np.loadtxt('break.dmx'),np.loadtxt('MAB.dmx'),np.reshape(self.content,self.lenght)))
        return self.go




