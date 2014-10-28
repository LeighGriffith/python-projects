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

import mymod

artist = mymod.MyArtist()
artist.pensize(7)
artist.pencolor('red')

artist.draw_a_square(50)
artist.draw_a_square(60)
artist.draw_a_square(70)
artist.draw_a_square(80)
artist.draw_a_square(90)
