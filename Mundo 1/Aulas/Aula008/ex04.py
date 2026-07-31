import random

aluno1 = str(input("Nome do primeiro aluno(a): "))
aluno2 = str(input("Nome do segundo aluno(a): "))
aluno3 = str(input("Nome do terceiro aluno(a): "))
aluno4 = str(input("Nome do quarto aluno(a): "))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(lista)

print(f"O aluno sorteado para apagar o quadro foi {sorteio}")