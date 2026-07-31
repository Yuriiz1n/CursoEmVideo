import time

inicio = time.time()

with open("dados.txt", "r", encoding="utf-8") as f:
    for linha in f:
        print(linha.strip())

fim = time.time()

print("\nTempo sequencial:", fim - inicio)