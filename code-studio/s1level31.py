'''s1level31
penColour(colour_random());
for (var count = 0; count < 8; count++) {
  moveForward(100);
  moveBackward(100);
  turnRight(45);
}
'''

import turtle

artist = turtle.Turtle()
artist.pensize(7)

import mymod
 
for count in range(8):
    artist.pencolor(mymod.random_color())
    artist.forward(100)
    artist.backward(100)
    artist.right(45)
