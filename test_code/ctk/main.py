import customtkinter as CTk
import tkinter as Tk
import tkinter.font as tkfont
from game_frame import *
from game_info import *
import customtkinter as CTk
from PIL import Image
import os

class App(CTk.CTk):

    def __init__(self, *args, **kwargs):
        CTk.CTk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = CTk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = {}
        for F in (GameFrame, GameFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("GameFrame")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == '__main__':
    app = App()
    app.mainloop()


