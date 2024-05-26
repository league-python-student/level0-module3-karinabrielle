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

    # =====================================================MAIN CHARACTER======================================================

    character = simpledialog.askstring(title="", prompt="Who would you like your main character to"
    " be? Write down the number you want to choose... \n 1. A wild wolf \n 2. A"
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
    elif choice1 > 0:
        messagebox.showinfo(message="The choices were 1, 2, 3, or 4, but since you did not choose any of the"
                                        "choices, we will choose one for you.")

        mcharacter_choices = ["a wild fox", "a wild wolf", "a stray cat", "a stray dog"]
        character = random.choice(mcharacter_choices)

        messagebox.showinfo(message="Your main character is " + character + "!")

    # ---------------------------------------------------NAME OF CHARACTER------------------------------------------------

    character_name = simpledialog.askstring(title="", prompt="What will be your main character"
                                                "'s name? For inspiration, some names are "
                                                "Snoopy, Olive, Checkers, Luna,"
                                                " or Autumn, but you can create your own name for your character"
                                                             "if you want to.")
    # -------------------------------------------LOCATION OF CHARACTER--------------------------------------------------------
    setting = simpledialog.askstring(title="", prompt="Where is " + character_name + " located? Write down the number you want to choose... \n 1. In a forest \n 2."
                                                                                         " On the streets \n 3. In a desert \n 4. We will choose for you")

    choicetwo = ["0", "1", "2", "3", "4"]

    choice2 = choicetwo.index(setting)

    if choice2 == 1:
        messagebox.showinfo(message="Awesome choice!")
    elif choice2 == 2:
        messagebox.showinfo(message="Awesome choice!")
    elif choice2 == 3:
        messagebox.showinfo(message="Awesome choice!")
    elif choice2 == 4:
        messagebox.showinfo(message="Alright, we will choose a setting for you...")
        setting_choices = ["in a forest", "on the streets", "in a desert"]
        setting = random.choice(setting_choices)

        messagebox.showinfo(message="Your character is located " + setting + "!")

    elif choice2 > 0:
        messagebox.showinfo(message="The choices were 1, 2, 3, or 4, but since you did not choose any of the"
                                            "choices, so we will choose a setting for you.")

        setting_choices = ["in a forest, on the streets, in a desert"]
        setting = random.choice(setting_choices)

        messagebox.showinfo(message="Your character is located " + setting + "!")

    # =============================================WHAT THE CHARACTER IS DOING============================================================























































