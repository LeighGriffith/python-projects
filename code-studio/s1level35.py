'''s1level35
for (var count = 0; count < 3; count++) {
    moveForward(100);
    turnRight(120);
}
'''

import turtle

artist = turtle.Turtle()
artist.pensize(7)
artist.pencolor('blue')

for count in range(3):
    artist.forward(100)
    artist.right(120)
