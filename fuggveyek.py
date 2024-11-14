def etlap(etel_lista):
    #itt írjuk ki saz ételek neveit
    for i in range(0,len(etel_lista),1):
        print(f"** {etel_lista[i].nev} {etel_lista[i].ar:>10} **")

def atlag_ar(etel_lista):
    osszeg:float=0
    for i in range(0, len(etel_lista),1):
        osszeg+=etel_lista[i].ar
    return osszeg/len(etel_lista)

def legdragabb(etel_lista):
    maxindex=0
    for i in range(0,len(etel_lista),1):
        if etel_lista[maxindex].ar < etel_lista[i].ar:
            maxindex = i
    return maxindex
