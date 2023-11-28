import tkinter as tk
from tkinter import ttk


class InputPage(ttk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self._init_widgets()

    def _init_widgets(self):
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=4)

        self.text_input_star_coord_label = ttk.Label(text='Введите координаты звезды:')
        self.text_input_inner_radius_label = ttk.Label(text='Введите внутренний радиус кольца:')
        self.text_input_outer_radius_label = ttk.Label(text='Введите внешний радиус кольца:')
        
        self.star_coord_x = tk.IntVar()
        self.star_coord_y = tk.IntVar()
        self.inner_radius = tk.IntVar()
        self.outer_radius = tk.IntVar()

        self.entry_star_coord_x = ttk.Entry(textvariable=self.star_coord_x)
        self.entry_star_coord_y = ttk.Entry(textvariable=self.star_coord_y)
        self.entry_inner_radius = ttk.Entry(textvariable=self.inner_radius)
        self.entry_outer_radius = ttk.Entry(textvariable=self.outer_radius)
    
        self.text_input_star_coord_label.grid(
                column=0, row=0,
                columnspan=2,
                padx=10, pady=10,
                sticky='w'
        )
        self.entry_star_coord_x.grid(
                column=0, row=1,
                padx=50, pady=3,
                sticky='w'
        )
        self.entry_star_coord_y.grid(
                column=1, row=1,
                padx=10, pady=3,
                sticky='e'
        )
        self.text_input_inner_radius_label.grid(
                column=0, row=2,
                columnspan=2,
                padx=10, pady=20,
                sticky='w'
        )
        self.entry_inner_radius.grid(
                column=0, row=3,
                padx=50, pady=3,
                sticky='e'
        )
        self.text_input_outer_radius_label.grid(
                column=0, row=4, 
                columnspan=2,
                padx=10, pady=20,
                sticky='w'
        )
        self.entry_outer_radius.grid(
                column=0, row=5,
                padx=50, pady=3,
                sticky='e'
        )

