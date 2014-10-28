'''s1level67
for (var count = 0; count < 3; count++) {
  // draw_a_snowman
  turnLeft(90);
  var distances = [(150) * 0.5, (150) * 0.3,(150) * 0.2];
  for (var counter = 0; counter < 6; counter++) {

    var distance = distances[counter < 3 ? counter: 5 - counter] / 57.5;
    for (var degree = 0; degree < 90; degree++) {
      moveForward(distance);
      turnRight(2);
    }
    if (counter != 2) {
'''

import turtle
artist = turtle.Turtle()
artist.pensize(7)
artist.pencolor('black')
artist.left(180)
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


for count in range(3):
    draw_snowman(2)
    artist.right(90)
    artist.up()
    artist.left(90)
    artist.forward(100)
    artist.down()
    artist.right(180)
    
  
