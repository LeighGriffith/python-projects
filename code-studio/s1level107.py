'''s1level107
make a function and call it and make the counter to count it off...
'''

import turtle
import random

artist = turtle.Turtle()
artist.pensize(7)
artist.speed(100)

def draw_a_circle(step):
    for count in range(60):

       artist.forward(step)
       artist.right(6)  
    

for count in range(10):
    artist.pencolor(random.random(),random.random(),random.random())
    draw_a_circle(4)
    draw_a_circle(8)
    artist.right(36)
