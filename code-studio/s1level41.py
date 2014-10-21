'''s1level41
penColour(colour_random());
for (var count2 = 0; count2 < 10; count2++) {
  for (var count = 0; count < 4; count++) {
    moveForward(20);
    turnRight(90);
  }
  moveForward(20);
}
'''

import mymod

import turtle

artist = turtle.Turtle()
artist.pensize(7)
artist.left(90)

for count in range(10):
    artist.pencolor(mymod.random_color())
    for count2 in range(4):
         artist.forward(20)
         artist.right(90)
    artist.forward(20)
                    
