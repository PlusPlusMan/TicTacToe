import tkinter as tk
from PIL import Image, ImageFilter, ImageTk
import glob
from time import strftime
from applybg import apply_background2

class StartGameSingleplayer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
