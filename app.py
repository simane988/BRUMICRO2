import tkinter as tk
from tkinter import *
from tkinter import ttk
from src.frames.MainMenu.MainMenu import MainMenu
from src.frames.Plots.InputManualPlot import InputManualPlot


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # SETTINGS
        self.title('BRUMICRO2')  # Задаём заголовок окна
        self.attributes('-fullscreen', True)  # Делаем окно полноэкранным
        self.config(cursor="none")  # Прячем курсор
        self.working_frames = [
            MainMenu,
            InputManualPlot,
        ]
        self.cframe = None

        self.win_height = self.winfo_screenheight()
        self.win_width = self.winfo_screenwidth()

        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.main_frame.rowconfigure(index=0, weight=1)
        self.main_frame.columnconfigure(index=0, weight=1)

        self.cframes = {}
        for F in self.working_frames:
            page_name = F.__name__
            frame = F(parent=self.main_frame, controller=self)
            self.cframes[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_new_manual_plot()

    def show_main_menu(self):
        self.show_frame('MainMenu')

    def show_new_manual_plot(self):
        self.show_frame('InputManualPlot')

    def show_frame(self, page_name):
        # if self.cframe:
        #     self.cframe.grid_forget()
        self.cframe = self.cframes[page_name]
        self.cframe.tkraise()


if __name__ == '__main__':
    app = App()
    app.mainloop()
