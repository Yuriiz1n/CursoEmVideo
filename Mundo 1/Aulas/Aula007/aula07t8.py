largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura

print(f"Sua parede possui uma dimensão de {largura:.1f}x{altura:.2f} e sua área é de {area:.3f}m²")
print(f"Para pintar esssa parede serão necessários {area / 2:.2f}l de tinta")