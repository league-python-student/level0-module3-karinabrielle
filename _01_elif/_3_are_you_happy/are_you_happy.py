from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements

    window = Tk()

    window.withdraw()

    simpledialog.askstring(title="", prompt="Hey...")

    happy = simpledialog.askstring(title="", prompt="Are you happy? :D")

    if happy == "no":
        want = simpledialog.askstring(title="", prompt="no?... Well... do you want to be happy?")
        if want == "no":
            simpledialog.askstring(title="", prompt="Huh... never mind.")
        elif want == "yes":
            messagebox.showinfo(title="", message="Change something to be happy! And please.")
        else:
            messagebox.showerror(title="", message="")
    elif happy == "yes":
        messagebox.showinfo(title="", message="Oh nice, then you can keep on doing what you were doing. :P")

    else:
        messagebox.showerror(title="", message="")




