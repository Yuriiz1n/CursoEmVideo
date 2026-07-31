print('Calcule a média')
nota1 = float(input('Nota do trabalho: '))
nota2 = float(input('Nota da prova: '))
media = (nota1 + nota2) /2


print('Média do aluno: {:.1f}'.format(media))


if media <= 5.0:
    print('reprovado')
elif media > 6.0 and media <= 10:
    print('aprovado')