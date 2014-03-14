import numpy
import os

def binaire (n):                
    sortie = []
    q = -1
    r = 0    
    for i in range (0,8):
        print i
        quotient = n / 2
        reste = n % 2
        sortie.append(int(reste))
        n = quotient   
    return sortie

def decimal(tableau):
    sortie = 0
    for i in range(0,len(tableau)):
        sortie = sortie + tableau[i]*2**i
    return str(sortie)



class Trame:
    def __init__(self,nom="Trame_vide", selecteur="F1", h=512):
        self.name = nom
        self.height = h+1
        self.lenght = self.height*11
        self.savepath = os.getcwd() + "\\Preps\\"
        self.selecteur = selecteur
        self.content = numpy.zeros((self.height,11),int)
        for i in range(0,self.height):
            self.content[(i,0)] = 1
    
    def new(self):
        pass

    def loadFromFile(self, fichier):
        print numpy.load(fichier)
        return numpy.load(fichier)
    
    def save(self, nom):
        self.name=nom
        numpy.save(self.savepath + self.name,self.content)
        return True

    def relire(self):
        return numpy.load(self.savepath + self.name + '.numpyy')

    def modif_canal(self, Chn, Val):
        if (Chn in range (0,self.height)):
            Set = binaire(Val)
            for j in range (0,8):
                self.content[Chn,j+1] = Set[j]
            return self.content
        else:
            return False

    def lire_canal(self, Chn):
        return decimal(self.content[Chn,1:9])

    def make(self):
        self.go = numpy.concatenate((numpy.loadtxt('break.dmx'),numpy.loadtxt('MAB.dmx'),numpy.reshape(self.content,self.lenght)))
        return self.go




