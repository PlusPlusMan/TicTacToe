import tkinter.font as tkfont
from StartPage import *
from StartGame import *
from About import About
from Settings import *
from StartGameSingleplayer import *
from StartGameLAN import *
from StartGameOnline import *
from StartGameHotSeat import *
#TODO: powiadomienie o wygranej, przegranej, remisie
#TODO: dodać nową funkcjonalność do game_info: text label z historią ruchów
#TODO: skończyć Settings dodając możliwość zmiany dźwieku, poziomu trudności, języka, zdjęcia tła
#TODO: napisać multiplayer i lan

# List of all frames that will be used in the app
FRAME_LIST = (StartPage, StartGame, About, Settings, StartGameSingleplayer, StartGameHotSeat, StartGameLAN, StartGameOnline)

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Window config
        #self.overrideredirect(True)  # Remove window borders
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.subtitle_font = tkfont.Font(family='Helvetica', size=12, slant="italic")
        self.title("Tic Tac Toe Game - by: @PlusPlusMan")
        self.wm_iconbitmap("image/title_icon/red-icon.ico")
        self.width = 750
        self.height = 500
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)


        # Clear the winner.txt file from data of previous games
        with open("winner.txt", "w") as f:
            f.write("")

        #Container settings
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #Frames setting
        self.frames = {}
        for F in FRAME_LIST:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # Put all pages in the same location;
            # The one on the top of the stacking order,
            # will be the one that is visible.
            frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == '__main__':
    app = App()
    app.mainloop()
