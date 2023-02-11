import tkinter as tk
from PIL import Image, ImageFilter, ImageTk
import glob
import random
from applybg import apply_background2

class StartGame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        apply_background2(self, x=0)

        label = tk.Label(self, text="Choose Game mode", font=controller.title_font, bg="black", fg="white")
        label.pack(side="top", fill="x", pady=50)
        button1 = tk.Button(self, text="Go to the start page",
                            height=2, width=20, bg="red", activebackground="darkred",
                            command=lambda: controller.show_frame("StartPage"))
        button2 = tk.Button(self, text="Hot Seat",
                            height=2, width=20, bg="grey", activebackground="darkgrey",
                            command=lambda: controller.show_frame("StartGameHotSeat"))
        button3 = tk.Button(self, text="Singleplayer", state="disabled",
                            height=2, width=20, bg="grey", activebackground="darkgrey",
                            command=lambda: controller.show_frame("StartGameSingleplayer"))
        button4 = tk.Button(self, text="LAN", state="disabled",
                            height=2, width=20, bg="grey", activebackground="darkgrey",
                            command=lambda: controller.show_frame("StartGameLAN"))
        button5 = tk.Button(self, text="Online", state="disabled",
                            height=2, width=20, bg="grey", activebackground="darkgrey",
                            command=lambda: controller.show_frame("StartGameOnline"))
        button3.pack()
        button2.pack()
        button4.pack()
        button5.pack()
        button1.pack(pady=(20, 0))
