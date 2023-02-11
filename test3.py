import logging
import tkinter as tk
from itertools import chain
from PIL import Image, ImageTk
from check_win import check_win
from debug_logs import debug_logs
from game_info import GameInfoFrame

# Global variable declaration of player_turn : variates beetwen 0 and 1
player_turn = 0
board_list = [[None for _ in range(3)] for _ in range(3)]

result, winner, = None, None


class StartGameHotSeat(tk.Frame):
    debug_logs()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.fig_img_id = None
        self.controller = parent
        self.canvas = tk.Canvas(self, width=750, height=500)
        self.canvas.pack()

        # Process background image
        self.bg_img = Image.open("image/bg/temp.png")
        self.bg_img = self.bg_img.resize((750, 500), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.bg_img_id = self.canvas.create_image(375, 250, image=self.bg_img, anchor=tk.CENTER)

        # Process board image
        self.board_img = Image.open("image/base/board.png")
        self.board_img = self.board_img.resize((300, 300), Image.ANTIALIAS)
        self.board_img = ImageTk.PhotoImage(self.board_img)
        self.board_img_padx = 15
        self.board_img_pady = 100
        self.board_img_id = self.canvas.create_image(self.board_img_padx, self.board_img_pady, image=self.board_img,
                                                     anchor=tk.NW)
        # Draw a rectangle around the board
        self.img2_rect_id = self.canvas.create_rectangle(self.board_img_padx, self.board_img_pady,
                                                         self.board_img_padx + 300, self.board_img_pady + 300,
                                                         outline="black", width=2)

        # Open circle and cross images
        self.circle_img = Image.open("image/base/circle2.png")
        self.circle_img = self.circle_img.resize((83, 83), Image.ANTIALIAS)
        self.circle_img = ImageTk.PhotoImage(self.circle_img)
        self.cross_img = Image.open("image/base/cross2.png")
        self.cross_img = self.cross_img.resize((83, 83), Image.ANTIALIAS)
        self.cross_img = ImageTk.PhotoImage(self.cross_img)

        # Define single square size on playing board
        self.square_width = 300 / 3
        self.square_height = 300 / 3

        # Binding event
        self.canvas.bind("<Button-1>", self.process_click)  # Listens for mouse click with process_click function

        # Place game info frame on the canvas, then update it every time a winner is detected
        def game_info_frame(start=False):
            global winner
            if winner is not None or start:
                self.game_info_frame = GameInfoFrame(self, pointer=winner)
                self.game_info_frame = self.canvas.create_window(425, 50, anchor=tk.NW, window=self.game_info_frame)
            winner = None
            self.after(1, game_info_frame)
        game_info_frame(True)

    def process_click(self, event):
        global player_turn, board_list
        win_grid = None
        square_size = 100
        a = event.x
        b = event.y
        x = int((a - self.board_img_padx) / square_size)
        y = int((b - self.board_img_pady) / square_size)
        print("Clicked square: ({}, {})\tcoordinates: ({}, {})".format(x, y, a, b))
        logging.info(f"player turn = {player_turn}")
        logging.info(f"x={x}, y={y}")

        # Check if mouse click is vaiable and check if square is already filled, if not, place figure on square
        if x not in (0, 1, 2) or y not in (0, 1, 2) or board_list[x][y] is not None:
            logging.warning(f"wrong coordinates for x={x}, y={y}")
            logging.warning(f"square already filled for boardlist[{x}][{y}]")
            return
        else:
            global result, winner
            board_list[x][y] = player_turn
            self.add_figure(x, y)
            logging.info(f"value = {player_turn} got placed on square x={x}, y={y}")
            logging.info(f"board={board_list}")
            logging.info(f"check_win={check_win(board_list)}")
            # Checks for win, if detected, extract winner and winning grid from check_win function, else pass
            try:
                result = check_win(board_list)
                if result:
                    winner, win_grid = result
                    self.draw_win_grid(win_grid)
            except (TypeError, ValueError):
                pass
            logging.info(f"winner={winner}, win_grid={win_grid}")
            print(f"winner={winner}, win_grid={win_grid}")

        player_turn = 1 - player_turn

    def add_figure(self, x, y):
        # Place figure on square
        if player_turn == 0:
            self.canvas.create_image(x * 100 + 65, y * 100 + 145, anchor="center", image=self.circle_img)
        if player_turn == 1:
            self.canvas.create_image(x * 100 + 65, y * 100 + 150, anchor="center", image=self.cross_img)

    def draw_win_grid(self, win_grid, step_size=5):
        ax, ay, bx, by, cx, cy = list(chain(*win_grid))
        print(ax, ay, bx, by, cx, cy)

        start_x = ax*100 + 65
        start_y = ay*100 + 145
        end_x = cx*100 + 65
        end_y = cy*100 + 145

        # Calculate the change in x and y
        delta_x = end_x - start_x
        delta_y = end_y - start_y

        # Calculate the number of steps to animate the line
        steps = max(abs(delta_x), abs(delta_y)) // step_size + 1

        # Calculate the step size for x and y
        x_step = delta_x / steps
        y_step = delta_y / steps

        # Animate the line step by step
        for i in range(steps + 1):
            x = start_x + x_step * i
            y = start_y + y_step * i
            self.canvas.create_line(start_x, start_y, x, y, fill="red", width=5)
            self.update()
            self.after(int(5-0.15*steps))  # 10 milliseconds delay between each step

if __name__ == "__main__":
    root = tk.Tk()
    app = StartGameHotSeat(root, None)
    app.pack()
    root.mainloop()
