import feladatok
import fajlkezeles

lista = fajlkezeles.lista_letrehozas()
"""
print(lista)

print()

szoveg = fajlkezeles.szovegge_alakit(lista)
print(szoveg)

fajlkezeles.fajlba_mentes(szoveg)
szoveg_lista = fajlkezeles.fajbol_olvas()
print()
"""
print()
#1
db = feladatok.negativ_db(lista)
print(f"A számok között {db}db negatív szám található.")
print()

#2
legn = feladatok.legnagyobb(lista)
print(f"A legnagyobb szám: {legn}")
print()

#3
p = feladatok.paros_lista(lista)
print(f"Páros számok listája: {p}")
print()

#4
ot = feladatok.ottel_oszthato(lista)
print(f"Öttel osztható számok összege : {ot}")
print()

#5
min = feladatok.legkisebb_szam(lista)
print(f"A lekisebb szám: {lista[min]}, és a/az {min}. helyen áll. ")