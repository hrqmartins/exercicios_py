print("|-----------/-*-\-----------|")
print('|-*-\GRAU DE OBESIDADE /-*-|')
print("|-----------\-*-/-----------|")
Altura = float(input('Qual é a sua altura?: '))
Peso = float(input('Qual é o seu peso corporal?: '))
massa = (Peso/Altura**2)
if massa < 26:
      print ('Grau de Obesidade: Normal.')
elif massa >= 26 and massa < 30:
    print('Grau de Obesidade: Sobrepeso.')
elif massa >= 30:
    print('Grau de Obesidade: Obesidade.')
