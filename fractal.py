from turtle import *

def sierpinski(n,longueur):
    speed(42)
    pencolor("black")
    shape("turtle")
    ht()

    if n==0:
        for i in range(3):
            forward(longueur)
            left(120)

    if n>0:
        sierpinski(n-1,longueur/2)
        forward(longueur/2)
        sierpinski(n-1,longueur/2)
        backward(longueur/2)
        left(60)
        forward(longueur/2)
        right(60)
        sierpinski(n-1,longueur/2)
        left(60)
        backward(longueur/2)
        right(60)


sierpinski(6,600)
