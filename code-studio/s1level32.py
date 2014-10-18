'''s1level32
for (var count = 0; count < 360; count++) {
  moveForward(1);
  turnRight(1);
}
'''

import turtle

artist = turtle.Turtle()
artist.pensize(7)
artist.pencolor('orange')
artist.speed(30)

for count in range(360):
    artist.forward(1)
    artist.right(1)
    
