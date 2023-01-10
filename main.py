from guizero import App, PushButton, Text, Window, TextBox

username = []
names = []
data_save = None

def vote():
    global names

    def vote_press():
        app.info("Success", "Vote Recorded!")

    vote_window = Window(app, layout="grid")
    vote_window.bg = "#003459"

    button1 = PushButton(vote_window, text="Vote", grid=[1, 1], command=vote_press)
    message1 = Text(vote_window, text=names[0], grid=[2, 1])
    message1.bg = "white"

    button2 = PushButton(vote_window, text="Vote", grid=[1, 3], command=vote_press)
    message2 = Text(vote_window, text=names[1], grid=[2, 3])
    message2.bg = "white"

    button3 = PushButton(vote_window, text="Vote", grid=[1, 5], command=vote_press)
    message3 = Text(vote_window, text=names[2], grid=[2, 5])
    message3.bg = "white"

    button4 = PushButton(vote_window, text="Vote", grid=[1, 7], command=vote_press)
    message4 = Text(vote_window, text=names[3], grid=[2, 7])
    message4.bg = "white"

def results():
    window = Window(app, title="Results")
    window.show(wait=True)

def save_data():
    global names, data_save, text_box

def register():
    register_window = App(layout="grid")
    TextBox(register_window, text ="Input your name", grid=[1, 1])
    data_save = PushButton(register_window, text="Save Name", grid=[2, 1], command= save_data)


app = App(title="Main window")
app.bg = "#003459"
open_button1= PushButton(app, text="Register", command=register)
open_button2= PushButton(app, text="Vote", command=vote)
open_button3= PushButton(app, text="Results", command=results)

app.display()
