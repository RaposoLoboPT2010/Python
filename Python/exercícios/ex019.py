from random import choice
a1 = input("Diga o primeiro aluno: ")
a2 = input("Diga o segundo aluno: ")
a3 = input("Diga o treceiro aluno: ")
a4 = input("Diga o terceiro aluno: ")
lista = [a1, a2, a3, a4]
escolido = choice(lista)
print("O aluno escolido foi {}!".format(escolido))