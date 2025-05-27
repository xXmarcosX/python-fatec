ids = []
nomes = []
salarios = []
fgts_s = []
inss_s = []
salario_liquidos = []

nome: str = ''
salario: float = 0
fgts: float = 0
inss: float = 0
salario_liquido: float = 0

i: int = 0
resp: str = ""

def cal_fgts(salario: float):
    return (salario / 100) * 8

def show_users(lista):
    for i in range(len(lista)):
        print(f'{ids[i]} | {nomes[i]} | {salarios[i]} | {fgts_s[i]} | {inss_s[i]} | {salario_liquidos[i]}')

def cal_inss(salario: float):
    if salario >= 4190.84: 
        return ((salario * 14) / 100) - 190.40
    elif salario >= 2793.89 and salario <= 4190.83:
       return ((salario * 12) / 100)  - 106.59
    elif salario >= 1518.01 and salario <= 2793.88:
        return ((salario * 9) / 100) - 22.77
    elif salario <= 1518.00:
        return (salario/ 100) * 7.5


while True:
    i += 1
    print('')

    id = i
    nome = input('Digite o nome do usuário: ')
    salario = float(input('Digite o salário do usuário: '))
    fgts = cal_fgts(salario)
    inss = cal_inss(salario)
    salario_liquido = salario - cal_inss(salario)

    ids.append(id)
    nomes.append(nome)
    salarios.append(salario)
    fgts_s.append(fgts)
    inss_s.append(inss)
    salario_liquidos.append(salario_liquido)

    print('INSS: ', cal_inss(salario))

    resp = input('Deseja adicionar outro usuário?: ')

    while resp != 's'.lower() and resp != 'n'.lower():
        resp = input('Digite apenas "s" ou "n": ')

    if resp == "n":
        break

print('')
print('ID | Nome | Salário Bruto | FGTS | INSS | Salário Líquido')
print('')

show_users(nomes)