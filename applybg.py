import glob
import random
from PIL import Image, ImageFilter, ImageTk
import tkinter as tk

"""
This module is not in use
"""

def apply_background(x):
    background_images = [_ for _ in glob.glob("image/bg/*.jpg")]
    image = random.choice(background_images)
    image = Image.open(image, mode='r')
    image = image.filter(ImageFilter.GaussianBlur(x))
    image = image.convert("RGBA")
    image.save("image/bg/temp.png")
    return "image/bg/temp.png"

def apply_background2(self, x):
    background_images = [_ for _ in glob.glob("image/bg/*.jpg")]
    image = random.choice(background_images)
    image = Image.open(image, mode='r')
    image = image.filter(ImageFilter.GaussianBlur(x))
    image = image.convert("RGBA")
    image.save("image/bg/temp.png")
    img = ImageTk.PhotoImage(Image.open(apply_background(x=0)).resize((750, 500), Image.ANTIALIAS))
    lbl = tk.Label(self, image=img)
    lbl.img = img  # Keep a reference in case this code put is in a function.
    lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.
