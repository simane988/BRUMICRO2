import tkinter as tk

from src.abstract_classes.VerticalMenuFrameABC import VerticalMenuFrameABC


class SettingsMenu(VerticalMenuFrameABC):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.buttons = [
            tk.Button(self, text='Настройки', background=self.button_bg),
            tk.Button(self, text='Настройки', background=self.button_bg),
            tk.Button(self, text='Настройки', background=self.button_bg),
            tk.Button(self, text='Настройки', background=self.button_bg),
        ]
        self.buttons_exec = [
            None,  # Настройки
            None,  # Настройки
            None,  # Настройки
            None,  # Настройки
        ]

        self.button_amount = len(self.buttons)
