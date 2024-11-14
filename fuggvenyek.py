from Alkalmazott import Alkalmazott

#1. feladat: mennyi az össz fizetés?
def ossz_fizu(dolgozo_lista):
    osszeg:float=0
    for i in range(0, len(dolgozo_lista),1):
        osszeg+=dolgozo_lista[i].fizetes
    return osszeg

#2. Hány éves a legidősebb ember?
def legidosebb(lista):
    legi=0
    for i in range(0,len(lista),1):
        if lista[legi].kor < lista[i].kor:
            legi=i
    return legi

#3. Hány ember van beosztott pozicíóba?
def beosztott(lista):
    for i in range(0,len(lista),1):
        if "Beosztott" == lista[i].pozicio:
            beosztott = i
    return beosztott

#4. Kinek a legalacsonyabb a fizetése?
def legalacsoyabb(lista):
    legaf=0
    for i in range(0,len(lista),1):
        if lista[legaf].fizetes > lista[i].fizetes:
            legaf = i
    return legaf

#+Az osztálynak legyen egy fizets emelés metódusa, amelyik a fizetést megemeli a paraméterben megadott százalék értékével.
#A legkisebb fizetésű ember fizetését emeld meg 20%-kal!

def fizuemeles(lista, szam:int=20):
    for i in range(0,len(lista),1):
        emeles = lista[i].fizetes/100 * szam
        lista[i].fizetes = lista[i].fizetes + emeles
        #lista[i].fizetes=Alkalmazott.fizetes_emeles(emeles, emeles)
   

        