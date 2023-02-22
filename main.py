"""
class of turtle, how it looks and behaves
object of turtle doing the stuff
timmy = object, class = Turtle()

but the point of the blueprints are to have multiple
timmy & tommy each seperate instance of turtle object


they can each have different states. dif color. timmy green tommy purtple. dif state of that attribute
one move other stay still, 
"""
from turtle import Turtle as t
from turtle import Screen
import random

# r = t("turtle")
# r.color("red")
# r.pu()
# o = t("turtle")
# o.color("orange")
# o.pu()
# y = t("turtle")
# y.color("yellow")
# y.pu()
# g = t("turtle")
# g.color("green")
# g.pu()
# b = t("turtle")
# b.color("blue")
# b.pu()
# p = t("turtle")
# p.color("purple")
# p.pu()


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:  ").lower()


is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
number = 0
my_turtles = []
y_value = 150
for turtle in range (0, 6):
    number += 1
    new_turtle = ("turtle_{number}")
    new_turtle = t(shape = "turtle")
    new_turtle.pu()
    new_turtle.color(colors[number - 1])
    new_turtle.goto(x = -230, y = y_value)
    y_value -= 50
    my_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in my_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"You won! The winner is the {winner} turtle!")
            else:
                print(f"You lost! The winner is the {winner} turtle!")
        
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
       


screen.exitonclick()






# r.goto(x= -230, y= 150)
# o.goto(x= -230, y= 100)
# y.goto(x= -230, y= 50)
# g.goto(x= -230, y= 0)
# b.goto(x= -230, y= -50)
# p.goto(x= -230, y= -100)



