sal = float(input("Qual é o salário do Funcionário? EUR€"))
aum = sal + sal * 15 / 100
print("Um Funcionário que ganhava EUR€{:.2f}, com 15% de aumento, passa a receber EUR€{:.2f}.".format(sal, aum))