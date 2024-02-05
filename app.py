import tkinter as tk
from tkinter import *
from tkinter import ttk
from src.frames.MainMenu.MainMenu import MainMenu


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # SETTINGS
        self.title('BRUMICRO2')  # Задаём заголовок окна
        self.attributes('-fullscreen', True)  # Делаем окно полноэкранным
        self.config(cursor="none")  # Прячем курсор
        self.working_frames = [MainMenu]

        self.win_height = self.winfo_screenheight()
        self.win_width = self.winfo_screenwidth()

        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)

        main_frame.rowconfigure(index=0, weight=1)
        main_frame.columnconfigure(index=0, weight=1)

        self.frames = {}
        for F in self.working_frames:
            page_name = F.__name__
            frame = F(parent=main_frame, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        # for F in [WB_Neg_Menu]:
        #     page_name = F.__name__
        #     frame = F(parent=main_frame, controller=self)
        #     self.frames[page_name] = frame
        #     frame.grid(row=0, column=1, sticky='nsew')

        self.show_main_menu()

    def show_main_menu(self):
        self.show_frame('MainMenu')

    def show_wb_neg_menu(self):
        # self.show_frame('WB_Neg_Menu')
        pass

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# class MainMenu(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#
#         self.rowconfigure(index=0, weight=1)
#         for c in range(5):
#             self.columnconfigure(index=c, weight=1)
#
#         self.frames = {}
#         for F in [FirstMenu]:
#             page_name = F.__name__
#             frame = F(parent=self, controller=parent)
#             self.frames[page_name] = frame
#             frame.grid(row=0, column=0, sticky='nsew')
#
#         self.show_frame('FirstMenu')
#
#     def show_frame(self, page_name):
#         frame = self.frames[page_name]
#         frame.tkraise()
#
#
# class FirstMenu(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent, highlightbackground="blue", highlightthickness=1)
#         self.controller = controller
#         self.btn_cursor = 0
#
#         # SETTINGS
#         self.button_amount = 9
#         self.button_padx = 20
#         self.button_pady = 10
#         self.button_sticky = 'nsew'
#         self.button_bg = 'white'
#         self.button_focus_bg = 'gray'
#
#         self.buttons = [
#             tk.Label(self, text='Чёрно-белый негатив', background=self.button_bg),
#             tk.Label(self, text='Чёрно-белый позитив', background=self.button_bg),
#             tk.Label(self, text='Цветной негатив', background=self.button_bg),
#             tk.Label(self, text='Цветной позитив', background=self.button_bg),
#             tk.Label(self, text='Аудио негатив', background=self.button_bg),
#             tk.Label(self, text='Аудио позитив', background=self.button_bg),
#             tk.Label(self, text='Седьмой тип плёнки', background=self.button_bg),
#             tk.Label(self, text='Настройки', background=self.button_bg),
#             tk.Label(self, text='Выход', background=self.button_bg)
#         ]
#         self.buttons_exec = [
#             self.master.master.master.show_wb_neg_menu()
#         ]
#
#         for c in range(1):
#             self.columnconfigure(index=c, weight=1)
#         for r in range(len(self.buttons)):
#             self.rowconfigure(index=r, weight=1)
#
#         for btn_id in range(len(self.buttons)):
#             self.buttons[btn_id].grid(row=btn_id, column=0,
#                                       sticky=self.button_sticky, pady=self.button_pady, padx=self.button_padx)
#
#         self.bind('<Up>', self.focus_up)
#         self.bind('<Down>', self.focus_down)
#         self.bind('<Enter>', self.focus_exec)
#
#         self.focus_set()
#         self.focus_update()
#
#     def focus_update(self):
#         for i in range(len(self.buttons)):
#             if i == self.btn_cursor:
#                 self.buttons[i].configure(background='gray')
#             else:
#                 self.buttons[i].configure(background='white')
#
#     def focus_exec(self, event):
#         self.buttons_exec[self.btn_cursor]()
#
#     def focus_down(self, event):
#         if self.btn_cursor < len(self.buttons) - 1:
#             self.btn_cursor += 1
#             self.focus_update()
#
#     def focus_up(self, event):
#         if self.btn_cursor > 0:
#             self.btn_cursor -= 1
#             self.focus_update()
#
#
# class WB_Neg_Menu(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent, highlightbackground="blue", highlightthickness=1)
#         self.controller = controller
#         self.btn_cursor = 0
#
#         # SETTINGS
#         self.button_amount = 9
#         self.button_padx = 20
#         self.button_pady = 10
#         self.button_sticky = 'nsew'
#         self.button_bg = 'white'
#         self.button_focus_bg = 'gray'
#
#         self.buttons = [
#             tk.Label(self, text='Чёрно-белый негатив', background=self.button_bg),
#             tk.Label(self, text='Чёрно-белый позитив', background=self.button_bg),
#             tk.Label(self, text='Цветной негатив', background=self.button_bg),
#             tk.Label(self, text='Цветной позитив', background=self.button_bg),
#             tk.Label(self, text='Аудио негатив', background=self.button_bg),
#             tk.Label(self, text='Аудио позитив', background=self.button_bg),
#             tk.Label(self, text='Седьмой тип плёнки', background=self.button_bg),
#             tk.Label(self, text='Настройки', background=self.button_bg),
#             tk.Label(self, text='Выход', background=self.button_bg)
#         ]
#         self.buttons_exec = [
#
#         ]
#
#         for c in range(1):
#             self.columnconfigure(index=c, weight=1)
#         for r in range(len(self.buttons)):
#             self.rowconfigure(index=r, weight=1)
#
#         for btn_id in range(len(self.buttons)):
#             self.buttons[btn_id].grid(row=btn_id, column=0,
#                                       sticky=self.button_sticky, pady=self.button_pady, padx=self.button_padx)
#
#         self.bind('<Up>', self.focus_up)
#         self.bind('<Down>', self.focus_down)
#
#         self.focus_set()
#         self.focus_update()
#
#     def focus_update(self):
#         for i in range(len(self.buttons)):
#             if i == self.btn_cursor:
#                 self.buttons[i].configure(background='gray')
#             else:
#                 self.buttons[i].configure(background='white')
#
#     def focus_down(self, event):
#         if self.btn_cursor < len(self.buttons) - 1:
#             self.btn_cursor += 1
#             self.focus_update()
#
#     def focus_up(self, event):
#         if self.btn_cursor > 0:
#             self.btn_cursor -= 1
#             self.focus_update()


if __name__ == '__main__':
    app = App()
    app.mainloop()
