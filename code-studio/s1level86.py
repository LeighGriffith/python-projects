'''s1level86
function draw_a_square() {
  for (var count = 0; count < 4; count++) {
    moveForward(100);
    turnRight(90);
  }
}

function draw_a_house() {
  draw_a_square();
  moveForward(100);
  turnRight(30);
  draw_a_triangle();
}

function draw_a_triangle() {
  for (var count = 0; count < 3; count++) {
    moveForward(100);
    turnRight(120);
  }
}
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

    
    
    
    
         

 
