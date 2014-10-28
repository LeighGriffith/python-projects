'''s1level61
for (var count2 = 0; count2 < 3; count2++) {
  // draw_a_square
  for (var count = 0; count < 4; count++) {
    moveForward((100));
    turnRight(90);
  }
  turnLeft(120);
}
'''
import mymod

artist = mymod.MyArtist()
artist.pensize(7)
artist.pencolor('red')

for count in range(3):
    artist.draw_a_square()
    artist.left(120)




           
         
