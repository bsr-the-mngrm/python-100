import turtle

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

    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

    screen.exitonclick()
