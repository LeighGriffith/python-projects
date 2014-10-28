'''s1level62
for (var count2 = 0; count2 < 60; count2++) {
  penColour(colour_random());
  // draw_a_square
  for (var count = 0; count < 4; count++) {
      moveForward(100)
      turnRight(10)
    }
'''
import mymod

artist = mymod.MyArtist()
artist.pensize(7)
artist.speed(100)


for count in range(60):
    artist.pencolor(mymod.random_color())
    artist.draw_a_square(100)
    artist.right(10)
    



