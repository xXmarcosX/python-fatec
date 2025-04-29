import random

numero_aleatorio = random.randint(1, 100)
tentativas = 0
num_usuario = 0

print('Jogo de adivinhação')

while num_usuario != numero_aleatorio:
    tentativas += 1
    num_usuario = int(input(f'Tentativa: {tentativas}: '))

    if tentativas == 7:
        print(f'Tentativas esgotadas. O número secreto era {numero_aleatorio}')
        break

    if num_usuario == numero_aleatorio:
        print(f'Acertou!! o numero secreto era {numero_aleatorio}')
        print(numero_aleatorio)
        break
    else:
        if num_usuario < numero_aleatorio:
            print('O número secreto é maior')
            continue
        if num_usuario > numero_aleatorio:
            print('O número secreto é menor')
            continue



