def deleni(delitel, jmenovatel):
    if jmenovatel != 0:
        vysledek = delitel/jmenovatel
        return vysledek
    else:
        print("Nelze dělit nulou")

x = int(input("Zadejte proměnou a: "))        
y = int(input("Zadejte proměnou b: "))

print("Výsledek je: ", deleni(x,y))