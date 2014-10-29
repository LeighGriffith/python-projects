'''s1level69
FREE LEVEL!!!
'''

import random
import turtle
b = turtle.Turtle()
b.pensize(7)
b.speed(100)


 
def random_color():
    return (random.random(),random.random(),random.random())
 
 
def draw_a_square(length):
        for count in range(4): 
            b.forward(length)
            b.right(90)
def square_counter(length):
    b.draw_a_square(length)
    b.draw_a_square(length + 10)
    b.draw_a_square(length + 20)
    b.draw_a_square(length + 30)
    b.draw_a_square(length + 40)

def spiral(length):
    b.forward(length)
    b.right(90)
    b.forward(length + 5)
    b.right(90)
    b.forward(length + 10)
    b.right(90)
    b.forward(length + 15)
    b.right(90)
    b.forward(length + 20)
    b.right(90)
    b.forward(length + 25)
    b.right(90)
    b.forward(length + 30)
    b.right(90)
    b.forward(length + 35)
    
def draw_snowman(length):
    distances = [(length) * 0.5, (length) * 0.3,(length) * 0.2]
    for counter in range(6):
        distance = distances[counter if counter < 3 else 5-counter]

        for degree in range(90):
            b.forward(distance)
            b.right(2)

        if counter != 2:
            b.left(180)
            b.forward(2) 
 



for count in range(6):
    b.pencolor(random_color())
    for count2 in range(6):
         spiral(6)
         draw_snowman(3.7)
         draw_a_square(2.7)

        
        
