'''s1level89
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

function draw_a_house(length2) {
  draw_a_square
  move_Forward(length2)
  draw_a_triangle


draw_a_house(100)
turn_right(60)
move_forward(100)
turn_right(90)
move_forward(100)
turn_left(180)
draw_a_house(150)
turn_right(60)
move_forward(100)
turn_right(90)
move_forward(100)
turn_left(180)
draw_a_house(100)
'''
 
import turtle

artist = turtle.Turtle()
artist.pensize(7)
artist.pencolor('black')
artist.left(90)
artist.speed(100)


def draw_a_square(length):
        for count in range(4): 
            artist.forward(length)
            artist.right(90)

def draw_a_triangle(length):
    for count in range(3):
        artist.forward(length)
        artist.right(120)


def draw_a_house(length):
    def draw_a_square(length):
        for count in range(4): 
            artist.forward(length)
            artist.right(90)
    def draw_a_triangle(length):
        for count in range(3):
            artist.forward(length)
            artist.right(120)
    draw_a_square(length)
    artist.forward(length)
    artist.right(30)
    draw_a_triangle(length)

 
draw_a_house(100)
artist.right(60)
artist.forward(100)
artist.right(90)
artist.forward(100)
artist.left(180)
draw_a_house(150)
artist.right(60)
artist.forward(150)
artist.right(90)
artist.forward(150)
artist.left(180)
draw_a_house(100)


 
 

