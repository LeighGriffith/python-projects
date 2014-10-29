
import turtle
artist = turtle.Turtle()
artist.pensize(7)
artist.pencolor('black')
artist.left(180)
artist.speed(100)


def draw_snowman(length):
   
    

    distances = [(length) * 0.5, (length) * 0.3,(length) * 0.2]
    for counter in range(6):
        distance = distances[counter if counter < 3 else 5-counter]

        for degree in range(90):
            artist.forward(distance)
            artist.right(2)

        if counter != 2:
            artist.left(180)
            artist.forward(2)


 
    draw_snowman(5)
    artist.right(90)
    artist.up()
    artist.left(90)
    artist.forward(100)
    artist.down()
    artist.right(180)
    
