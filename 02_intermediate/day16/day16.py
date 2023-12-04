import turtle
import prettytable

if __name__ == '__main__':
    table = prettytable.PrettyTable()

    table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
    table.add_column("Type", ["electric", "water", "fire"])

    table.align = 'l'

    print(table)

    # my_screen = turtle.Screen()
    # timmy = turtle.Turtle()
    #
    # timmy.shape("turtle")
    # timmy.color("BlueViolet")
    # timmy.forward(100)
    #
    # my_screen.exitonclick()
