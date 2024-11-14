'''1. lépés: osztály étrehozása:'''
class Etel:
    def __init__(self, nev:str="", ar:int=1000):
        #konsrutor feladata: létrehozza a konkrt példányt a konkrét adatokkal a tervrajzból
        #beállítsa az adattagokat - objektum tulajdonságok értkei
        self.nev = nev
        self.ar = ar
        self.allapot = "folyamatban"

    def keszul(self):
        self.allapot = "kész"
    
    def __str__(self):
        return f"Étel neve: {self.nev}, Ár: {self.ar} Ft, Állapot: {self.allapot}"
    
