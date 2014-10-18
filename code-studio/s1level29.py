'''s1level29
for (var count = 0; count < 3; count++) {
  moveForward(100);
  turnRight(120);
}
turnLeft(90);
for (var count2 = 0; count2 < 4; count2++) {
  moveForward(100);
  turnLeft(90);
}
'''
import turtle
artist = turtle.Turtle()
artist.pensize(7)
artist.pencolor('red')


for count in range(3):
    artist.forward(100)
    artist.right(120)

artist.left(90)

for count2 in range(4):
    artist.forward(100)
    artist.left(90)

    
