from tkinter import simpledialog, messagebox, Tk
import random
# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story

window = Tk()
window.withdraw()
if __name__ == '__main__':

    simpledialog.askstring(title="", prompt="Hello, today we will be creating a story together, so lets get started!!!")
    character = simpledialog.askstring(title="", prompt="Who would you like your main character to"
    " be? Your choices are a wild wolf, a"
    " wild fox, a stray dog, or a"
    " stray cat! Sorry, there"
    " aren't any more choices. If you want to"
    " choose a main character, then you will"
    " have to say 'a stray cat' instead of '"
    "stray cat'.")

    if character == "a wild wolf":
        messagebox.showinfo(message="OK, cool, cool.")
    elif character == "a wild fox":
        messagebox.showinfo(message="Nice.")
    elif character == "a stray cat":
        messagebox.showinfo(message="Awesome.")
    elif character == "a stray dog":
        messagebox.showinfo(message="Awesome.")
    else:
        messagebox.showinfo(message="It has to be a stray cat, a stray dog, a wild wolf,"
                                        " or a wild fox. Since you did not choose any of the "
                                        "characters, we will choose one for you.")

        mcharacter_choices = ["a wild fox", "a wild wolf", "a stray cat", "a stray dog"]
        character = random.choice(mcharacter_choices)

        messagebox.showinfo(message = "Your main character is " + character + "!")

    character_name = simpledialog.askstring(title="", prompt="What will be your main character"
                                                "'s name? Some names are "
                                                "Snoopy, Olive, Checkers, Luna,"
                                                " Aspen, or Autumn")

    simpledialog.askstring(title="", prompt="Alright, what will " + character_name + "be doing"
    "at the time? The choices are that " + character_name + "will be walking in a forest,")




























































