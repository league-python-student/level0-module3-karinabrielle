from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story

window = Tk()
window.withdraw()

simpledialog.askstring(title="", prompt="Hello, today we will be creating a story together, so lets get started!!!")
character = simpledialog.askstring(title="", prompt="Who would you like your main character to be? Your choices are a wild wolf, a wild fox, a stray dog, or a stray cat! Sorry, there"
 "aren't any more choices.")
if character == "a wild wolf":
    messagebox.showinfo(message="OK, cool, cool.")
elif character == "a wild fox":
    messagebox.showinfo(message="Nice.")
elif character == "a stray cat":
    messagebox.showinfo(message="Awesome.")
elif character == "a stray dog":
    messagebox.showinfo(message="Awesome.")
else:
    character2 = simpledialog.askstring(title='', prompt="Please pick between one of the choices: a wild wolf, a wild fox, a stray dog, or a stray cat.")
    if character2 == "a wild wolf":
        messagebox.showinfo(message="OK, cool, cool.")
    elif character2 == "a wild fox":
        messagebox.showinfo(message="Nice.")
    elif character2 == "a stray cat":
        messagebox.showinfo(message="Awesome.")
    elif character2 == "a stray dog":
        messagebox.showinfo(message="Awesome.")
    else:
        messagebox.showinfo(message="OK, if you can't choose ")








































































