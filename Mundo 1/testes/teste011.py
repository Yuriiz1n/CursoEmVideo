from random import sample

alu1 = str(input("Primeiro aluno: "))
alu2 = str(input("Segundo aluno: "))
alu3 = str(input("Terceiro aluno: "))
alu4 = str(input("Quarto aluno: "))

alunos = [alu1, alu2, alu3, alu4]

print(f"Ordem de apresentação \n{sample(alunos, 4)}")