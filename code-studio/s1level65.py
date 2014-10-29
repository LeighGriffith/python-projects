'''s1level65
var counter;

for (counter = 25; counter <= 60; counter += 5) {
  moveForward(counter);
  turnRight(90);
}
'''


import turtle

artist = turtle.Turtle()
artist.pensize(7)
artist.pencolor('darkblue')


def spiral(length):
        artist.forward(length)
        artist.right(90)
        artist.forward(length + 5)
        artist.right(90)
        artist.forward(length + 10)
        artist.right(90)
        artist.forward(length + 15)
        artist.right(90)
        artist.forward(length + 20)
        artist.right(90)
        artist.forward(length + 25)
        artist.right(90)
        artist.forward(length + 30)
        artist.right(90)
        artist.forward(length + 35)




spiral(30)
