from model.User import User
from model.Users_Database import Users_Database
from utils.cal_fgts import cal_fgts
from utils.cal_inss import cal_inss

database = Users_Database()
id = 0

while True:
    id += 1

    name = input('\nDigite o nome do usuário: ')
    salary = float(input('Digite o salário do usuário: '))

    user = User(id, name, salary, cal_fgts(salary), cal_inss(salary))
    database.add_user(user)

    resp = input('Deseja adicionar um novo usuário? (s/n): ')

    while resp.lower() != 's' and resp.lower() != 'n':
        resp = input('Digite apenas S ou N: ')

    if resp == 'n':
        break

print('')
print('ID | Nome | Salário Bruto | FGTS | INSS | Salário Líquido')
print('')

database.get_users()