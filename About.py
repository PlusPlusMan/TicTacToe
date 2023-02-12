import tkinter as tk
from applybg import *
import webbrowser

text_1 = """
Author: Krystian Kowalik - @PlusPlusMan
AI Algorithm author: ...
Version: 0.1
Date: 2023-02-12
Contact: plusplusman00@gmail.com
        """

text_2 = """
This is a simple game of Tic Tac Toe.
The game is my first GUI project in Python.
I hope you will enjoy it.
        """


class About(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bg_path = apply_background(x=0)
        self.bg_image = tk.PhotoImage(file=self.bg_path)
        self.canvas = tk.Canvas(self, width=750, height=500)
        self.canvas.pack()

        # Rectangle info
        self.bg = self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)
        self.canvas.create_rectangle(75, 50, 675, 350, fill="darkgrey", outline="white", width=2, stipple="gray50")
        self.canvas.create_text(375, 100, text="About the game", font=("Arial", 20), fill="blue")
        self.canvas.create_text(375, 170, text=text_1, font=("Arial", 10), fill="blue")
        self.canvas.create_text(375, 270, text=text_2, font=("Arial", 15), fill="blue")

        self.back_button = self.canvas.create_window(250, 400, window=tk.Button(self,
                                                                                text="Back", height=2, width=20,
                                                                                cursor="hand2",
                                                                                bg="grey", activebackground="darkgrey",
                                                                                command=lambda: controller.show_frame(
                                                                                    "StartPage")))

        self.git_button = self.canvas.create_window(500, 400, window=tk.Button(self,
                                                                               text="GitHub", height=2, width=20,
                                                                               bg="grey", activebackground="darkgrey",
                                                                               cursor="hand2",
                                                                               command=lambda: webbrowser.open(
                                                                                   "https://github.com/PlusPlusMan/TicTacToe")))


if __name__ == "__main__":
    root = tk.Tk()
    app = About(root, None)
    app.pack()
    root.mainloop()
