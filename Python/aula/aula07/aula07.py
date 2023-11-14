n1 = int(input("Diga um número: "))
n2 = int(input("Diga outro número: "))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print("O resultado da adição é {}, \nda subtração é {}, \nda multiplicação é {}, \nda divisão é {:.3f}, \nda divisão inteira é {} e \nda potenciação é {}!".format(a, s, m, d, di, p))