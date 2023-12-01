from math import radians, sin, cos, tan
ang = float(input("Diga um ângulo: "))
rad = radians(ang)
sen = sin(rad)
print("O ângulo de {} tem o SENO de {:.2f}.".format(ang, sen))
cos = cos(rad)
print("O ângulo de {} tem o COSSENO de {:.2f}.".format(ang, cos))
tan = tan(rad)
print("O ângulo de {} tem a TANGENTE de {:.2f}.".format(ang, tan))