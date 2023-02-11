from PIL import Image, ImageFilter, ImageTk
import tkinter as tk
import tkinter.ttk as ttk
import glob
import random
from game_info import *

point_list = []


def game_points(event):
    point_list.append(event)
    sum_a = sum([_[0] for _ in point_list])
    sum_b = sum([_[1] for _ in point_list])

    return sum_a, sum_b


def start_button_callback():
    print("Start button clicked")


class GameFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(self, parent)
        self.controller = controller
        # Window config
        # SWAP: self.title("Tic Tac Toe Game - by: @PlusPlusMan")
        # SWAP: self.wm_iconbitmap("image/title_icon/red-icon.ico")
        self.width = 750
        self.height = 500
        # SWAP: self.geometry(f"{self.width}x{self.height}")
        # SWAP: self.resizable(False, False)

        # Grid settings
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=2)
        self.rowconfigure(0, minsize=100, weight=3)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=2)
        self.rowconfigure(4, minsize=200, weight=3)

        # Playing board image
        self.board = tk.Image(Image.open("image/base/board.png").convert("RGBA"),
                              size=(400, 350))
        self.board_label = tk.Label(self,
                                    image=self.board,
                                    text='')
        self.board_label.grid(row=1, column=0, sticky='w', padx=20)

        # Game info frame
        self.game_info_frame = GameInfoFrame(self, header_name="Game info")
        self.game_info_frame.grid(row=1, column=1, sticky='n', padx=20, pady=20)
