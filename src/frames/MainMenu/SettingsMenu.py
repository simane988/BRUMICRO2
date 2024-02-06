import tkinter as tk

from src.abstract_classes.VerticalMenuFrameABC import VerticalMenuFrameABC


class SettingsMenu(VerticalMenuFrameABC):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.buttons = [
            tk.Button(self, text='Названия архивов', background=self.button_bg),
            tk.Button(self, text='Очистить архив', background=self.button_bg),
            tk.Button(self, text='Установки', background=self.button_bg),
            tk.Button(self, text='Доступы', background=self.button_bg),
            tk.Button(self, text='Инструкции', background=self.button_bg),
        ]
        self.buttons_exec = [
            None,  # Названия архивов
            None,  # Очистить архив
            None,  # Установки
            None,  # Доступы
            None,  # Инструкции
        ]

        self.button_amount = len(self.buttons)
