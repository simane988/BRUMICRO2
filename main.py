import tkinter as tk
from tkinter import *
from tkinter import ttk


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('BRUMICRO2')  # Задаём заголовок окна
        self.attributes('-fullscreen', True)

        self.win_height = self.winfo_screenheight()
        self.win_width = self.winfo_screenwidth()

        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)

        main_frame.rowconfigure(index=0, weight=1)
        main_frame.columnconfigure(index=0, weight=1)

        self.frames = {}
        for F in [MainMenu]:
            page_name = F.__name__
            frame = F(parent=main_frame, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame('MainMenu')

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.rowconfigure(index=0, weight=1)
        for c in range(5):
            self.columnconfigure(index=c, weight=1)

        self.frames = {}
        for F in [FirstMenu]:
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame('FirstMenu')

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class FirstMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, highlightbackground="blue", highlightthickness=1)
        self.controller = controller

        wb_neg_btn = ttk.Button(self, text='Чёрно-белый негатив')
        wb_pos_btn = ttk.Button(self, text='Чёрно-белый позитив')
        color_neg_btn = ttk.Button(self, text='Цветной негатив')
        color_pos_btn = ttk.Button(self, text='Цветной позитив')
        audio_neg_btn = ttk.Button(self, text='Аудио негатив')
        audio_pos_btn = ttk.Button(self, text='Аудио позитив')
        dont_remember_btn = ttk.Button(self, text='Седьмой тип плёнки')  # TODO: УТОЧНИТЬ И ПОМЕНЯТЬ НАЗВАНИЕ 7-ОГО ТИПА
        settings_btn = ttk.Button(self, text='Настройки')
        exit_btn = ttk.Button(self, text='Выход')

        for c in range(1):
            self.columnconfigure(index=c, weight=1)
        for r in range(9):
            self.rowconfigure(index=r, weight=1)

        wb_neg_btn.grid(row=0, column=0)
        wb_pos_btn.grid(row=1, column=0)
        color_neg_btn.grid(row=2, column=0)
        color_pos_btn.grid(row=3, column=0)
        audio_neg_btn.grid(row=4, column=0)
        audio_pos_btn.grid(row=5, column=0)
        dont_remember_btn.grid(row=6, column=0)
        settings_btn.grid(row=7, column=0)
        exit_btn.grid(row=8, column=0)


if __name__ == '__main__':
    app = App()
    app.mainloop()
