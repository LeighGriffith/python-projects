'''s1level43
for (var count3 = 0; count3 < 4; count3++) {
  for (var count2 = 0; count2 < 10; count2++) {
    penColour(colour_random());
    for (var count = 0; count < 4; count++) {
      moveForward(20);
      turnRight(90);
    }
    moveForward(20);
  }
  turnRight(80);
}
'''

import mymod

import turtle

artist = turtle.Turtle()
artist.pensize(7)

artist.right(230)

for count in range(4):
    for count2 in range(10):
        artist.pencolor(mymod.random_color())
        for count3 in range(4):
            artist.forward(20)
            artist.right(90)

        artist.forward(20)

    artist.right(80)
