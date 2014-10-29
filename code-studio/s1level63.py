'''s1level63
// draw_a_square
for (var count = 0; count < 4; count++) {
  moveForward((50));
  turnRight(90);
}
// draw_a_square
for (var count2 = 0; count2 < 4; count2++) {
  moveForward((60));
  turnRight(90);
}
// draw_a_square
for (var count3 = 0; count3 < 4; count3++) {
  moveForward((70));
// draw_a_square
for (var count = 0; count < 4; count++) {
  moveForward((80));
  turnRight(90);
}
// draw_a_square
}
for (var count2 = 0; count2 < 4; count2++) {
  moveForward((90));
  turnRight(90);
}
'''

import turtle

artist = turtle.Turtle()
artist.pensize(7)
artist.pencolor('red')

def draw_a_square(length):
        for count in range(4): 
            artist.forward(length)
            artist.right(90)

draw_a_square(50)
draw_a_square(60)
draw_a_square(70)
draw_a_square(80)
draw_a_square(90)
