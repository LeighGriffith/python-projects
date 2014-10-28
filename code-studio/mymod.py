import random
import turtle

 
def random_color():
    return (random.random(),random.random(),random.random())

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
    def draw_a_snowman(self,length=100):
         self.left(90)
         for count in range(360):
             self.forward(1)
             self.left(1)
         
     
            
            
         
            
           
