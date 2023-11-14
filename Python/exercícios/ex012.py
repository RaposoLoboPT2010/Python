p = float(input("Qual é o preço do produto? EUR€"))
des = p - p * 5 / 100 
print("O produto que custava EUR€{:.2f}, com o desconto de 5% vai custar EUR€{:.2f}".format(p, des))