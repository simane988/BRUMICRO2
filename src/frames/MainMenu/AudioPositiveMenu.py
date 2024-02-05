import tkinter as tk

from src.abstract_classes.VerticalMenuFrameABC import VerticalMenuFrameABC


class AudioPositiveMenu(VerticalMenuFrameABC):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.buttons = [
            tk.Button(self, text='Аудио позитив', background=self.button_bg),
            tk.Button(self, text='Аудио позитив', background=self.button_bg),
            tk.Button(self, text='Аудио позитив', background=self.button_bg),
            tk.Button(self, text='Аудио позитив', background=self.button_bg),
        ]
        self.buttons_exec = [
            None,  # Аудио позитив
            None,  # Аудио позитив
            None,  # Аудио позитив
            None,  # Аудио позитив
        ]

        self.button_amount = len(self.buttons)
