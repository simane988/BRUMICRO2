import tkinter as tk
from tkinter import messagebox


class VerticalMenuFrameABC(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, highlightbackground="black", highlightthickness=3)
        self.parent = parent
        self.controller = controller
        self.btn_cursor = 0

        # SETTINGS
        self.button_amount = 9
        self.button_padx = 20
        self.button_pady = 10
        self.button_sticky = 'nsew'
        self.button_bg = 'white'
        self.button_focus_bg = 'gray'
        self.orientation = 'vertical'

        self.buttons = [
        ]
        self.buttons_exec = [
        ]

    def activate(self):
        self.btn_cursor = 0
        self.update_layout()
        self.bind_keys()
        self.focus_set()
        self.focus_update()

    def reactivate(self):
        self.update_layout()
        self.bind_keys()
        self.focus_set()
        self.focus_update()

    def update_layout(self):
        if self.orientation in ['vertical', 'Vertical', 'vert', 'Vert']:
            for c in range(1):
                self.columnconfigure(index=c, weight=1)
            for r in range(len(self.buttons)):
                self.rowconfigure(index=r, weight=1)
            for btn_id in range(len(self.buttons)):
                self.buttons[btn_id].grid(row=btn_id, column=0,
                                          sticky=self.button_sticky, pady=self.button_pady, padx=self.button_padx)
        elif self.orientation in ['horizontal', 'Horizontal', 'horiz', 'Horiz']:
            for c in range(len(self.buttons)):
                self.columnconfigure(index=c, weight=1)
            for r in range(1):
                self.rowconfigure(index=r, weight=1)
            for btn_id in range(len(self.buttons)):
                self.buttons[btn_id].grid(row=0, column=btn_id,
                                          sticky=self.button_sticky, pady=self.button_pady, padx=self.button_padx)
        else:
            messagebox.showerror('Code Error', f'Class {self.__class__.__name__} orientation is invalid!')

    def bind_keys(self):
        self.bind('<Up>', self.focus_up)
        self.bind('<Down>', self.focus_down)
        self.bind('<Return>', self.focus_exec)
        self.bind('<Escape>', self.back)

    def focus_update(self):
        for i in range(len(self.buttons)):
            if i == self.btn_cursor:
                self.buttons[i].configure(background='gray')
            else:
                self.buttons[i].configure(background='white')

    def focus_exec(self, event):
        self.buttons_exec[self.btn_cursor]()

    def focus_down(self, event):
        if self.btn_cursor < len(self.buttons) - 1:
            self.btn_cursor += 1
        else:
            self.btn_cursor = 0
        self.focus_update()

    def focus_up(self, event):
        if self.btn_cursor > 0:
            self.btn_cursor -= 1
        else:
            self.btn_cursor = self.button_amount - 1
        self.focus_update()

    def back(self, event):
        self.parent.go_back()
