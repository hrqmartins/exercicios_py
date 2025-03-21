print('--------------')
print('Faixa Etária')
print('--------------')

idade = int(input('Idade: '))
if idade < 12:
    print('Criança.')
elif idade < 18:
    print('Adoslecente')
elif idade < 60:
    print('Adulto')
else:
    print('Idoso')
