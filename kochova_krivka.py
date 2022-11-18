
import time
import turtle
import math
from turtle import *


def koch_curve(a, order):
    if order > 0:
        for t in [60, -120, 60, 0]:
            koch_curve(a / 3, order - 1)
            left(t)
    else:
        forward(a)
try:
    iteration = int(input("Iterations: "))
except ValueError:
    iteration = 4

order = iteration

try:
    bg_color = input("Background color? (B)lack, (W)hite, (Y)ellow, (C)yan: >> ").lower()
    match bg_color:
        case "b":
            bgcolor("Black")
        case "w":
            bgcolor("White")
        case "y":
            bgcolor("Yellow")
        case "c":
            bgcolor("Cyan")
        case "":
            bgcolor("Blue")
except:
    bgcolor("Blue")

try:
    curve_color = input("Koch´s curve color? (S)ilver, (G)reen, (P)urple, Pin(K): >> ").lower()
    match curve_color:
        case "s":
            color("Silver")
        case "g":
            color("Green")
        case "p":
            color("Purple")
        case "k":
            color("Pink")
        case "":
            color("White")
except:
    color("White")


screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)
screen.colormode(255)
size = 1000

# Starting to draw the first phase in 1/sqrt(3) of the half screen
penup()
backward(size/math.sqrt(3))
left(30)
pendown()

tracer(20)
hideturtle()
begin_fill()

# 3 curves to complete the fractal
for j in range(3):
    for i in range(3):
        koch_curve(size, order)
        right(120)

end_fill()
update()

time.sleep(4)