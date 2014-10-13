'''
for (var count = 0' count <3; count++) {
    penCoulor(clour_random());
    moveForward(100);
    turnRight(120)
}
'''
random = ('blue','red','yellow')


from turtle import Turtle
color = ['red','yellow','green']
artist = Turtle()
artist.pensize(7)
artist.pencolor(color)

 



for i in range(3):
    artist.forward(100)
    artist.right(120)










