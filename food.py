from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')

    def  regenerate (self):
        x=random.randint(-280,279)
        y=random.randint(-280,279)
        self.goto(x,y)
