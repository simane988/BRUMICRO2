import tkinter as tk

from src.abstract_classes.VerticalMenuFrameABC import VerticalMenuFrameABC


class ColorPositiveMenu(VerticalMenuFrameABC):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.buttons = [
            tk.Button(self, text='Цветной позитив', background=self.button_bg),
            tk.Button(self, text='Цветной позитив', background=self.button_bg),
            tk.Button(self, text='Цветной позитив', background=self.button_bg),
            tk.Button(self, text='Цветной позитив', background=self.button_bg),
        ]
        self.buttons_exec = [
            None,  # Цветной позитив
            None,  # Цветной позитив
            None,  # Цветной позитив
            None,  # Цветной позитив
        ]

        self.button_amount = len(self.buttons)
