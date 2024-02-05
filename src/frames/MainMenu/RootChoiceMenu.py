import sys
import tkinter as tk

from src.abstract_classes.VerticalMenuFrameABC import VerticalMenuFrameABC
# from src.frames.MainMenu.MainMenu import MainMenu


class RootChoiceMenu(VerticalMenuFrameABC):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.buttons = [
            tk.Button(self, text='Чёрно-белый негатив', background=self.button_bg),
            tk.Button(self, text='Чёрно-белый позитив', background=self.button_bg),
            tk.Button(self, text='Цветной негатив', background=self.button_bg),
            tk.Button(self, text='Цветной позитив', background=self.button_bg),
            tk.Button(self, text='Аудио негатив', background=self.button_bg),
            tk.Button(self, text='Аудио позитив', background=self.button_bg),
            tk.Button(self, text='Седьмой тип плёнки', background=self.button_bg),
            tk.Button(self, text='Настройки', background=self.button_bg),
            tk.Button(self, text='Выход', background=self.button_bg)
        ]
        self.buttons_exec = [
            self.show_wb_neg,  # Чёрно-белый негатив
            None,  # Чёрно-белый позитив
            None,  # Цветной негатив
            None,  # Цветной позитив
            None,  # Аудио негатив
            None,  # Аудио позитив
            None,  # Седьмой тип плёнки
            None,  # Настройки
            self.exit  # Выход
        ]

        self.button_amount = len(self.buttons)

    def exit(self):
        sys.exit()

    def show_wb_neg(self):
        self.parent.show_frame('WBNegativeMenu', 1)
