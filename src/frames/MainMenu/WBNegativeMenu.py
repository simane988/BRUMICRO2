import tkinter as tk

from src.abstract_classes.VerticalMenuFrameABC import VerticalMenuFrameABC


class WBNegativeMenu(VerticalMenuFrameABC):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.buttons = [
            tk.Button(self, text='Чёрно-белый негатив', background=self.button_bg),
            tk.Button(self, text='Чёрно-белый позитив', background=self.button_bg),
            tk.Button(self, text='Цветной негатив', background=self.button_bg),
            tk.Button(self, text='Цветной позитив', background=self.button_bg),
            tk.Button(self, text='Аудио негатив', background=self.button_bg),
            tk.Button(self, text='Аудио позитив', background=self.button_bg),
        ]
        self.buttons_exec = [
            None,  # Чёрно-белый негатив
            None,  # Чёрно-белый позитив
            None,  # Цветной негатив
            None,  # Цветной позитив
            None,  # Аудио негатив
            None,  # Аудио позитив
        ]

        self.button_amount = len(self.buttons)
