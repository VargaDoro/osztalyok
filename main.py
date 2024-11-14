'''hozz létre egy osztályzatok listát 
osztályzatok_lista=[3,4,5,2,3,4,5,4]
nevek=["Béla", "Jenő", "Ági", "Rozi",]

nevek és a nevekhe tartozó osztályzatok összetartoznak

etelek=["húsleves","krumplist"]
ar=[1234, 3456]

Új adatszerkezet ami egybe tudja kezelni sz összetartozó adatokat

szemely = {nev: "Béla", osztalyzat: 3}

kaja1= {nev:"húsleves", ar: 1234, elkeszitési_ido: 2}
kaja2= {nev:"krumplist", ar: 2345, elkesztitesi_ido: 0.5}

objektumok - tulajdonságokkal (főnevek) és visekedéssel (cselekvés) bíró adatszerkezet

Kászítünk egy sablont ami alapján le tudjuk gyártni a konkrét egyedeket.
OSZTÁLY - sablon - osztály - tervrajz
OBJEKTUM - konkrét egyedek - objektumok - konkrét termék'''

from Etel import Etel
import fuggveyek

'''2. lépés: létrehozzuk a konkrét példányt a tervrajz alapján:'''
etel_lista=[]
etel_lista.append(Etel("húsleves",1234))
etel_lista.append(Etel("krumplis",2345))
etel_lista.append(Etel("rantotthus",1230))
etel_lista.append(Etel("palacsinta",4560))

'''print("Szia én vagyok a "+ etel_lista[0].nev + " Az állapotom "+ etel_lista[0].allapot)
etel1.keszul()
print("Szia én vagyok a "+ etel1.nev + " Az állapotom "+ etel1.allapot)
print("Szia én vagyok a "+ etel2.nev + " Az állapotom "+ etel2.allapot)

Írj metódu st, amely paraméterekben  megkapja a listát és kiija az ételek és árait látványos formában

fuggveyek.etlap(etel_lista)

Írj metódust, amely paraméterekben megkapja a listát és megmondja az ételek átlagárát és a legdrágább étel nevét

atlagar=fuggveyek.atlag_ar(etel_lista)
print(f"At ételek átlagára: {atlagar}")

maxi=fuggveyek.legdragabb(etel_lista)
print(f"A legdrágább étel neve és ára: {etel_lista[maxi].nev}, {etel_lista[maxi].ar}")

print(etel_lista[0])'''

'''Hozz létre egy alkalmazot osztályt amelyikben az alábbi infókat lehet tárolni egy cég dolgozóiról: 
nev
szul_datum
fizetes
pozicio
kor

Készíts hozzá egy metódust, ami megmondja az adott ember korát
__str__

Hozz létre legalább 5 embert - listába
1. feladat: mennyi az össz fizetés?
2. Hány éves  alegidősebb ember?
3. Hány ember van beosztott pozicíóba?
4. Kinek a legalacsonyabb a fizetése?
+ Az osztálynak legyen egy fizets emelés metódusa, amelyik a fizetést megemeli a paraméterben megadott százalék értékével.
A legkisebb fizetésű ember fizetését emeld meg 20%-kal!'''

from Alkalmazott import Alkalmazott
import fuggvenyek

dolgozok_lista=[]
dolgozok_lista.append(Alkalmazott("Kovács János", 1975, 700000, "Programozó"))
dolgozok_lista.append(Alkalmazott("Varga Péter", 1980, 400000, "HR"))
dolgozok_lista.append(Alkalmazott("Szabó Tünde", 1985, 450000, "Beosztott"))
dolgozok_lista.append(Alkalmazott("Asztalos Virág", 1990, 300000, "Takarító"))
dolgozok_lista.append(Alkalmazott("Szabó Tibor", 1974, 1000000, "Igazgató"))

print(dolgozok_lista[0])

osszfizu=fuggvenyek.ossz_fizu(dolgozok_lista)
print(f"A dolgozók össz. fizetése: {osszfizu}")

legi=fuggvenyek.legidosebb(dolgozok_lista)
print(f"A legidősebb dolgozó: {dolgozok_lista[legi].nev}, kora: {dolgozok_lista[legi].kor}")

beosztott=fuggvenyek.beosztott(dolgozok_lista)
print(f"Beosztott bozicíóban {dolgozok_lista[beosztott].nev} van.")

legalacsonyabbfizu=fuggvenyek.legalacsoyabb(dolgozok_lista)
print(f"A legalacsonyabb fizetéssel {dolgozok_lista[legalacsonyabbfizu].nev} rendelkezik.")

fuggvenyek.fizuemeles(dolgozok_lista, 20)
print(f"Az emelt fizetések:")
print(f"{dolgozok_lista[0].nev}-nek az emelt fizetése {dolgozok_lista[0].fizetes}")
print(f"{dolgozok_lista[1].nev}-nek az emelt fizetése {dolgozok_lista[1].fizetes}")
print(f"{dolgozok_lista[2].nev}-nek az emelt fizetése {dolgozok_lista[2].fizetes}")
print(f"{dolgozok_lista[3].nev}-nek az emelt fizetése {dolgozok_lista[3].fizetes}")
print(f"{dolgozok_lista[4].nev}-nek az emelt fizetése {dolgozok_lista[4].fizetes}")