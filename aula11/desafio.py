arq = open("C:\\Users\\2830482511008\\Desktop\\python-fatec\\aula11\\qbdata.txt", 'r')
saida = open("C:\\Users\\2830482511008\\Desktop\\python-fatec\\aula11\\quarterback.txt", 'w')

num = input("Digite o número: ")

linhas = arq.readlines()

for linha in linhas:
    if linha.split()[10] == num:
        print(f'{linha.split()[0]} {linha.split()[1]} teve valor {num}\n')
        saida.write(f'{linha.split()[0]} {linha.split()[1]} teve valor {num}\n')