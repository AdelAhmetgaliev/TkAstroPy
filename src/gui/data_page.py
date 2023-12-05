from tkinter import ttk


class DataPage(ttk.Frame):
    def __init__(self, master, controller) -> None:
        super().__init__(master)
        self.controller = controller

        self._init_widgets()

    def _init_widgets(self):
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=2)

        self.flow_label_frame = ttk.Labelframe(self, text='Потоки')
        self.graph_label_frame = ttk.Labelframe(self, text='Выбор графиков')

        self.star_flow_with_noise_label = ttk.Label(
                self.flow_label_frame, text='От звезды с шумом:\t0.0')
        self.noise_flow_label = ttk.Label(
                self.flow_label_frame, text='От окружающего шума:\t0.0')
        self.star_flow_without_noise_label = ttk.Label(
                self.flow_label_frame, text='От звезды без шума:\t0.0')

        self.x_graph_check_button = ttk.Checkbutton(
                self.graph_label_frame, text='По оси X')
        self.y_graph_check_button = ttk.Checkbutton(
                self.graph_label_frame, text='По оси Y')
        self.z_graph_check_button = ttk.Checkbutton(
                self.graph_label_frame, text='По оси Z')

        self.flow_label_frame.grid(
            column=0, row=0,
            padx=10, pady=20,
            sticky='nswe'
        )
        self.graph_label_frame.grid(
            column=0, row=1,
            padx=10, pady=20,
            sticky='nswe'
        )

        self.star_flow_with_noise_label.grid(
            column=0, row=0,
            padx=10, pady=20,
            sticky='nswe'
        )
        self.noise_flow_label.grid(
            column=0, row=1,
            padx=10, pady=20,
            sticky='nswe'
        )
        self.star_flow_without_noise_label.grid(
            column=0, row=2,
            padx=10, pady=20,
            sticky='nswe'
        )

        self.x_graph_check_button.grid(
            column=0, row=0,
            padx=10, pady=20,
            sticky='nswe'
        )
        self.y_graph_check_button.grid(
            column=0, row=1,
            padx=10, pady=20,
            sticky='nswe'
        )
        self.z_graph_check_button.grid(
            column=0, row=2,
            padx=10, pady=20,
            sticky='nswe'
        )

    def update_labels(self, star_flow: float, noise_flow: float, total_flow: float):
        self.star_flow_with_noise_label['text'] = f'От звезды с шумом:\t{star_flow}'
        self.noise_flow_label['text'] = f'От окружающего шума:\t{noise_flow}'
        self.star_flow_without_noise_label['text'] = f'От звезды без шума:\t{total_flow}'

