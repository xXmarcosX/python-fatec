def cal_inss(salario: float):
    if salario >= 4190.84: 
        return ((salario * 14) / 100) - 190.40
    elif salario >= 2793.89 and salario <= 4190.83:
       return ((salario * 12) / 100)  - 106.59
    elif salario >= 1518.01 and salario <= 2793.88:
        return ((salario * 9) / 100) - 22.77
    elif salario <= 1518.00:
        return (salario/ 100) * 7.5