'''s1level64
var counter;

for (counter = 50; counter <= 90; counter += 10) {
  // draw_a_square
  for (var count = 0; count < 4; count++) {
    moveForward((counter));
    turnRight(90);
  }
}
'''
import mymod

artist = mymod.MyArtist()
artist.pensize(7)
artist.pencolor('blue')

artist.square_counter(50) 


