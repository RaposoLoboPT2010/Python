ds = int(input("Quantos dias carro foi alugado? "))
km = int(input("Quantos km você andou com o carro? "))
pt = ds * 60 + km * 0.15
print("O preço total é de {:.2f}.".format(pt))