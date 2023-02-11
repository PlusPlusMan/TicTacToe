import customtkinter as CTk
from PIL import Image, ImageFilter, ImageTk
import tkinter as tk
import tkinter.ttk as ttk
import os
import glob
import random
from game_info import *
from time import strftime

CTk.set_appearance_mode("dark")

def apply_background():
    background_images = [_ for _ in glob.glob("image/bg/*.jpg")]
    image = random.choice(background_images)
    image = Image.open(image, mode='r')
    image = image.filter(ImageFilter.GaussianBlur(5))
    image = image.convert("RGBA")
    # image.show() # For testing: to show image
    return image

point_list = []
def game_points(event):
    point_list.append(event)
    sum_a = sum([ _[0] for _ in point_list])
    sum_b = sum([ _[1] for _ in point_list ])

    return sum_a, sum_b

def start_button_callback():
    print("Start button clicked")

class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        #Window config
        self.title("Tic Tac Toe Game - by: @PlusPlusMan")
        self.wm_iconbitmap("image/title_icon/red-icon.ico")
        self.width = 750
        self.height = 500
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        #Grid settings
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=2)
        self.rowconfigure(0, minsize=100, weight=3)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=2)
        self.rowconfigure(4, minsize=200, weight=3)

        #Background image
        self.bg_image = CTk.CTkImage(apply_background(),
                                     size=(self.width, self.height))
        self.bg_image_label = CTk.CTkLabel(self,
                                           image=self.bg_image,
                                           text='')
        self.bg_image_label = self.bg_image_label.place(x=0, y=0)

        #Playing board image
        self.board = CTk.CTkImage(Image.open("image/base/board.png").convert("RGBA"),
                                  size=(400, 350))
        self.board_label = CTk.CTkLabel(self,
                                        image=self.board,
                                        text='')
        self.board_label.grid(row=1, column=0, sticky='w', padx=20)

        self.game_info_frame = GameInfoFrame(self, header_name="Game info")
        self.game_info_frame.grid(row=1, column=1, sticky='n', padx=20, pady=20)

if __name__ == '__main__':
    app = App()
    app.mainloop()
