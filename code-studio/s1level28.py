'''s1level28
for (var count = 0; count < 4; count++) {
  moveForward(100);
  turnRight(90);
}
turnRight(60);
moveForward(100);
turnLeft(120);
moveForward(100);
'''
 

import turtle

artist = turtle.Turtle()
artist.pensize(7)
artist.pencolor('orange')


for count in range(4):
    artist.forward(100)
    artist.right(90)

for count2 in range(2):
    artist.left(120)
    artist.backward(100)  
