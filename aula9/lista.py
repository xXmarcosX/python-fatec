desconto_dez = lambda x: x * 0.10
desconto_quinze = lambda x: x * 0.15
desconto_vinte = lambda x: x * 0.20
desconto_vinte_cinco = lambda x: x * 0.25

valores = []

while True:
    val = float(input('Digite um valor: '))

    if val == 0:
        break
    
    valores.append(val)

desconto = []

for valor in valores:
    if valor >= 50 and valor <= 200:
        desconto.append(valor - desconto_dez(valor))
    
    elif valor > 200 and valor <= 500:
         desconto.append(valor - desconto_quinze(valor))

    elif valor > 500 and valor <= 1000:
        desconto.append(valor - desconto_vinte(valor))

    elif valor > 1000:
        desconto.append(valor - desconto_vinte_cinco(valor))

    else:
        desconto.append(valor)

for item in desconto:
    print(f'Valor com desconto {item}')
