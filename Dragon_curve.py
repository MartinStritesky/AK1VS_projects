import time
import turtle
from turtle import *

try:
    iteration = int(input("Iterations: >> "))
except:
    iteration = 9

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
            bgcolor("Black")
except:
    bgcolor("Black")

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
            color("Red")
except:
    color("Red")

try:
    step = int(input("Enter length of each segment:  >> "))
except:
    step = 20

cycle  = 1

old = "r"
new = old

while cycle < iteration:
    new = (old) + "r"
    old = old[::-1]
    print(old)

    for letter in range(0, len(old)):
        if old[letter] == "r":
            old = (old[:letter]) + "l" + (old[letter + 1:])
        elif old[letter] == "l":
            old = (old[:letter]) + "r" + (old[letter + 1:])
    new = (new) + (old)
    old = new
    cycle += 1

tracer(20)
hideturtle()
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)

penup()
backward(250)
right(90)
forward(250)
left(90)
pendown()
for letter in range(0, len(new)):
    if new[letter] == "r":
        turtle.right(90)
        turtle.forward(step)
    elif new[letter] == "l":
        turtle.left(90)
        turtle.forward(step)

time.sleep(5)





