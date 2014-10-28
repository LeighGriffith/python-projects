'''s1level59
for (var count = 0; count < 4; count++) {
  moveForward(100);
  turnRight(90);
}
'''

import turtle

artist = turtle.Turtle()
artist.pensize(7)
artist.pencolor('red')


for count in range(4):
    artist.forward(100)
    artist.right(90)
