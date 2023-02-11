import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
from game_info import GameInfoFrame

class StartGameHotSeat(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.player = "cross"

        # Opening background and board images
        self.background_img = Image.open("image/bg/temp.png")
        self.board_img = Image.open("image/base/board.png")
        # Resizing images
        self.background_img = self.background_img.resize((750, 500), Image.ANTIALIAS).filter(ImageFilter.GaussianBlur(5))
        self.board_img = self.board_img.resize((350, 450), Image.ANTIALIAS)
        self.board_img2 = ImageTk.PhotoImage(self.board_img)
        # Defining background image
        self.background_img.paste(self.board_img, (15, 20), self.board_img)
        self.background_img = ImageTk.PhotoImage(self.background_img)
        self.background_label = tk.Label(self, image=self.background_img)
        self.background_label.pack()

        # Frame that shows game info
        self.game_info_frame = GameInfoFrame(self)
        self.game_info_frame.place(x=425, y=50)

        #===================== Binding events =====================
        self.background_label.bind("<Button-1>", self.process_click)

    def process_click(self, event):
        x, y = event.x, event.y

        # Determine which square was clicked on based on the x and y coordinates
        # Example logic:
        square_width = self.board_img2.width() / 3
        square_height = self.board_img2.height() / 3

        row = int(y // square_height)
        col = int(x // square_width)

        # Use the row and col variables to place the appropriate symbol on the square
        # Example logic:
        cross_img = Image.open("image/base/cross2.png")
        cross_img = cross_img.resize((int(square_width) - 40, int(square_height) - 40), Image.ANTIALIAS)

        cross_img = ImageTk.PhotoImage(cross_img)
        label = tk.Label(self, image=cross_img)
        label.image = cross_img
        label.place(x=col * square_width + 40, y=row * square_height + 40)

if __name__ == "__main__":
    root = tk.Tk()
    app = StartGameHotSeat(root, None)
    app.pack()
    root.mainloop()
