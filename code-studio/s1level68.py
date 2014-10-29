'''s1level68
var counter;

for (counter = 110; counter >= 70; counter -= 10) {
  // draw_a_snowman
  turnLeft(90);
  var distances = [(counter) * 0.5, (counter) * 0.3,(counter) * 0.2];
  for (var counter2 = 0; counter2 < 6; counter2++) {

    var distance = distances[counter2 < 3 ? counter2: 5 - counter2] / 57.5;
    for (var degree = 0; degree < 90; degree++) {
      moveForward(distance)
      }
'''

import turtle
artist = turtle.Turtle()
artist.pensize(7)
artist.pencolor('black')
artist.left(180)
artist.up()
artist.forward(100)
artist.right(90)
artist.down()
artist.left(90)
artist.speed(100)


def draw_snowman(length):
   
    

    distances = [(length) * 0.5, (length) * 0.3,(length) * 0.2]
    for counter in range(6):
        distance = distances[counter if counter < 3 else 5-counter]

        for degree in range(90):
            artist.forward(distance)
            artist.right(2)

        if counter != 2:
            artist.left(180)
            artist.forward(2)


 
draw_snowman(3.5)
artist.right(90)
artist.up()
artist.left(90)
artist.forward(100)
artist.down()
artist.right(180)
draw_snowman(3)
artist.right(90)
artist.up()
artist.left(90)
artist.forward(100)
artist.down()
artist.right(180)
draw_snowman(2.5)
artist.right(90)
artist.up()
artist.left(90)
artist.forward(100)
artist.down()
artist.right(180)
draw_snowman(2)
artist.right(90)
artist.up()
artist.left(90)
artist.forward(100)
artist.down()
artist.right(180)
draw_snowman(1.5)
artist.right(90)
artist.up()
artist.left(90)
artist.forward(100)
artist.down()
artist.right(180)


 

 
