desconto_dez = lambda x: x * 0.10
desconto_quinze = lambda x: x * 0.15
desconto_vinte = lambda x: x * 0.20
desconto_vinte_cinco = lambda x: x * 0.25

valor_total = float(input('Digite o valor total da compra: '))

if valor_total >= 50 and valor_total <= 200:
    print(f'Parabéns!!! Você conseguiu um desconto de 10%')
    print(f'Valor total da compra: {valor_total}')
    print(f'Valor do desconto: {desconto_dez(valor_total)}')
    print(f'Total a pagar: {valor_total - desconto_dez(valor_total)}')

elif valor_total > 200 and valor_total <= 500:
    print(f'Parabéns!!! Você conseguiu um desconto de 15%')
    print(f'Valor total da compra: {valor_total}')
    print(f'Valor do desconto: {desconto_quinze(valor_total)}')
    print(f'Total a pagar: {valor_total - desconto_quinze(valor_total)}')

elif valor_total > 500 and valor_total <= 1000:
    print(f'Parabéns!!! Você conseguiu um desconto de 20%')
    print(f'Valor total da compra: {valor_total}')
    print(f'Valor do desconto: {desconto_vinte(valor_total)}')
    print(f'Total a pagar: {valor_total - desconto_vinte(valor_total)}')

elif valor_total > 1000:
    print(f'Parabéns!!! Você conseguiu um desconto de 25%')
    print(f'Valor total da compra: {valor_total}')
    print(f'Valor do desconto: {desconto_vinte_cinco(valor_total)}')
    print(f'Total a pagar: {valor_total - desconto_vinte_cinco(valor_total)}')

else:
    print('Que pena. Você não conseguiu o desconto...')
    print(f'O valor a ser pago é: {valor_total}')