#!/usr/bin/env python3

"""planets.py: Description of how the planets move.

__author__ = "Wang Qichao"
__pkuid__  = "1800011837"
__email__  = "1800011837@pku.edu.cn"
"""

import math
import turtle


Sun=turtle.Turtle()  
Mercury=turtle.Turtle()  #shui
Venus=turtle.Turtle()  #jin
Mars=turtle.Turtle()  #huo
Earth=turtle.Turtle()  
Jupiter=turtle.Turtle()  #mu
Saturn=turtle.Turtle()  #tu

def planet(name,color,d):
    """The color, shape, and initial position of the planet
    """
    name.shape("circle")
    name.color(color)
    name.speed(0)
    name.penup()
    name.fd(d)
    name.pendown()


def orbit(name,a,i):
    """The planetary orbit
    """
    name.speed(0)
    b=(a**2-40*2)**0.5
    x=a*math.cos(math.radians(10*i))
    y=b*math.sin(math.radians(10*i))
    name.goto(x,y)


def main():
    """The parameters of every planet
    """
    planet(Sun,"red",1)
    planet(Mercury,"blue",50)
    planet(Venus,"yellow",90)
    planet(Mars,"purple",130)
    planet(Earth,"orange",170)
    planet(Jupiter,"green",210)
    planet(Saturn,"brown",250)
    for i in range(1000):       
        orbit(Mercury,50,0.5*i)
        orbit(Venus,90,0.4*i)
        orbit(Mars,130,0.3*i)
        orbit(Earth,170,0.2*i)
        orbit(Jupiter,210,0.1*i)
        orbit(Saturn,250,0.08*i)
    turtle.mainloop()


if __name__ == '__main__':
    main()
