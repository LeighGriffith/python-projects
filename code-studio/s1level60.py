'''s1level60
// draw_a_square
for (var count = 0; count < 4; count++) {
  moveForward((50));
  turnRight(90);
}
'''
 
import turtle

artist = turtle.Turtle()
artist.pensize(7)

def draw_a_square(length):
        for count in range(4): 
            artist.forward(length)
            artist.right(90)
draw_a_square(100)
