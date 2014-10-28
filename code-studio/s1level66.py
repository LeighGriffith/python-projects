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
}
'''
import mymod
 
artist = mymod.MyArtist()
artist.pensize(7)
artist.pencolor('blue')

 

artist.draw_a_snowman(130)

