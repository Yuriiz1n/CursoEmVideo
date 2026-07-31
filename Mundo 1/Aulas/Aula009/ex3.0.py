import time

linha_desejada = int(input("Digite o número da linha: "))

inicio = time.time()

with open("dados.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()

    if 0 < linha_desejada <= len(linhas):
        print("Linha:", linhas[linha_desejada - 1].strip())
    else:
        print("Linha inválida")

fim = time.time()

print("Tempo acesso direto:", fim - inicio)