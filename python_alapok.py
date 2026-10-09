# Egysoros komment
"""
Többsoros
komment
"""

def input_output(): # Függvény definiálása
    var1 = input("Kérek egy inputot! ") # létrehozol egy változót és a felhasználó ad neki egy értéket. (változó típusa string)
    print("A változó " + var1) # konzolra kinyomtatás szöveg összefűzéssel
    print("A változó" , var1) # konzolra kinyomtatás külön tagokként (elválasztó " ")

def io_adv():
    a = input("Kérek egy inputot! ")
    return a # a függvény térjen vissza a változó értékével

def basic_op():
    a = int(input("Kérek egy inputot! ")) # a megadott változót számként kezelje
    b = int(io_adv())
    c = int(io_adv())
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
"""
print paraméterek sep, end
listák
tuple
bitwise
változó típuskonvertálás
for while loopok
if elif else elágazás
logikai operátorok and, or, not, demorgan azonosságok
file műveletek
yield break continue return
mátrix műveletek
dictionaries
try exept
"""



