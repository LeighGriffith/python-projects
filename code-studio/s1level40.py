'''s1level40
for (var count = 0; count < 4; count++) {
  moveForward(20);
  turnRight(90);
}
'''

import turtle

artist = turtle.Turtle()
artist.pensize(7)
artist.pencolor('red')

for count in range(4):
    artist.forward(20)
    artist.right(90)
    
