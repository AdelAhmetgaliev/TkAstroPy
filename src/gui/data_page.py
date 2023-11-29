from tkinter import ttk


class DataPage(ttk.Frame):
    def __init__(self, master, controller) -> None:
        super().__init__(master)
        self.controller = controller

        self.test_label = ttk.Label(self, text='Test')
        self.test_label.grid(row=0, column=0)

