import turtle
import pandas as pd

# Creating screen and background for the project
screen = turtle.Screen()
screen.title("Portugal districts Game")
img = "Map.gif"
screen.addshape(img)
turtle.shape(img)

# Importing csv file with all districts and converting all districts into a Python List with .to_list() function
data = pd.read_csv("20_districts.csv")
all_distr = data.district.to_list()

# Function for getting all coordinates on screen
# def get_mouse(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse)
# turtle.mainloop()

guessed_dist = []

while len(guessed_dist) < 20:
    # Create input for district
    user_answer = screen.textinput(title=f"{len(guessed_dist)}/20 Districts", prompt="What is another district name?").title()
    # Check if answer match all districts
    if user_answer in all_distr:
        guessed_dist.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.district == user_answer]
        # Converting X & Y cor into integer numbers
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_answer, font=("Arial", 8, "bold"))

    # Congratulations functions
    def game_over():
        over = turtle.Turtle()
        over.goto(0, 0)
        over.hideturtle()
        over.write("Congratulations!", align="center", font=("Arial", 25, "bold"))

    if len(guessed_dist) == 20:
        game_over()

screen.exitonclick()