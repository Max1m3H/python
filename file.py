class File():
    def __init__(self):
        self.maFile = []
        self.taille = 0

    def estVide(self):
        return self.taille == 0

    def ajouter(self, x):
        self.maFile.append(x)
        self.taille += 1
        return None

    def extraire(self):
        if self.taille == 0:
            pass
        else:
            x = self.maFile.pop(0)
            self.taille -= 1
            return x
