'''s1level61
for (var count2 = 0; count2 < 3; count2++) {
  // draw_a_square
  for (var count = 0; count < 4; count++) {
    moveForward((100));
    turnRight(90);
  }
  turnLeft(120);
}
'''
import turtle

artist = turtle.Turtle()
artist.pensize(7)
artist.pencolor('red')

def draw_a_square(length):
        for count in range(4): 
            artist.forward(length)
            artist.right(90)


for count in range(3):
    draw_a_square(100)
    artist.left(120)




           
         
