from PIL import Image, ImageFilter, ImageTk
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont
import os
import glob
import random
from time import strftime

point_list = []
def game_points(event):
    point_list.append(event)
    sum_a = sum([_[0] for _ in point_list])
    sum_b = sum([_[1] for _ in point_list])
    return sum_a, sum_b

def start_button_callback():
    print("Start button clicked")


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Window config
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("Tic Tac Toe Game - by: @PlusPlusMan")
        self.wm_iconbitmap("image/title_icon/red-icon.ico")
        self.width = 750
        self.height = 500
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        #Container settings
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #Frames setting
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

        #Background Image
        def apply_background():
            background_images = [_ for _ in glob.glob("image/bg/*.jpg")]
            image = random.choice(background_images)
            image = Image.open(image, mode='r')
            image = image.filter(ImageFilter.GaussianBlur(5))
            image = image.convert("RGBA")
            image.save("image/bg/temp.png")
            self.bg_image = tk.PhotoImage(file="image/bg/temp.png",
                                          width=self.width,
                                          height=self.height)
            self.bg_image_label = tk.Label(self,
                                           image=self.bg_image,
                                           text='')
            self.bg_image_label.pack()
        apply_background()



if __name__ == '__main__':
    app = App()
    app.mainloop()
