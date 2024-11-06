import random
def lista_letrehozas():
    szamok = []
    for i in range(100):
        szam:int = int(random.random()*201) - 50
        szamok.append(szam)
    return szamok

def szovegge_alakit(lista):
    szoveg:str = ""
    for i in range(1, len(lista), 1):
        if (i<len(lista)-1):
            szoveg +=f"{lista[i]}; "
        else:
            szoveg +=f"{lista[i]}"
    return szoveg
    
def fajlba_mentes(szoveg):
    fajlom = open("adatok.txt", "w", encoding='utf-8')
    fajlom.write(szoveg)
    fajlom.close()

def fajbol_olvas():
    fajlom = open("adatok.txt", "r", encoding='utf-8')
    szoveg_fajlbol:str = fajlom.read()
    lista = szoveg_fajlbol.split(";")

    sz_lista:int = []
    for i in range(0, len(lista), 1):
        szam:int = int(lista[i].strip())
        sz_lista.append(szam)

    #print(szoveg_fajlbol)
    print(sz_lista)
    fajlom.close()
    return sz_lista