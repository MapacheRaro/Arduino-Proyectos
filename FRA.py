from turtle import *
import colorsys
import math

# Configuración inicial
speed(0.25)
bgcolor("black")

# Genera los pétalos
goto(0, -40)

for i in range(16):
    for j in range(18):
        color("red")  # Cambiado a rojo
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)

# Genera la parte central de la flor
color("black")
shape("turtle")
fillcolor("darkred")  # Cambiado a rojo más oscuro
phi = 137.508 * (math.pi / 180.0)

for i in range(200):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    penup()
    goto(x, y)
    setheading(i * 137.508)
    pendown()
    stamp()

# Añade el texto al final
penup()
goto(0, -200)  # Posiciona el texto
pendown()
color("white")  # Color del texto
write("Te amo, Angela", align="center", font=("Arial", 24, "bold"))  # Escribe el texto

done()
