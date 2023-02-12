import tkinter as tk
from PIL import Image, ImageTk
import sys
from applybg import apply_background2
from pygame import mixer

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        apply_background2(self, x=0)

        # Music settings
        mixer.init()
        self.bg_music = mixer.Sound("audio/bg-music.mp3")
        self.bg_music.play(-1)
        mixer.Sound.set_volume(self.bg_music, 0.02)
        self.button_click1 = mixer.Sound("audio/button-click.mp3")
        self.button_click2 = mixer.Sound("audio/button-click2.mp3")

        # Music setting buttons
        self.mute_music_icon = Image.open("image/buttons/music-mute.png")
        self.mute_music_icon = self.mute_music_icon.resize((32, 32), Image.ANTIALIAS).convert("RGBA")
        self.mute_music_picon = ImageTk.PhotoImage(self.mute_music_icon)
        self.mute_music_button = tk.Button(self, text="mute", image=self.mute_music_picon, cursor="dot",
                                           command=lambda: (
                                               mixer.Sound.set_volume(self.bg_music, 0), self.button_click2.play()))
        self.mute_music_button.place(x=50, y=450)

        self.volume_down_icon = Image.open("image/buttons/music-down.png")
        self.volume_down_icon = self.volume_down_icon.resize((32, 32), Image.ANTIALIAS).convert("RGBA")
        self.volume_down_picon = ImageTk.PhotoImage(self.volume_down_icon)
        self.volume_down_button = tk.Button(self, text="volume down", image=self.volume_down_picon, cursor="dot",
                                            command=lambda: (
                                                mixer.Sound.set_volume(self.bg_music,
                                                                       self.bg_music.get_volume() - 0.02),
                                                self.button_click2.play()))
        self.volume_down_button.place(x=100, y=450)

        self.stop_music_icon = Image.open("image/buttons/music-pause.png")
        self.stop_music_icon = self.stop_music_icon.resize((32, 32), Image.ANTIALIAS).convert("RGBA")
        self.stop_music_picon = ImageTk.PhotoImage(self.stop_music_icon)
        self.stop_music_button = tk.Button(self, text="stop", image=self.stop_music_picon, cursor="dot",
                                           command=lambda: (
                                               mixer.Sound.stop(self.bg_music), self.button_click2.play()))
        self.stop_music_button.place(x=150, y=450)

        self.play_music_icon = Image.open("image/buttons/music-play.png")
        self.play_music_icon = self.play_music_icon.resize((32, 32), Image.ANTIALIAS).convert("RGBA")
        self.play_music_picon = ImageTk.PhotoImage(self.play_music_icon)
        self.play_music_button = tk.Button(self, text="play", image=self.play_music_picon, cursor="dot",
                                           command=lambda:
                                               (mixer.Sound.play(self.bg_music),
                                                self.button_click2.play()) if not mixer.get_busy() else None)
        self.play_music_button.place(x=200, y=450)

        self.volume_up_icon = Image.open("image/buttons/music-up.png")
        self.volume_up_icon = self.volume_up_icon.resize((32, 32), Image.ANTIALIAS).convert("RGBA")
        self.volume_up_picon = ImageTk.PhotoImage(self.volume_up_icon)
        self.volume_up_button = tk.Button(self, text="volume up", image=self.volume_up_picon, cursor="dot",
                                          command=lambda: (
                                              mixer.Sound.set_volume(self.bg_music, self.bg_music.get_volume() + 0.02),
                                              self.button_click2.play()))
        self.volume_up_button.place(x=250, y=450)

        # Title and subtitle
        self.title_label = tk.Label(self, text="Tic Tac Toe Game", font=controller.title_font, bg="black", fg="white")
        self.title_label.pack(side="top", fill="x", pady=(75, 0))
        self.subtitle_label = tk.Label(self, text="made by PlusPlusMan", font=controller.subtitle_font, bg="black",
                                       fg="white")
        self.subtitle_label.pack(side="top", fill="x", pady=(0, 20))

        # Other buttons
        self.start_game_button = tk.Button(self, text="Start Game", cursor="diamond_cross",
                                           height=2, width=20, bg="green", fg="black", activebackground="darkgreen",
                                           command=lambda: controller.show_frame("StartGame"))
        self.settings_button = tk.Button(self, text="Settings", state='disabled', cursor="exchange",
                                         height=2, width=20, bg="grey", activebackground="darkgrey",
                                         command=lambda: controller.show_frame("Settings"))
        self.about_button = tk.Button(self, text="About", cursor="question_arrow",
                                      height=2, width=20, bg="grey", activebackground="darkgrey",
                                      command=lambda: controller.show_frame("About"))
        self.quit_button = tk.Button(self, text="Quit", cursor="pirate",
                                     height=2, width=20, bg="red", activebackground="darkred",
                                     command=lambda: sys.exit(0))

        self.start_game_button.pack(pady=(10, 0))
        self.settings_button.pack(pady=(10, 0))
        self.about_button.pack(pady=(10, 0))
        self.quit_button.pack(pady=(20, 0))
