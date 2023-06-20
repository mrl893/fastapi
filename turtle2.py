import turtle
from random import randint

tur = turtle.Turtle()
screen = turtle.Screen() 
screen.title("Us State Game")
screen.bgpic("United_States_black_by_county_1880.gif")
    
def main(distance) -> None:
    while distance > 0:
        if turtle.distance(0,0) > 100:
            angle = turtle.towards(0,0)
            turtle.setheading(angle)
        turtle.forward(1)
        distancec= distance -1
        
boundary =  turtle.Turtle(visible=False)
boundary.color("red")
boundary.penup()
boundary.sety(-100)
boundary.pendown()
boundary.goto(main(10)[0], boundary.ycor()+364) # type: ignore

if __name__ == "":
    for i in range(1000):
        turtle.left(randint(0,90))
        turtle.forward(randint(1, 50))
        turtle.mainloop()