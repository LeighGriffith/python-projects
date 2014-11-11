'''s1level106
???
'''

import random
import turtle

artist = turtle.Turtle()
artist.pensize(7)



def draw_a_circle(step):
    for count in range(60):
        
        artist.forward(step)
        artist.right(6)


for count in range(10):
    artist.pencolor(random.random(),random.random(),random.random())
    draw_a_circle(6)
    artist.right(36)
