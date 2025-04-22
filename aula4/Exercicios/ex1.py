idade = int(input('Digite sua idade: '))

if idade < 12:
    print('Tu é criança')
elif idade >= 12 and idade <= 17:
    print('Tu é adolescente')
elif idade >= 18 and idade <= 59:
    print('Tu é adulto')
else:
    print('Tu é idoso')