print('--------------------------')
print('*-* Calculando a Média *-*')
print('--------------------------')

#entrada de dados
cp1 = float(input('Checkpoint 1: '))
cp2 = float(input('Checkpoint 2: '))
cp3 = float(input('Checkpoint 3: '))
faltas = int(input('Faltas: '))

#processamento
media = (cp1 + cp2 + cp3)/3

#saída de dados
print('Média: ', media)
if (media >= 6 and faltas <=18):
    print('Aprovado!!!!')
else:
    print('Reprovado!!! ')
