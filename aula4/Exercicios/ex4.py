num1 = float(input('Digite o primeiro número '))
op = input('Digite a operação (+, -, * ou /): ')
num2 = float(input('Digitr o segundo número '))

if op == '+':
    print(f'Resultdo: {num1 + num2}')
elif op == '-':
    print(f'Resultdo: {num1 - num2}')
elif op == '*':
    print(f'Resultado: {num1 * num2}')
elif op == '/':
    if num2 == 0:
        print(f'Não é possível dividir por zero')
    else:
        print(f'Resultado: {num1 / num2}')
else:
    print('Operação inválida')
