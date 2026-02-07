import tkinter as tk
from tkinter import ttk
from .frames import ContentFrame, BottomFrame
from .grids import cofigure_main_grid, place_main_frames
from .scripts import AppFunctions
import os, sys

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Создать ярлык")
        self.geometry("400x350")
        self.resizable(False, False)
        self.iconbitmap(AppFunctions.resource_path("icon.ico"))

        self.style = ttk.Style()
        self.style.theme_use("vista")

        self.content = ContentFrame(self, self.focus_in, self.focus_out)
        self.bottom = BottomFrame(self, self.on_create, self.exit_true)

        cofigure_main_grid(self)
        place_main_frames(self.content, self.bottom)
    

    def focus_in(self, event):
        AppFunctions.focus_in(self.content, event)
    
    def focus_out(self, event):
        AppFunctions.focus_out(self.content, event)

    def on_create(self):
        return AppFunctions.on_create(self.content)
    
    def exit_true(self):
        self.after(500, self.destroy)