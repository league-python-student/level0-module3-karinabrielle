from tkinter import simpledialog, messagebox, Tk
import webbrowser


# Use this function to play a video from the internet
def play_video(url):
    webbrowser.open(url)

# =================== DO NOT MODIFY THE CODE ABOVE ===========================


if __name__ == '__main__':
    # TODO 1) Make a new window variable, window = Tk()
    #      2) Hide the window using the window's .withdraw() method
    #      3) Ask the user how many cats they have
    #      4) If they have 3 or more cats, tell them they are a crazy cat lady
    #      5) If they have less than 3 cats AND more than 0 cats, call the
    #         play_video function below to show them a cat video
    #      6) If they have 0 cats, show them a video of A Frog Sitting on a
    #         Bench Like a Human

    pass

    window = Tk()

    window.withdraw()

    name = simpledialog.askstring(title="", prompt="Hello! We would like to know more about you, so can "
                                             "you tell us your name?")
    cats = simpledialog.askstring(title="", prompt="That's a cool name, "+ name +". Now, HOW MANY CATS DO "
                                
                                
                                                                          "YOU HAVE?!?!?!????????!")
    if int(cats) > 3:

        messagebox.showinfo(message ="Sorry, I'm just really obsessed with cats.")
        messagebox.showinfo(message ="But man, you really are one of those crazy cat "
                               "ladies!")

        play_video("https://www.youtube.com/watch?v=47msKc3abqo")

    elif int(cats) > 0 and int(cats) < 3:
        messagebox.showinfo(message="Wow nice! Oh, and sorry for yelling at ya like that, I'M JUST REALLY OBSESSED WITH CATS!!!")

        play_video("https://www.youtube.com/shorts/Po098TRdOn4")

    else:
        messagebox.showinfo(message="...")

        play_video("https://www.youtube.com/watch?v=VLVdjLbXdm4")













