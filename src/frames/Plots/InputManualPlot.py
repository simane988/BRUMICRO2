import tkinter as tk
import matplotlib

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

matplotlib.use('TkAgg')


class InputManualPlot(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        # self.update_layout()

        self.figure = Figure(figsize=(8, 11))
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self)

        self.plot = self.figure.add_subplot()
        self.plot.plot([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5])

        self.figure_canvas.get_tk_widget().pack(fill=tk.Y)

    def update_layout(self):
        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=5)
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=4)
