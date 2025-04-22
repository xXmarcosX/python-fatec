minha_tupla = (
    1, 2, 3, 4, 5, 
    'Pão de batata', 
    {"Bebida": "Coca gelada"}, 
    ['maçã', 'banana', 'pera']
    )

# convertendo tupla para lista
nova_lista = list(minha_tupla)
nova_lista[0] = 'Girafa'

print(nova_lista)

# convertendo lista para tupla
nova_lista = tuple(nova_lista)

print(nova_lista)

# print(minha_tupla[5])
# print(minha_tupla[6]["Bebida"])
# print(minha_tupla[7][0])