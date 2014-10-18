'''s1level27
for (var count = 0; count < 3; count++) {
  penColour(colour_random());
  moveForward(100);
  turnRight(120);
}
'''

import mymod

import turtle

artist = turtle.Turtle()
artist.pensize(7)
 


for count in range(3):
    artist.pencolor(mymod.random_color())
    artist.forward(100)
    artist.right(120)
