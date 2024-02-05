import tkinter as tk
from src.frames.MainMenu.RootChoiceMenu import RootChoiceMenu
from src.frames.MainMenu.WBNegativeMenu import WBNegativeMenu


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.cur_frame = None
        self.frames_history = []

        # SETTINGS
        self.columns_amount = 5
        self.rows_amount = 1
        self.submenus = [
            RootChoiceMenu,
            WBNegativeMenu
        ]

        for r in range(self.rows_amount):
            self.rowconfigure(index=r, weight=1)
        for c in range(self.columns_amount):
            self.columnconfigure(index=c, weight=1)

        self.frames = {}
        for F in self.submenus:
            page_name = F.__name__
            frame = F(parent=self, controller=parent)
            self.frames[page_name] = frame

        self.show_frame('RootChoiceMenu', 0)

    def show_frame(self, frame_name, pos):
        self.cur_frame = self.frames[frame_name]
        self.cur_frame.grid(row=0, column=pos, sticky='nsew')
        self.cur_frame.activate()
        self.frames_history.append(self.cur_frame)
        self.cur_frame.tkraise()

    def go_back(self):
        if len(self.frames_history) == 1:
            return
        self.frames_history.remove(self.cur_frame)
        self.cur_frame.grid_forget()
        self.cur_frame = self.frames_history[-1]
        self.cur_frame.activate()
