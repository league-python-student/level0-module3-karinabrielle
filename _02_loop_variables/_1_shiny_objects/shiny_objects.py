from tkinter import simpledialog, Tk
from playsound import playsound




can_play_sounds = True

def play_mister_zee():
    if can_play_sounds:
        playsound('shiny-objects.wav')
    else:
        print("Mister Zee requires shiny objects")



def many_shiny_objects():

    amount = simpledialog.askstring(title="", prompt="How many objects would you like?")

    for i in range(int(amount)):
            play_mister_zee()

    # TODO 1) Call the method above to play Mister Zee

    # TODO 2) Ask the user how many shiny objects they want

    # TODO 3) Play the sound that many times

    pass


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    many_shiny_objects()
