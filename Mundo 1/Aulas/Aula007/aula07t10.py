salario = float(input('Qual é o salário do funcionário atualmente? R$'))
aumento = int(input('Porcentagem do aumento? '))
novo = salario + (salario * aumento / 100)

print(f'o salário atual do funcionário com {aumento}% de aumento é R${novo:.2f}')