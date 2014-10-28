'''s1level45
RANDOM DRAW LEVEL
'''

import mymod

import turtle

artist = turtle.Turtle()
artist.pensize(7)
artist.speed(100)


for count in range(37):
    for count2 in range(4):
        artist.pencolor(mymod.random_color())
        artist.right(76)
        artist.forward(12)
        for count3 in range(6):
            artist.backward(22)
            
