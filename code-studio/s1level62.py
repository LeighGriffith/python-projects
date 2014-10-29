'''s1level62
for (var count2 = 0; count2 < 60; count2++) {
  penColour(colour_random());
  // draw_a_square
  for (var count = 0; count < 4; count++) {
      moveForward(100)
      turnRight(10)
    }
'''
import turtle
import random
 

artist = turtle.Turtle() 
artist.pensize(7)
artist.speed(100)

 
def draw_the_square(length):
    for count in range(4):
        artist.forward(length)
        artist.right(90) 
 


for count in range(60):
    artist.pencolor(random.random(),random.random(),random.random())
    draw_the_square(100)
    artist.right(10)
    
     



 
 
    



