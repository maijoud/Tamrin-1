import turtle
window = turtle.Screen()
window.title("Turtle Square Drawing")
drawer = turtle.Turtle()
square_color = input("Enter the color for the square: ")
side_length = int(input("Enter the length of each side of the square: "))

drawer.color(square_color)

for _ in range(4):
    drawer.forward(side_length)
    drawer.right(90)
window.mainloop()