'''s1level37
penCoulor(colour_random());
for (var count2 = 0; count2 < 4; count2++) {
    for (var count = 0; count < 3; count++) {
    moveForward(100);
    turnRight(120);
  }
turnRight(90);
}
'''
import random

import turtle

artist = turtle.Turtle()
artist.pensize(7)

for count in range(4):
    artist.pencolor(random.random(),random.random(),random.random())
    for count2 in range(3):
        artist.forward(100)
        artist.right(120)

    artist.right(90)
