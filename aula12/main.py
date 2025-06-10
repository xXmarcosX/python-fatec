from utils.calcula_media import calcula_media
from utils.situacao_aluno import situacao_aluno

#Matérias
matematica: float = 0
portugues: float = 0
historia: float = 0
ciencias: float = 0
ingles: float = 0

nome: str = ''

# Estudantes
total_estudantes: int = 0
aprovados: int = 0
recuperacao: int = 0
reprovados: int = 0
menor_nota = 99
alunos = []


while True:
    menor_mat = ''
    nome = input("\nDigite nome do aluno ou 'sair' para finalizar: ")

    if nome.lower() == 'sair':
        print('\nRegistro Finalizado...')
        break

    total_estudantes += 1

    matematica = float(input(f"\nDigite a nota em matemática para {nome}: "))
    portugues = float(input(f"Digite a nota em português para {nome}: "))
    historia = float(input(f"Digite a nota em história para {nome}: "))
    ciencias = float(input(f"Digite a nota em ciências para {nome}: "))
    ingles = float(input(f"Digite a nota em ingles para {nome}: "))

    if matematica < menor_nota:
        menor_mat = 'Matematica'
        menor_nota = matematica
    
    if portugues < menor_nota:
        menor_mat = 'Português'
        menor_nota = portugues
    
    if historia < menor_nota:
        menor_mat = 'História'
        menor_nota = historia
    
    if ciencias < menor_nota:
        menor_mat = 'Ciências'
        menor_nota = ciencias
    
    if ingles < menor_nota:
        menor_mat = 'Inglês'
        menor_nota = ingles

    media = calcula_media(matematica, portugues, historia, ciencias, ingles)
    situacao = situacao_aluno(media)

    alunos.append({
        "nome": nome,
        "matematica": matematica,
        "portugues": portugues,
        "historia": historia,
        "ciencias": ciencias,
        "ingles": ingles,
        "media": media,
        "situacao": situacao,
        "menor_num": menor_nota,
        "menor_materia": menor_mat
    })
        
    print('A média do aluno', media)
    print('A situação do aluno é:', situacao)

    if situacao == 'Aprovado':
        aprovados += 1
    elif situacao == 'Recuperação':
        recuperacao += 1
    elif situacao == 'Reprovado':
        reprovados += 1

print('')
print('=== RELATÓRIO DA TURMA ===')
print('')

for aluno in alunos:
    print(f'\nEstudante: {aluno["nome"]}')
    print(f'Notas: "Matemática": {aluno["matematica"]}, "Português": {aluno["portugues"]}, "História": {aluno["historia"]}, "Ciências": {aluno["ciencias"]}, "Inglês": {aluno["ingles"]}')
    print(f'Média: {aluno["media"]}')
    print(f'Situação: {aluno["situacao"]}')
    print(f'Disciplina com menor nota: {aluno["menor_materia"]} {aluno["menor_num"]}')

print('')
print('=== RESUMO DA TURMA ===')
print(f'Total de estudantes: {total_estudantes}')
print(f'Aprovados: {aprovados}')
print(f'Em Recuperação: {recuperacao}')
print(f'Reprovados: {reprovados}')