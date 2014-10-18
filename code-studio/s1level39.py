'''s1level39
for (var count2 = 0; count2 < 36; count2++)
    pen_Colour(colour_random());
    for (var count = 0; count < 3; count++) {
      moveForward(100);
      turnRight(120);
 }
}
turnRight(10)
'''

import random

import turtle

artist = turtle.Turtle()
artist.pensize(7)
artist.speed(100)
 
for count in range(36):
    artist.color(random.random(),random.random(),random.random())
    for count2 in range(3):
            artist.forward(100)
            artist.right(120)
    artist.right(10)
 
