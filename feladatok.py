"""
1. negatív db
2. legnagyobb
3. paros lista
4. öttel oszthatók összege
5. hányadik helyen áll a legkisebb szám
"""
def negativ_db(szoveg_lista):
    db:int = 0
    for i in range(0, len(szoveg_lista), 1):
        if (szoveg_lista[i] < 0):
            db += 1
    return db

def legnagyobb(lista):
    max_index:int = 0
    for i in range(0, len(lista), 1):
        if (lista[i] > lista[max_index]):
            max_index = i
    return lista[max_index]

def paros_lista(lista):
    parosak = []
    for i in range(0, len(lista), 1):
        if lista[i] % 2 == 0:
            parosak.append(lista[i])
    return parosak

def ottel_oszthato(lista):
    otos:int = 0
    for i in range(0, len(lista), 1):
        if lista[i] % 5 == 0:
            otos += lista[i]
    return otos

def legkisebb_szam(lista):
    min_index:int = 0
    for i in range(0, len(lista), 1):
        if (lista[i] < lista[min_index]):
            min_index = i
    return min_index