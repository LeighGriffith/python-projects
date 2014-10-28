'''s1level66
// draw_a_snowman
turnLeft(90);
var distances = [(250) * 0.5, (250) * 0.3,(250) * 0.2];
for (var counter = 0; counter < 6; counter++) {

  var distance = distances[counter < 3 ? counter: 5 - counter] / 57.5;
  for (var degree = 0; degree < 90; degree++) {
    moveForward(distance);
    turnRight(2);
  }
  if (counter != 2) {
    turnLeft(180);
    moveForward(100)
}
'''

import turtle


      
            
artist = turtle.Turtle()
artist.pensize(7)
artist.pencolor('black')
artist.speed(100)
artist.left(180)

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

draw_snowman(5)
artist.left(180)
draw_snowman(2)
        


 
 



