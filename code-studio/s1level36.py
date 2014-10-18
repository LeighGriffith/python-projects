'''s1level36
penCoulor(colour_random());
for (var count = 0; count < 3; count++) {
    moveForward(100);
    turnRight(120);
}

turnRight(90);

penCoulor(coulor_random());
for (var count2 = 0; count 2 < 3; count2++) {
    moveForward(100);
    turnRight(120)
}
'''

import mymod

import turtle

artist = turtle.Turtle()
artist.pensize(7)

for count in range(3):
    artist.pencolor(mymod.random_color())
    artist.forward(100)
    artist.right(120)

artist.right(90)

for count2 in range(3):
    artist.pencolor(mymod.random_color())
    artist.forward(100)
    artist.right(120)

