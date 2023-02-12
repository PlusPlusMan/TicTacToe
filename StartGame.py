import tkinter as tk
from applybg import apply_background2
from pygame import mixer

class StartGame(tk.Frame):
    def __init__(self, parent, controller):
        # Frame settings
        tk.Frame.__init__(self, parent)
        self.controller = controller
        apply_background2(self, x=0)

        # Music settings
        mixer.init()
        self.button_click1 = mixer.Sound("audio/button-click.mp3")

        self.label = tk.Label(self, text="Choose Game mode", font=controller.title_font, bg="black", fg="white")
        self.label.pack(side="top", fill="x", pady=50)
        self.button1 = tk.Button(self, text="Go to the start page",
                                 height=2, width=20, bg="red", activebackground="darkred",
                                 command=lambda: (controller.show_frame("StartPage"), self.button_click1.play()))
        self.button2 = tk.Button(self, text="Hot Seat",
                                 height=2, width=20, bg="grey", activebackground="darkgrey",
                                 command=lambda: (controller.show_frame("StartGameHotSeat"), self.button_click1.play()))
        self.button3 = tk.Button(self, text="Singleplayer", state="disabled",
                                 height=2, width=20, bg="grey", activebackground="darkgrey",
                                 command=lambda: (controller.show_frame("StartGameSingleplayer"), self.button_click1.play()))
        self.button4 = tk.Button(self, text="LAN", state="disabled",
                                 height=2, width=20, bg="grey", activebackground="darkgrey",
                                 command=lambda: (controller.show_frame("StartGameLAN"), self.button_click1.play()))
        self.button5 = tk.Button(self, text="Online", state="disabled",
                                 height=2, width=20, bg="grey", activebackground="darkgrey",
                                 command=lambda: (controller.show_frame("StartGameOnline"), self.button_click1.play()))
        self.button3.pack(pady=(10, 0))
        self.button2.pack(pady=(10, 0))
        self.button4.pack(pady=(10, 0))
        self.button5.pack(pady=(10, 0))
        self.button1.pack(pady=(20, 0))
