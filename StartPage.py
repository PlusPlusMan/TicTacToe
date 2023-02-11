import tkinter as tk
from PIL import Image, ImageTk
import sys
from applybg import apply_background2

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        apply_background2(self, x=0)

        title_label = tk.Label(self, text="Tic Tac Toe Game", font=controller.title_font, bg="black", fg="white")
        title_label.pack(side="top", fill="x", pady=(75, 0))
        subtitle_label = tk.Label(self, text="made by PlusPlusMan", font=controller.subtitle_font, bg="black", fg="white")
        subtitle_label.pack(side="top", fill="x", pady=(0, 20))

        button1 = tk.Button(self, text="Start Game",
                            height=2, width=20, bg="green", fg="black", activebackground="darkgreen",
                            command=lambda: controller.show_frame("StartGame"))
        button2 = tk.Button(self, text="Settings",
                            height=2, width=20, bg="grey", activebackground="darkgrey",
                            command=lambda: controller.show_frame("Settings"))
        button3 = tk.Button(self, text="Quit",
                            height=2, width=20, bg="red", activebackground="darkred",
                            command=lambda: sys.exit(0))

        button1.pack(pady=(0, 10))
        button2.pack(pady=(0, 10))
        button3.pack(pady=(0, 10))
