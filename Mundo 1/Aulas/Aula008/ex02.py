from math import sqrt
oposto = float(input("Comprimento do cateto oposto: "))
adjacente = float(input("Comprimento do cateto adjacnete: "))
po = oposto ** 2 + adjacente ** 2
hi = sqrt(po)

print(f"A hipotenusa mede {hi:.2f}")