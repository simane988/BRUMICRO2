import tkinter as tk

from src.abstract_classes.VerticalMenuFrameABC import VerticalMenuFrameABC


class AudioNegativeMenu(VerticalMenuFrameABC):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.buttons = [
            tk.Button(self, text='Ввод новой плёнки', background=self.button_bg),
            tk.Button(self, text='Из архивов', background=self.button_bg),
            tk.Button(self, text='Назначить эталон', background=self.button_bg),
            tk.Button(self, text='Удаление файлов', background=self.button_bg),
            tk.Button(self, text='Просмотр журнала', background=self.button_bg),
        ]
        self.buttons_exec = [
            None,  # Ввод новой плёнки
            None,  # Из архива
            None,  # Назначить эталон
            None,  # Удаление файлов
            None,  # Просмотр журнала
        ]

        self.button_amount = len(self.buttons)
