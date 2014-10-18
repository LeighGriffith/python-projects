'''

for (var count = 0; count < 4; count++) {

    moveForward(100);
    turnRight(90);

}

'''
 
 
from turtle import Turtle


artist = Turtle()
artist.pensize(7)
artist.pencolor('orange')

for count in range(4):
    artist.forward(100)
    artist.right(90)



     
