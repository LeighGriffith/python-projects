'''s1level65
var counter;

for (counter = 25; counter <= 60; counter += 5) {
  moveForward(counter);
  turnRight(90);
}
'''


import mymod

artist = mymod.MyArtist()
artist.pensize(7)
artist.pencolor('darkblue')




artist.spiral(30)
