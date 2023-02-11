import tkinter as tk
from time import strftime

class GameInfoFrame(tk.Frame):
    def __init__(self, *args, pointer, header_name="Game info", **kwargs):
        super().__init__(*args, **kwargs)
        self.point = pointer
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

        points_a, points_b = [], []
        with open("winner.txt", "r") as f:
            for i in f.read():
                if i == "0":
                    points_a.append(i)
                elif i == "1":
                    points_b.append(i)
                elif i == "2":
                    points_b.append(i)
                    points_a.append(i)
        def game_points(point=None):
            with open("winner.txt", "a+") as f:
                if point is not None:
                    if point == 0:
                        points_a.append(point)
                        f.write(f"{point}")
                    elif point == 1:
                        points_b.append(point)
                        f.write(f"{point}")
                    elif point == 2:
                        points_b.append(point)
                        points_a.append(point)
                        f.write(f"{point}")
            sum_a = len(points_a)
            sum_b = len(points_b)
            self.points.configure(text=f"Player A: {str(sum_a)}\nPlayer B: {str(sum_b)}")
            self.points.after(1000, game_points)

        self.points = tk.Label(self, font=('calibri', 20))
        self.points.grid(row=2, column=0, sticky='n', pady=20)
        game_points(self.point)














        """
                point_list = []
        def game_points(point=None):
            if point is not None:
                point_list.append(point)
            sum_a = sum([_[0] for _ in point_list])
            sum_b = sum([_[1] for _ in point_list])
            self.points.configure(text=f"Player A: {str(sum_a)}\nPlayer B: {str(sum_b)}")
            self.points.after(1000, game_points)

        self.points = tk.Label(self, font=('calibri', 20))
        self.points.grid(row=2, column=0, sticky='n', pady=20)
        game_points((0, 1))
        """
