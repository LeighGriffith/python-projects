'''s1level87
var length2;

function draw_a_square(length2) {
  for (var count = 0; count < 4; count++) {
    moveForward(length2);
    turnRight(90);
  }
}

function draw_a_triangle(length2) {
  for (var count2 = 0; count2 < 3; count2++) {
    moveForward(length2);
    turnRight(120);
    }
}
draw_a_triangle(100)
move_Forward(100)
draw_a_tringle(200)
'''
import turtle

artist = turtle.Turtle()
artist.pensize(7)
artist.pencolor('red')
artist.left(90)

def draw_a_square(length):
        for count in range(4): 
            artist.forward(length)
            artist.right(90)

def draw_a_triangle(length):
    for count in range(3):
        artist.forward(length)
        artist.right(120)

draw_a_triangle(100)
artist.forward(100)
draw_a_triangle(200)


    



