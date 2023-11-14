lar = float(input("Diga a largura da parede: "))
alt = float(input("Diga a altura da parede: "))
a = lar * alt
tin = a / 2
print("A sua parede tem a dimensão de {} x {} e a sua área é {}m².".format(lar, alt, a))
print("Para pintar essa parede sería necessário {}l de tinta.".format(tin))