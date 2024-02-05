import tkinter as tk

from src.abstract_classes.VerticalMenuFrameABC import VerticalMenuFrameABC


class ColorNegativeMenu(VerticalMenuFrameABC):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.buttons = [
            tk.Button(self, text='Цветной негатив', background=self.button_bg),
            tk.Button(self, text='Цветной негатив', background=self.button_bg),
            tk.Button(self, text='Цветной негатив', background=self.button_bg),
            tk.Button(self, text='Цветной негатив', background=self.button_bg),
        ]
        self.buttons_exec = [
            None,  # Цветной негатив
            None,  # Цветной негатив
            None,  # Цветной негатив
            None,  # Цветной негатив
        ]

        self.button_amount = len(self.buttons)
