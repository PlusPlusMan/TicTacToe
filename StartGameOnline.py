import tkinter as tk
from PIL import Image, ImageFilter, ImageTk
import glob
import random

class StartGameOnline(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button2 = tk.Button(self, text="Singleplayer",
                            command=lambda: controller.show_frame("StartGameSingleplayer"))
        button3 = tk.Button(self, text="LAN",
                            command=lambda: controller.show_frame("StartGameLAN"))
        button4 = tk.Button(self, text="Online",
                            command=lambda: controller.show_frame("StartGameOnline"))
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
