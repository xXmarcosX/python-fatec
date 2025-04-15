
preco_frutas = {
    'pera':'Estava mais cara que o normal...', #Inicializando o dicionário somente com 'uva': 'Estava bem conta!',
    'maçã': 'Não tinha...!'
}

numero_frutas = {
    1: 1, 
    2: 1, 
    3: 0
    } #Somente com inteiros

frutas = {
    'pera': 50, 
    'uva': 2, 
    'maçã':55, 
    'abacaxi': 25, 
    'manga':''
    } #Misturando os dois tipos print(preco_frutas)

# print(numero_frutas) 
# print(frutas)

# print(preco_frutas['pera'])
# print(frutas['maçã'])
# print(frutas.get('Pitomba', 'Fruta não encontrada'))
# print(frutas.clear())

frutas['maçã'] = 100

# print(frutas['maçã'])

frutas['jaca'] = 150

print(frutas)

del frutas['jaca'] # deletando a chave 'jaca'
del frutas # deletando o dicionário

print(frutas)