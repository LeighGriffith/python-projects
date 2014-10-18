'''s1level30
turnRight(90);
for (var count = 0; count < 4; count++) {
  moveForward(100);
  turnRight(90);
}
turnRight(180);
moveForward(50);
for (var count2 = 0; count2 < 4; count2++) {
  moveForward(100);
  turnLeft(90);
}
'''

import turtle

artist = turtle.Turtle()
artist.pensize(7)
artist.pencolor('orange')

artist.right(90)
for count in range(4):
    artist.forward(100)
    artist.right(90)

artist.left(90)
artist.forward(50)

for count2 in range(4):
    artist.forward(100)
    artist.right(90)

    
    

