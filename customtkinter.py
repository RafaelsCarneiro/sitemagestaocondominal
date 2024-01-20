import tkinter as tk
from tkinter import ttk

class CTk(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

class CTkButton(ttk.Button):
    def __init__(self, master=None, bg_color=None, fg_color=None, **kwargs):
        ttk.Button.__init__(self, master, **kwargs)
        self.configure_custom(bg_color=bg_color, fg_color=fg_color)

    def configure_custom(self, bg_color=None, fg_color=None, **kwargs):
        style = ttk.Style()
        style.configure("Custom.TButton", padding=6)

        if bg_color:
            style.map("Custom.TButton", background=[("active", bg_color)])
        if fg_color:
            style.map("Custom.TButton", foreground=[("active", fg_color)])

class CTkEntry(ttk.Entry):
    def __init__(self, master=None, **kwargs):
        ttk.Entry.__init__(self, master, **kwargs)

    def get(self):
        return super().get()
class CTkLabel(ttk.Label):
    def __init__(self, master=None, bg_color=None, fg_color=None, **kwargs):
        ttk.Label.__init__(self, master, **kwargs)
        self.configure_custom(bg_color=bg_color, fg_color=fg_color)

    def configure_custom(self, bg_color=None, fg_color=None, **kwargs):
        if bg_color:
            self.configure(background=bg_color)
        if fg_color:
            self.configure(foreground=fg_color)


class CTkTextbox(tk.Text):
    pass

class CTkOptionMenu(ttk.Combobox):
    def __init__(self, master=None, **kwargs):
        ttk.Combobox.__init__(self, master, **kwargs)
        self["values"] = kwargs.get("values", [])
        self.current(0)
