'''s1level84
language:

function draw_a_square() {
  for (var count = 0; count < 4; count++) {
    moveForward(100);
    turnRight(90);
  }
}

function draw_a_triangle() {
  for (var count2 = 0; count2 < 3; count2++) {
    moveForward(100);
    turnRight(120);
  }
}

draw_a_triangle()
move_forward(100)
draw_a_square()
move_forward(100)
draw_a_triangle()
'''



import turtle

artist = turtle.Turtle()
artist.pensize(7)
artist.pencolor('black')
artist.left(90)

def draw_a_triangle(length):
    for count in range(3):
        artist.forward(length)
        artist.right(120)

def draw_a_square(length):
        for count in range(4): 
            artist.forward(length)
            artist.right(90)


draw_a_triangle(80)
artist.forward(80)
draw_a_square(80)
artist.forward(80)
draw_a_triangle(80)




