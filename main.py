import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
image = "nepal_zone.gif"
screen.addshape(image)
turtle.shape(image)
screen.title("nepal zone guessing game")
zone_file = pandas.read_csv("zone.csv")
all_zones = zone_file.zone.to_list()

watermark = Turtle()
watermark.penup()
watermark.hideturtle()
watermark.goto(200,-300)
watermark.color("blue")
watermark.write("© Adarsha Rimal",font=("arial",15,"italic"))

guessed_zone = []

while len(guessed_zone) < 50:
    answer_zone = screen.textinput(title=f"{len(guessed_zone)}/14 correct zones", prompt="guess the another zone").title()
    if answer_zone == "Exit":
        missing_zone = [zone for zone in all_zones if zone not in guessed_zone]

        new_data = pandas.DataFrame(missing_zone)
        new_data.to_csv("zones_to_learn.csv")
        exit()

    if answer_zone in all_zones:
        t = Turtle()
        t.hideturtle()
        t.penup()
        zone_data = zone_file[zone_file.zone == answer_zone]
        t.goto(int(zone_data.x),int(zone_data.y))
        t.color("green")
        t.write(f"{answer_zone}")
        guessed_zone.append(answer_zone)



turtle.mainloop()
