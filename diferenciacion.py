from math import e, log

def evaluar(expr, x):
    return eval(expr)

#Para los puntos 1.8 / 1.9 / 2.0 / 2.1 / 2.2
h = 0.1
f = "x*e**x"

tres_adelante = []
tres_atras = []
tres_medio = []
cinco_adelante = []
cinco_atras = []
cinco_medio = []

#3 hacia adelante
a = 1.8
for i in range(3):
    tres_adelante.append((1/(2*h))*(-3*evaluar(f, a) + 4*evaluar(f, a + h) - evaluar(f, a + 2*h)))
    a = a + h

#3 hacia atras
a = 2.2
for i in range(3):
    tres_atras.append((1/(2*h))*(3*evaluar(f, a) - 4*evaluar(f, a - h) + evaluar(f, a - 2*h)))
    a = a - h

#3 punto medio
a = 1.9
for i in range(3):
    tres_medio.append((1/(2*h))*(evaluar(f, a + h) - evaluar(f, a - h)))
    a = a + h

#5 hacia adelante
a = 1.8
cinco_adelante.append((1/(12*h))*(-25*evaluar(f, a) + 48*evaluar(f, a + h) - 36*evaluar(f, a + 2*h) + 16*evaluar(f, a + 3*h) - 3*evaluar(f, a + 4*h)))

#5 hacia atras
a = 2.2
cinco_atras.append((1/(12*h))*(25*evaluar(f, a) - 48*evaluar(f, a - h) + 36*evaluar(f, a - 2*h) - 16*evaluar(f, a - 3*h) + 3*evaluar(f, a - 4*h)))

#5 punto medio
a = 2.0
cinco_medio.append((1/(12*h))*(evaluar(f, a - 2*h) - 8*evaluar(f, a - h) + 8*evaluar(f, a + h) - evaluar(f, a + 2*h)))


print("Tres hacia adelante:")
print(tres_adelante)
print("Tres hacia atrás:")
print(tres_atras)
print("Tres punto medio:")
print(tres_medio)
print("Cinco hacia adelante:")
print(cinco_adelante)
print("Cinco hacia atrás:")
print(cinco_atras)
print("Cinco punto medio:")
print(cinco_medio)
