peso = float(input('Quanto você pesa? ').strip().replace(',','.'))
altura = float(input('Qual a sua altura? ').strip().replace(',','.'))
imc = peso / (altura*altura)

print(f'Seu IMC é {imc :.2f}')

if imc < 18.5:
    print('Você esta abaixo do peso.')

elif imc < 24.9:
    print('Você esta com seu peso normal.')

elif imc < 29.9:
    print('Você está com sobrepeso')

elif imc < 39.9:
    print('Você está com obesidade moderada')

else:
    print('Você está com obesidade grave')