from tkinter import simpledialog, messagebox, Tk
import random
# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story

window = Tk()
window.withdraw()
if __name__ == '__main__':

    simpledialog.askstring(title="", prompt="""Hello, today we will be creating a story together, so lets get started!!!""")
    character = simpledialog.askstring(title="", prompt="Who would you like your main character to"
    " be? Write down the number you want to choose. \n 1. A wild wolf \n 2. A"
    " wild fox \n 3. A stray dog \n 4. A"
    " stray cat")

    choiceone = ["0", "1", "2", "3", "4"]

    choice1 = choiceone.index(character)

    if choice1 == 1:
        messagebox.showinfo(message="Awesome choice!")
    elif choice1 == 2:
        messagebox.showinfo(message="Awesome choice!")
    elif choice1 == 3:
        messagebox.showinfo(message="Awesome choice!")
    elif choice1 == 4:
        messagebox.showinfo(message="Awesome choice!")
    else:
        messagebox.showinfo(message="The choices were 1, 2, 3, or 4, but since you did not choose any of the "
                                        "choices, we will choose one for you.")

        mcharacter_choices = ["a wild fox", "a wild wolf", "a stray cat", "a stray dog"]
        character = random.choice(mcharacter_choices)

        messagebox.showinfo(message="Your main character is " + character + "!")

    character_name = simpledialog.askstring(title="", prompt="What will be your main character"
                                                "'s name? For inspiration, some names are "
                                                "Snoopy, Olive, Checkers, Luna,"
                                                " Aspen, or Autumn, but you can create your own name for your character"
                                                             "if you want to.")

    what = simpledialog.askstring(title="", prompt="Alright, what will " + character_name + " "
    "be doing at the time? The choices are that " + character_name + " will be walking in a forest, " + character_name + " will be walking on the street, " +
                           character_name + "will be eating some food they found, or " + character_name + "will be laying down on the sidewalk staring at all the"
                           "pets playing with their owners.")
    messagebox.showinfo(message="Alright, let's move on!")
    simpledialog.askstring(title="", prompt='What will your main character do next? Will ' + character_name + 'see a fish that looks delicious? '
                        '')



























































