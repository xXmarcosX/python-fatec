compra = float(input('Digite o valor total da sua compra: '))
desconto = 0.0

if compra >= 100 and compra < 200:
    print(f'Valor total da sua compra: {compra}')
    print(f'Desconto: {compra * 0.05}')

    compra = compra - (compra * 0.05)

    print(f'Desconto de 5% aplicado. Valor final da compra: {compra}')

elif compra >= 200 and compra < 300:
    print(f'Valor total da sua compra: {compra}')
    print(f'Desconto: {compra * 0.10}')

    compra = compra - (compra * 0.10)

    print(f'Desconto de 10% aplicado. Valor final da compra: {compra}')

elif compra >= 300:
    print(f'Valor total da sua compra: {compra}')    
    print(f'Desconto: {compra * 0.15}')

    compra = compra - (compra * 0.15)

    print(f'Desconto de 15% aplicado. Valor final da compra: {compra}')

else:
    print(f'Valor total da sua compra: {compra}')
    print('Você não gastou o suficiente para que o desconto seja aplicado')