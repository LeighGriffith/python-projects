import random
<<<<<<< HEAD
import turtle
=======
 
>>>>>>> origin/master

 
def random_color():
    return (random.random(),random.random(),random.random())

<<<<<<< HEAD
class MyArtist(turtle.Turtle):
    def draw_a_square(self,length=100):
        for count in range(4): 
            self.forward(length)
            self.right(90)
    def square_counter(self,length=100):
        self.draw_a_square(length)
        self.draw_a_square(length + 10)
        self.draw_a_square(length + 20)
        self.draw_a_square(length + 30)
        self.draw_a_square(length + 40)

    def spiral(self,length=100):
        self.forward(length)
        self.right(90)
        self.forward(length + 5)
        self.right(90)
        self.forward(length + 10)
        self.right(90)
        self.forward(length + 15)
        self.right(90)
        self.forward(length + 20)
        self.right(90)
        self.forward(length + 25)
        self.right(90)
        self.forward(length + 30)
        self.right(90)
        self.forward(length + 35)
    
    def draw_snowman(self,length):
    distances = [(length) * 0.5, (length) * 0.3,(length) * 0.2]
    for counter in range(6):
        distance = distances[counter if counter < 3 else 5-counter]

        for degree in range(90):
            self.forward(distance)
            self.right(2)

        if counter != 2:
            self.left(180)
            self.forward(2)
      
     
            
            
         
            
           
=======
 
    
>>>>>>> origin/master
