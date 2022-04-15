class Pile:
    def __init__(self):
        self.maPile = []
        self.taille = 0
	
    def estVide(self):
        return self.taille == 0

    def ajouter(self, x):
        self.maPile.append(x)
        self.taille += 1
        return None
	
    def extraire(self):
        if self.taille == 0:
            pass
        else:
            x = self.maPile.pop()
            self.taille -= 1
            return x
