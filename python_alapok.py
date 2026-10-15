# Egysoros komment
"""
Többsoros
komment
"""
import math


def input_output(): # Függvény definiálása
    var1 = input("Kérek egy inputot! ") # létrehozol egy változót és a felhasználó ad neki egy értéket. (változó típusa string)
    print("A változó " + var1) # konzolra kinyomtatás szöveg összefűzéssel
    print("A változó" , var1) # konzolra kinyomtatás külön tagokként (elválasztó " ")

def io_return():
    a = input("Kérek egy inputot! ")
    return a # a függvény térjen vissza a változó értékével

def basic_op():
    a = int(input("Kérek egy inputot! ")) # a megadott változót számként kezelje
    b = int(io_return())
    c = int(io_return())
    print("A számok összege", a+b+c) # kiírja a számok összegét
    szorzat = a*b*c
    print("A számok szorzata", szorzat) # kiírja a számok szorzatát

"""
szám műveletek:
    összeadás +
    értéknövelés +=
    kivonás -
    értékcsökkentés -=
    szorzás *
    sokszorozás *=
    osztás /
    tördelés /=
    maradékos osztás %
    osztás egészre kerekítve //
    hatványozás **

szám összehasonlítások
    egyenlővé tétel =
    egyenlőség vizsgálat ==
    nem egyenlő !=
    kisebb nagyob < >
    kisebb nagyobb egyenlő <= >=

szöveg műveletek
    összefűzés +
    sortörés \n
    upper() "alma".upper()
    lower()
    capitalize()
    split('')
"""

def while_ism(): # Printeljük a számokat 1-10 között while loop segítségével
    i = 1 # Létrehozzuk az indexet
    while i <= 10: # A while loop addig ismétel amíg a benne lévő feltétel igaz.
        print(i)
        i+=1

    j = 1
    while j < 11: 
        print(j)
        j+=1

    k = 1
    while True:
        print(k)
        k+=1
        if k == 11:
            break

def for_ism(): # Printeljük a számokat 100-1 között 7-esével
    for i in range(100,0,-7): # i -> index változó; range ->(100-tól, 1-ig, -7-lépéssel)
        print(i)

def elagazas():
    a = int(input("Kérek egy számot! \n"))
    if a > 0: # Ha a feltétel igaz
        print("A szám pozítív")

    elif a == 0: # különben ha ez a feltétel igaz
        print("A szám 0")

    elif a > 0: # Soha nem fog futni mert a fentebbi feltétel már kezeli
        print("lol") 

    else: # ha egyik fentebbi feltétel sem igaz
        print("A szám negatív")

def tipus_con_szam():
    a = 400 # változó létrehozása számként
    print(a)
    print(type(a)) # kiprintelem a típust
    a = float(a)
    print(a)
    print(type(a))
    a += 0.99999
    b = a 
    print(a)
    a = int(a) # levágja a törtrészt
    print(a)
    b = round(b) # kerekít felfele vagy lefele, és átalakítja int-é
    print(b)
    print(type(b))

def tipus_con_szoveg():
    a = str(75368) 
    print(a)
    print(type(a))

    a = list(a) # stringből csinálunk listát
    print(a)
    print(type(a))

    a = "".join(a) # listából csinál stringet ("" jelek közé rakjuk az elválasztót)
    print(a)
    print(type(a))

def tipus_con_bool():
    a = True
    b = False
    c = 5
    print(type(a))
    print(type(b))
    print(type(c))
    a = int(a)
    print(a)
    b = int(b)
    print(b)
    c = bool(c)
    print(c)








"""
változó típuskonvertálás
logikai operátorok and, or, not, demorgan azonosságok
"""



