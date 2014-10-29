'''s1level64
var counter;

for (counter = 50; counter <= 90; counter += 10) {
  // draw_a_square
  for (var count = 0; count < 4; count++) {
    moveForward((counter));
    turnRight(90);
  }
}
'''
import turtle

artist = turtle.Turtle()
artist.pensize(7)
artist.pencolor('blue')

def draw_a_square(length):
        for count in range(4): 
            artist.forward(length)
            artist.right(90)
def square_counter(length):
        draw_a_square(length)
        draw_a_square(length + 10)
        draw_a_square(length + 20)
        draw_a_square(length + 30)
        draw_a_square(length + 40)


square_counter(50) 


