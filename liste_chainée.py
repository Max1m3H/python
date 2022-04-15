'''classes de Maillon et de listes chainées'''

class Maillon:

    def __init__(self,valeur,suivant=-1):
        self.val=valeur
        self.suiv=suivant

    def __str__(self):
        return str(self.val)+"-"+str(self.suiv)


class ListeChainee:

    def __init__(self,premiere):
        self.prem = Maillon(premiere)

    def Ajoute_fin(self,valeur):
        s=self.prem
        while s.suiv !=-1:
            s=s.suiv
        s.suiv=Maillon(valeur)

    def tete(self):
        return self.prem.val

    def queue(self): 
        if self.prem.suiv == None:
            return None
        else:
            return str(self.prem.suiv)

    def Ajoute_debut(self,valeur):
        self.prem = Maillon(valeur,self.prem)

    def longueur(self):
        taille = 1
        s=self.prem
        while s.suiv !=-1:
            taille+=1
            s=s.suiv
        return taille

    def __str__(self):
        s=self.prem
        liste=str(s.val)
        while s.suiv !=-1:
            s=s.suiv
            liste+=" , "+str(s.val)
        return liste

#    def __str__(self):
#        return str(self.prem)[:-3]
