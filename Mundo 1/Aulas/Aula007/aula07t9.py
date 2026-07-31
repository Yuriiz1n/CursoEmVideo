preco = float(input('Informe o preço do produto? R$'))
desconto = int(input('Qual o desconto desse produto? '))
novo = preco - (preco * desconto / 100)

print(f"o preço do produto com desconto de {desconto}% é R${novo:.2f}")