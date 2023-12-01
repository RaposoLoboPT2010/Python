from math import hypot
cat1 = float(input("Diga o comprimento do cateto: "))
cat2 = float(input("Diga o comprimento do outro cateto: "))
hip = hypot(cat1, cat2)
print("O comprimento da hipotenusa é {}.".format(hip))