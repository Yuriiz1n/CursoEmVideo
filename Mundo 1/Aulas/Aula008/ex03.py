import math
angulo = float(input("Digite o valor de um ângulo: "))
seno = math.sin(math.radians(angulo))
print(f"O ângulo de {angulo} tem o Seno de {seno:.2f}")
coss = math.cos(math.radians(angulo))
print(f"O ângulo de {angulo} tem o Cosseno de {coss:.2f}")
tan = math.tan(math.radians(angulo))
print(f"O ângulo de {angulo} tem a Tangente de {tan:.2f}")
