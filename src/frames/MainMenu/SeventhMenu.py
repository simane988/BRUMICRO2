import tkinter as tk

from src.abstract_classes.VerticalMenuFrameABC import VerticalMenuFrameABC


class SeventhMenu(VerticalMenuFrameABC):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.buttons = [
            tk.Button(self, text='Седьмой тип', background=self.button_bg),
            tk.Button(self, text='Седьмой тип', background=self.button_bg),
            tk.Button(self, text='Седьмой тип', background=self.button_bg),
            tk.Button(self, text='Седьмой тип', background=self.button_bg),
        ]
        self.buttons_exec = [
            None,  # Седьмой тип
            None,  # Седьмой тип
            None,  # Седьмой тип
            None,  # Седьмой тип
        ]

        self.button_amount = len(self.buttons)
