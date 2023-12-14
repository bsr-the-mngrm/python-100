import turtle
import pandas

# # Get x and y coordinates of a click on the screen
# def get_mouse_click_cor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()

if __name__ == '__main__':
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image_path = "img/blank_states_img.gif"
    screen.addshape(image_path)
    turtle.shape(image_path)

    data = pandas.read_csv("csv/50_states.csv")
    states = data["state"].to_list()
    number_of_states = len(states)
    guessed_states = []
    number_of_guessed_states = 50 #len(guessed_states)
    answer_state = ""

    state_writer = turtle.Turtle()
    state_writer.color("black")
    state_writer.penup()
    state_writer.hideturtle()

    # new_york = data[states["state"] == "New York"]
    # new_york.reset_index(drop=True)
    # x = new_york.x.iloc[0]
    # print(x)

    while number_of_guessed_states != number_of_states and answer_state != "exit":
        answer_state = screen.textinput(title=f"{number_of_guessed_states}/{number_of_states} States Correct",
                                        prompt="What's another state's name?").title()

        if answer_state in states and answer_state not in guessed_states:
            guessed_states.append(answer_state)
            number_of_guessed_states += 1

            state_data = data[data["state"] == answer_state]
            state_x = state_data["x"].iloc[0]
            state_y = state_data["y"].iloc[0]
            state_writer.goto(state_x, state_y)
            state_writer.write(answer_state, align="center", font=("Arial", 8, "normal"))

    if number_of_guessed_states == number_of_states:
        name_of_winner = screen.textinput(title="Game Over", prompt="Congrats! Save your name in the winner's list:")
        with open("csv/50_states_winners.csv", mode="a") as file:
            file.write(f"{name_of_winner}\n")

    # screen.exitonclick()
