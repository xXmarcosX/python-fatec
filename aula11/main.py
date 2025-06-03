import os

arq = open("C:\\Users\\2830482511008\\Desktop\\python-fatec\\aula11\\qbdata.txt", 'r')
saida = open("C:\\Users\\2830482511008\\Desktop\\python-fatec\\aula11\\saida.txt", 'w')

# for item in os.listdir("C:\\Users\\2830482511008\\Desktop\\python-fatec\\aula11"):
#     print(item)

conteudo = arq.read()

#lê arquivo completo
# print(conteudo)

linhas = arq.readlines()

# Lê o arquivo linha por linha
# print(linhas)

saida.write("Numeros de 1 a 10: \n")

for i in range(1, 11):
    saida.write(f'{i}\n')

arq.close()
saida.close()

saida = open("C:\\Users\\2830482511008\\Desktop\\python-fatec\\aula11\\saida.txt", 'a')

saida.write('Adicionando numeros de 11 a 20:\n')

for i in range(11, 21):
    saida.write(f'{i}\n')