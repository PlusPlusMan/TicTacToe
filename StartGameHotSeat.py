import tkinter as tk
import random
from glob import glob
from itertools import chain
from PIL import Image, ImageTk, ImageFilter
from PIL.ImageTk import PhotoImage
from pygame import mixer, mixer_music
from check_win import check_win
from game_info import GameInfoFrame

# Global variable declaration of player_turn : variates beetwen 0 and 1
player_turn = 0
board_list = [[None for _ in range(3)] for _ in range(3)]
bg_list = []
result, winner, winner_copy = None, None, None


class StartGameHotSeat(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #  To run without window borders: parent.overrideredirect(True)
        self.canvas = tk.Canvas(self, width=750, height=500)
        self.canvas.pack()

        # Process audio
        mixer.init()
        self.click1 = mixer.Sound("audio/lclick.mp3")
        self.click2 = mixer.Sound("audio/rclick.mp3")
        self.button_click1 = mixer.Sound("audio/button-click.mp3")
        self.button_click2 = mixer.Sound("audio/button-click2.mp3")

        # Process background image
        for _ in (glob("image/bg/*")):
            bg_list.append(_)  # looks for all images in the bg folder and adds then to a list
        self.bg_img = Image.open(random.choice(bg_list)).filter(
            ImageFilter.GaussianBlur(radius=0))  # 0 is no blur, change if needed
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
            if winner is None:
                try:
                    self.game_info_frame.destroy()
                except AttributeError:
                    pass
            if winner is not None or start:
                self.game_info_frame = GameInfoFrame(self, pointer=winner)
                self.game_info_frame = self.canvas.create_window(425, 50, anchor=tk.NW, window=self.game_info_frame)
            winner = None
            self.after(1, game_info_frame)

        game_info_frame(start=True)

        def restart_game():
            self.button_click1.play()
            global player_turn, board_list, winner
            player_turn = 0
            board_list = [[None for _ in range(3)] for _ in range(3)]
            winner = None
            with open("winner.txt", "w") as f:
                f.write("")
            StartGameHotSeat.destroy(self)
            StartGameHotSeat.__init__(self, parent, controller)
            self.__init__(parent, controller)
            StartGameHotSeat.pack(self)
            StartGameHotSeat.mainloop(self)

        def next_round():
            self.button_click1.play()
            global player_turn, board_list, winner
            player_turn = 0
            board_list = [[None for _ in range(3)] for _ in range(3)]
            for i in StartGameHotSeat.winfo_children(self):
                i.destroy()
            StartGameHotSeat.destroy(self)
            StartGameHotSeat.__init__(self, parent, controller)
            self.__init__(parent, controller)
            StartGameHotSeat.pack(self)
            StartGameHotSeat.mainloop(self)
            GameInfoFrame(self, pointer=winner_copy)

        # Place RESTART button on the canvas
        self.restart_button = tk.Button(self, text="restart",
                                        height=2, width=10, bg="lightblue",
                                        relief="groove", font=("Helvetica", 10, "italic"), fg="black",
                                        command=restart_game)
        self.restart_button = self.canvas.create_window(450, 400, anchor=tk.NW, window=self.restart_button)

        # Place NEXT button on the canvas
        self.next_button = tk.Button(self, text="next", state="disabled",
                                     height=2, width=10, bg="lightblue",
                                     relief="groove", font=("Helvetica", 10, "italic"), fg="black",
                                     command=next_round)
        self.next_button_id = self.canvas.create_window(575, 400, anchor=tk.NW, window=self.next_button)

        # Place back to MENU button on the canvas
        self.back_menu_icon = Image.open("image/buttons/exit.png")
        self.back_menu_icon = self.back_menu_icon.resize((16, 16), Image.ANTIALIAS).convert("RGBA")
        self.back_menu_picon = PhotoImage(self.back_menu_icon)
        self.back_menu = tk.Button(self, image=self.back_menu_picon,
                                   height=16, width=16, bg="pink", activebackground="red", relief="groove",
                                   command=lambda: (self.button_click2.play(), controller.show_frame("StartPage")))
        self.back_menu = self.canvas.create_window(20, 430, anchor=tk.NW, window=self.back_menu)

        # Place back to SETTINGS button on the canvas
        self.back_settings_icon = Image.open("image/buttons/settings.png")
        self.back_settings_icon = self.back_settings_icon.resize((16, 16), Image.ANTIALIAS).convert("RGBA")
        self.back_settings_picon = PhotoImage(self.back_settings_icon)
        self.back_settings = tk.Button(self, image=self.back_settings_picon,
                                       height=16, width=16, bg="lightyellow", activebackground="gold", relief="groove",
                                       command=lambda: (self.button_click2.play(), controller.show_frame("Settings")))
        self.back_settings = self.canvas.create_window(60, 430, anchor=tk.NW, window=self.back_settings)

        # Place back to HOME button on the canvas
        self.back_home_icon = Image.open("image/buttons/home.png")
        self.back_home_icon = self.back_home_icon.resize((16, 16), Image.ANTIALIAS).convert("RGBA")
        self.back_home_picon = PhotoImage(self.back_home_icon)
        self.back_home = tk.Button(self, image=self.back_home_picon,
                                   height=16, width=16, bg="lightgreen", activebackground="green", relief="groove",
                                   command=lambda: (self.button_click2.play(), controller.show_frame("StartGame")))
        self.back_home = self.canvas.create_window(100, 430, anchor=tk.NW, window=self.back_home)

    def process_click(self, event):
        global player_turn, board_list
        square_size = 100  # size of one of the squares on the board
        a = event.x
        b = event.y
        x = int((a - self.board_img_padx) / square_size)
        y = int((b - self.board_img_pady) / square_size)
        print("Clicked square: ({}, {})\tcoordinates: ({}, {})".format(x, y, a, b))

        # Check if mouse click is vaiable and check if square is already filled, if not, place figure on square
        if x not in (0, 1, 2) or y not in (0, 1, 2) or board_list[x][y] is not None or b < 100 or a < 15:  # 15 and 100 are padding of board image
            return
        else:
            global result, winner
            board_list[x][y] = player_turn
            self.add_figure(x, y)  # Place a figure on square
            mixer.Sound.play(self.click1) if player_turn == 0 else mixer.Sound.play(self.click2)  # Play a sound effect
            # Checks for win, if detected, extract winner and winning grid from check_win function, else pass
            try:
                result = check_win(board_list)
                if result:
                    global winner, win_grid, winner_copy
                    winner, win_grid = result
                    print(f"winner={winner}, win_grid={win_grid}")
                    self.draw_win_grid(win_grid)
            except (TypeError, ValueError):
                pass

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

        start_x = ax * 100 + 65
        start_y = ay * 100 + 145
        end_x = cx * 100 + 65
        end_y = cy * 100 + 145

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
            self.after(int(5 - 0.15 * steps))  # 10 milliseconds delay between each step

        # UPDATE STATE OF NEXT_BUTTON
        self.next_button.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    app = StartGameHotSeat(root, None)
    app.pack()
    root.mainloop()
