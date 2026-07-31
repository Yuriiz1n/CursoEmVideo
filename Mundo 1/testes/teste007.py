n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite outro valor: '))
n4 = int(input('Digite mais um: '))
re = n2 * n3
re2 = re / n4
re3 = n1 + re2

print(f"{n1} + ({n2} * {n3}) / {n4}")
print(f"{n1} + {re} / {n4}")
print(f"{n1} + {re2}")
print(f"{re3}")
