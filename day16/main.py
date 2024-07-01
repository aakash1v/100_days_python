"""# import turtle
from turtle import Turtle,Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('coral')
print(timmy)
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
"""

from prettytable import PrettyTable
table = PrettyTable()
table.add_column('pokemon Name',['Pickachu','Squirtle','Charmander'])
table.add_column('Type',['Electric','Water','Fire'])

# To align the items to left side..
table.align = "l"  # u can use 'r','c','l'

print(table)
new_table = PrettyTable()
new_table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
new_table.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)
print(new_table)
