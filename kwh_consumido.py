print('-=-=-=-=-=-=-=-=-=-=-=-=-')
print('*-* ENERGIA ELETRICA *-*')
print('-=-=-=-=-=-=-=-=-=-=-=-=-')
kwhConta = int(input('Quantos kWh você consumiu: '))
if kwhConta < 150:
    total = 11.90 + (kwhConta * 0.20)
    print('Valor da Conta: ', total)
elif kwhConta >= 150 and kwhConta < 500:
    total2 = 11.90 + (kwhConta * 0.25)
    print('Valor da Conta: ', total2)
elif kwhConta >= 500:
    total3 = 11.90 + (kwhConta * 0.30)
    print ('Valor da Conta: ', total3)
