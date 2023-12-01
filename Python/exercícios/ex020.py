from random import shuffle
a1 = input("Diga o primeiro aluno: ")
a2 = input("Diga o segundo aluno: ")
a3 = input("Diga o terceiro aluno: ")
a4 = input("Diga o quarto aluno: ")
lista = [a1, a2, a3, a4]
shuffle(lista)
print("A ordem escolida foi {}".format(lista))