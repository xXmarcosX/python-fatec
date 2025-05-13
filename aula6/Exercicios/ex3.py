especiais = ['@', '!', '#', '$', '%', '&', '*']
numericos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alfabeto_minusculo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('Crie um senha com as seguintes restrições:\n'
    '- Pelo menos uma letra maiúscula\n'
    '- Pelo menos uma letra minúsucla\n'
    '- Pelo menos um digito numérico\n'
    '- Pelo menos um caractere especial (!, @, #, $, %, *): ')

while True:
    incorreto_oito = True 
    incorreto_especial = True
    incorreto_numerico = True
    incorreto_alfabeto = True
    incorreto_alfabeto_min = True

    senha = input('\nDigite sua senha: ')

    for caractere in especiais:
        for letra in senha:
            if caractere == letra: 
                incorreto_especial = False

    for num in numericos:
        for letra in senha:
            if str(num) == letra:
                incorreto_numerico = False

    for l in alfabeto:
        for letra in senha:
            if l == letra:
                incorreto_alfabeto = False
    
    for let in alfabeto_minusculo:
        for letra in senha:
            if let == letra:
                incorreto_alfabeto_min = False
    
    if len(senha) >= 8:
        incorreto_oito = False

    if incorreto_especial or incorreto_numerico or incorreto_alfabeto or incorreto_alfabeto_min or incorreto_oito:
        print('\nSua senha não atende aos seguintes requisitos:')

        print('')

        if len(senha) < 8:
            print('❌ Mínimo 8 caracteres') 

        if incorreto_especial:
            print('❌ Pelo menos um caractere especial')

        if incorreto_numerico:
            print('❌ Pelo menos um digito numérico')

        if incorreto_alfabeto:
            print('❌ Pelo menos uma letra maiuscula')

        if incorreto_alfabeto_min:
            print('❌ Pelo menos uma letra minuscula')
        continue
    else:
        print('\n✅ Senha aceita com sucesso!!!')
        break