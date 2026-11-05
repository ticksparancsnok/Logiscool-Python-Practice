"""
Listák, mátrixok, tuple
logikai operátorok and, or, not, demorgan azonosságok
listaműveletek

yield break continue return
"""

import math
import re

list_a = [] #Lista létrehozása (üresen)
list_example = [1,"kettő",True]

def list_tpyes():
    print(type(list_example))
    print(type(list_example[0]))
    print(type(list_example[1]))
    print(type(list_example[2]))
    # Lista minden fajta típust tud tárolni

# Töltsük fel a listát számokkal
def add_to_list(st,en):
    for i in range(st,en+1,1): # "st"-tól 1-esével úgy hogy "en" is ki legyen iratva!
        list_a.append(i)
    print(list_a,sep=" ") # az egyes elemeket " " választja el (separator), az utolsó elem után pedig sortörés következik (end)
    # for ciklus a lista elemeivel
    for j in list_a:
        print(j,end=" ") # itt minden j külön print lenne ezért kell az end=" " és nem a sep.
    print()



def list_operations():
    list_a.extend(list_example) # Amíg az append csak 1 elem hozzáadására képes az extendben több elemet vagy akár egy másik listát is meg tudsz adni
    print(list_a)
    list_a.remove("kettő") # eltávolít minden olyan elemet a listából aminek az értéke: "kettő"
    print(list_a)
    list_a.pop(-1) # eltávolítja a "-1"-edik elemet vagyis az utolsó elemet a listából
    print(list_a)
    list_a[0]=0 # elem felülírása
    print(list_a)
    list_a.sort() # elemek rendezése növekvő sorrendbe
    print(list_a)
    list_a.reverse() # Fordított elemsorrend
    print(list_a) 
    # lista szeletelése:
    print(list_a[0])
    print(list_a[4])
    print(list_a[-1])
    print(list_a[2:5])
    print(list_a[4:])
    print(list_a[:5])
    print(list_a[0:-1:2])
    print(list_a[::-1])
    print(list_a[::-2])
    # Miscellanious:
    print(len(list_a)) # lista hosszának megadása


def tuple_things():
    # Tuple - Olyan speciális lista amely értékeit nem lehet módosítani létrehozás után
    tuple_minta = ("Alma","Banán","Citrom")
    print(tuple_minta)

def dictionary():
    dict_minta = {"name" : "John", "age(yrs)" : 36, "Height(cm)" : 145, "Weight(kg)" : 57}
    print(dict_minta.get("age(yrs)", "Nincs ilyen adat."))

def matrices():
    # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    matrix_a = []
    rows = int(input("Mennyi sor legyen? "))
    for i in range(rows):
        matrix_a.append([])
    cols = int(input("Mennyi oszlop legyen? "))
    for row in matrix_a:
        for j in range(cols):
            row.append(0)
    print(matrix_a)