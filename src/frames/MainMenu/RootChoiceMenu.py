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
            self.show_wb_pos,  # Чёрно-белый позитив
            self.show_color_neg,  # Цветной негатив
            self.show_color_pos,  # Цветной позитив
            self.show_audio_neg,  # Аудио негатив
            self.show_audio_pos,  # Аудио позитив
            self.show_seventh,  # Седьмой тип плёнки
            self.show_settings,  # Настройки
            self.exit  # Выход
        ]

        self.button_amount = len(self.buttons)

    def exit(self):
        sys.exit()

    def show_wb_neg(self):
        self.parent.show_frame('WBNegativeMenu', 1)

    def show_wb_pos(self):
        self.parent.show_frame('WBPositiveMenu', 1)

    def show_color_neg(self):
        self.parent.show_frame('ColorNegativeMenu', 1)

    def show_color_pos(self):
        self.parent.show_frame('ColorPositiveMenu', 1)

    def show_audio_neg(self):
        self.parent.show_frame('AudioNegativeMenu', 1)

    def show_audio_pos(self):
        self.parent.show_frame('AudioPositiveMenu', 1)

    def show_seventh(self):
        self.parent.show_frame('SeventhMenu', 1)

    def show_settings(self):
        self.parent.show_frame('SettingsMenu', 1)
