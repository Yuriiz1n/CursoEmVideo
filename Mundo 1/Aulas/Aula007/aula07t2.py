n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
po = n1 ** n2

print('A soma desse valor é {}, o produto vale {} e a divisão é {:.3f}'.format(s, m, d), end='. ')
print('Divisão inteira {} e potência {}.'.format(di, po))