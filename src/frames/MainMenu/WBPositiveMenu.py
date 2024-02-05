import tkinter as tk

from src.abstract_classes.VerticalMenuFrameABC import VerticalMenuFrameABC


class WBPositiveMenu(VerticalMenuFrameABC):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.buttons = [
            tk.Button(self, text='Чёрно-белый позитив', background=self.button_bg),
            tk.Button(self, text='Чёрно-белый позитив', background=self.button_bg),
            tk.Button(self, text='Чёрно-белый позитив', background=self.button_bg),
            tk.Button(self, text='Чёрно-белый позитив', background=self.button_bg),
        ]
        self.buttons_exec = [
            None,  # Чёрно-белый позитив
            None,  # Чёрно-белый позитив
            None,  # Чёрно-белый позитив
            None,  # Чёрно-белый позитив
        ]

        self.button_amount = len(self.buttons)
