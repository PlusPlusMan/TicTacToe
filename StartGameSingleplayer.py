import tkinter as tk
from PIL import Image, ImageFilter, ImageTk
import glob
from time import strftime
from applybg import apply_background2

point_list = []
def game_points(event):
    point_list.append(event)
    sum_a = sum([ _[0] for _ in point_list])
    sum_b = sum([ _[1] for _ in point_list ])

    return sum_a, sum_b

class GameInfoFrame(tk.Frame):
    def __init__(self, *args, header_name="Game info", **kwargs):
        super().__init__(*args, **kwargs)
        self.header_name = header_name
        self.header = tk.Label(self, text=self.header_name)
        self.header.grid(row=0, column=0, sticky='n', padx=10, pady=10)

        def time():
            t = strftime('%H:%M:%S %p')
            d = strftime('%A, %B, %Y')
            self.lbl.configure(text=f"{d}\n{t}")
            self.lbl.after(1000, time)

        self.lbl = tk.Label(self, font=('calibri', 20, 'italic'))
        self.lbl.grid(row=1, column=0, sticky='n', pady=20)
        time()

        point_list = []

        def game_points(event=None):
            if event is not None:
                point_list.append(event)
            sum_a = sum([_[0] for _ in point_list])
            sum_b = sum([_[1] for _ in point_list])
            self.points.configure(text=f"Player A: {str(sum_a)}\nPlayer B: {str(sum_b)}")
            self.points.after(1000, game_points)

        self.points = tk.Label(self, font=('calibri', 20))
        self.points.grid(row=2, column=0, sticky='n', pady=20)
        game_points()


class StartGameSingleplayer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        apply_background2(self, x=5)

        # Grid settings
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Playing board image
        img = Image.open("image/base/board_400x350.png").convert("RGBA")
        ph = ImageTk.PhotoImage(img, size=(400, 400))
        self.board_label = tk.Label(self,
                                    height=400,
                                    width=400,
                                    image=ph)
        #self.board_label.grid(row=0, column=0, padx=20, sticky='w')
        self.board_label.place(anchor="w", relx=0.05, rely=0.5)

        # Game info frame
        self.game_info_frame = GameInfoFrame(self, header_name="Game info")
        self.game_info_frame.grid(row=0, column=1, sticky='e', padx=20, pady=20)
