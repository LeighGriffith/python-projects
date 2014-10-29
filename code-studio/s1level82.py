'''s1level82
function draw_a_square() {
  for (var count = 0; count < 4; count++) {
    moveForward(100);
    turnRight(90);
  }
}

function draw_a_circle() {
  for (var count2 = 0; count2 < 360; count2++) {
    moveForward(1);
    turnRight(1);
  }
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
def draw_a_circle(length):
    for count in range(360):
        artist.forward(length)
        artist.right(length)


draw_a_square(80)


