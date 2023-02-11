import customtkinter as CTk
import datetime as dt
from time import strftime

# point_list = []
# def game_points(event):
#     point_list.append(event)
#     sum_a = sum([ _[0] for _ in point_list])
#     sum_b = sum([ _[1] for _ in point_list ])
#
#     return sum_a, sum_b

class GameInfoFrame(CTk.CTkFrame):
    def __init__(self, *args, header_name="Game info", **kwargs):
        super().__init__(*args, **kwargs)
        self.header_name = header_name
        self.header = CTk.CTkLabel(self, text=self.header_name)
        self.header.grid(row=0, column=0, sticky='n', padx=10, pady=10)

        def time():
            t = strftime('%H:%M:%S %p')
            d = strftime('%A, %B, %Y')
            self.lbl.configure(text=f"{d}\n{t}")
            self.lbl.after(1000, time)

        self.lbl = CTk.CTkLabel(self, font=('calibri', 20, 'italic'))
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

        self.points = CTk.CTkLabel(self, font=('calibri', 20))
        self.points.grid(row=2, column=0, sticky='n', pady=20)
        game_points()

