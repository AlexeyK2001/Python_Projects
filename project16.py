# # class - car; object can be mazda, kia, audi etc
# # objects can have attributes (variables, that are equal to something) and 
# # methods (functions that an object can execute)
# #These attributes and methods are used only by an object
# import another_module

# print(another_module.another_variable)

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# my_screen = Screen()

# print(my_screen.canvheight) #my_screen is an object here, canvheight is an attribute
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "r"
print(table)