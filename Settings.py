import tkinter as tk
from pygame import mixer

class Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        mixer.init()
        label = tk.Label(self, text="Settings", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        self.go_back_button = tk.Button(self, text="Go to the start page",
                                        command=lambda: controller.show_frame("StartPage"))
        self.go_back_button.pack()

