import random
import turtle
import sys
from tkinter import simpledialog, messagebox


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    #      3) Set the pen width to 10
    #      4) Ask the user what color pen they would like to draw with
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    hi = turtle.Turtle()

    messagebox.showinfo(message='In this program you will be able to make a square in any spot'
                                'with a color of your choice. Type "exit" to leave the program. ')

    for i in range(9999999):
        color = simpledialog.askstring(title="", prompt='What color of a pen would you like to use? \n '
        'Type the color you would like to use in this box')

        if color == "red" :
            hi.pencolor("red")
            hi.color("red")
        elif color == "orange" :
            hi.pencolor("orange")
            hi.color("orange")
        elif color == "yellow" :
            hi.pencolor("yellow")
            hi.color("yellow")
        elif color == "green" :
            hi.pencolor("green")
            hi.color("green")
        elif color == "blue" :
            hi.pencolor("blue")
            hi.color("blue")
        elif color == "purple" :
            hi.pencolor("purple")
            hi.color("purple")
        elif color == "pink" :
            hi.pencolor("pink")
            hi.color("pink")
        elif color == "brown" :
            hi.pencolor("brown")
            hi.color("brown")
        elif color == "black" :
            hi.pencolor("black")
            hi.color("black")
        elif color == "gray" :
            hi.pencolor("gray")
            hi.color("gray")
        elif color == "" :
            messagebox.showinfo(message="Wow! I-I think the pro- beep! Is br- beep! beep! x_x")
            sys.exit(0)
        elif color == "exit" :
            sys.exit(0)
        else:
            color2 = simpledialog.askstring(title='', prompt='Since we cannot do that color, then we will kindly ask you to pick a different color. :)')
            if color2 == "red":
                hi.pencolor("red")
                hi.color("red")
            elif color2 == "orange":
                hi.pencolor("orange")
                hi.color("orange")
            elif color2 == "yellow":
                hi.pencolor("yellow")
                hi.color("yellow")
            elif color2 == "green":
                hi.pencolor("green")
                hi.color("green")
            elif color2 == "blue":
                hi.pencolor("blue")
                hi.color("blue")
            elif color2 == "purple":
                hi.pencolor("purple")
                hi.color("purple")
            elif color2 == "pink":
                hi.pencolor("pink")
                hi.color("pink")
            elif color2 == "brown":
                hi.pencolor("brown")
                hi.color("brown")
            elif color2 == "black":
                hi.pencolor("black")
                hi.color("black")
            elif color2 == "gray":
                hi.pencolor("gray")
                hi.color("gray")
            elif color2 == "":
                messagebox.showinfo(message="Wow! I-I think the pro- beep! Is br- beep! beep! x_x")
                sys.exit(0)
            elif color == "exit":
                sys.exit(0)

        hi.pensize(10)

        hi.penup()
        hi.setposition(random.randint(-450, 450),random.randint(-450, 450))
        hi.pendown()
        for i in range(4):
            hi.forward(100)
            hi.right(90)







    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
