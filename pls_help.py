import random

body = 0

def nasobeni(a, b):
    vysledek = a*b
    return vysledek

body = 0

def deleni(a, b):
    vysledek = a/b
    return vysledek

def kontrola(vysledek, vysledek_zak):
    global body
    if vysledek == vysledek_zak:
        print("Jsi šikula :)")
        body += 1
        print(body)
    else:
        print("Jejda, spletl jsi si odpoved :(")
        body -= 1
        print (body)
    return body

for i in range(10):

    x = random.randint(1,10)
    y = random.randint(1,10)
    vysledek_zak = int(input(f"{x} * {y} = "))

    vysledek = nasobeni(x,y)
    kontrola(vysledek,vysledek_zak)

print("Koneční body ", body)

for i in range(10):

    x = random.randint(1,10)
    y = random.randint(1,10)
    vysledek_zak = int(input(f"{x} / {y} = "))

    vysledek = deleni(x,y)
    kontrola(vysledek,vysledek_zak)

print("Koneční body ", body)