from tkinter import ttk
from tkinter import StringVar

import matplotlib.pyplot as plt
from numpy import meshgrid, array

from astro.graph import get_data_from_x_graph, get_data_from_y_graph, get_data_from_z_graph


class DataPage(ttk.Frame):
    def __init__(self, master, controller) -> None:
        super().__init__(master)
        self.controller = controller
        self.chosen_graph_type = StringVar() 

        self._init_widgets()
        self._init_variables()

    def _init_variables(self) -> None:
        self.filepath = ''
        self.star_coord = (0, 0)
        self.radius = 0

    def _init_widgets(self) -> None:
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

        self.x_graph_radio_button = ttk.Radiobutton(
                self.graph_label_frame, text='По оси X',
                value='X', variable=self.chosen_graph_type)
        self.y_graph_radio_button = ttk.Radiobutton(
                self.graph_label_frame, text='По оси Y',
                value='Y', variable=self.chosen_graph_type)
        self.z_graph_radio_button = ttk.Radiobutton(
                self.graph_label_frame, text='По оси Z',
                value='Z', variable=self.chosen_graph_type)

        self.graph_button = ttk.Button(self, text='Построить графики', command=self._build_graphs)

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
        self.graph_button.grid(
            column=0, row=2,
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

        self.x_graph_radio_button.grid(
            column=0, row=0,
            padx=10, pady=20,
            sticky='nswe'
        )
        self.y_graph_radio_button.grid(
            column=0, row=1,
            padx=10, pady=20,
            sticky='nswe'
        )
        self.z_graph_radio_button.grid(
            column=0, row=2,
            padx=10, pady=20,
            sticky='nswe'
        )

    def _build_graphs(self) -> None:
        if self.filepath == '':
            return

        match self.chosen_graph_type.get():
            case 'X':
                plt.title('Энергия звезды по координаты X')
                plt.xlabel('Координата звезды')
                plt.ylabel('Энергия')
                plt.plot(*get_data_from_x_graph(self.filepath, self.star_coord, self.radius))
                plt.show()
            case 'Y':
                plt.title('Энергия звезды по координаты Y')
                plt.xlabel('Координата звезды')
                plt.ylabel('Энергия')
 
                plt.plot(*get_data_from_y_graph(self.filepath, self.star_coord, self.radius))
                plt.show()
            case 'Z':
                z_list, y_list, x_list = get_data_from_z_graph(
                        self.filepath, self.star_coord, self.radius)
                x_list, y_list = meshgrid(x_list, y_list)
                z_list = array(z_list)

                fig = plt.figure()
                ax = fig.add_subplot(projection='3d')

                ax.set_xlabel('Координата звезды по оси X')
                ax.set_ylabel('Координата звезды по оси Y')
                ax.set_zlabel('Энергия')

                ax.plot_surface(x_list, y_list, z_list)

                plt.show()

    def update_labels(self, star_flow: float, noise_flow: float, total_flow: float) -> None:
        self.star_flow_with_noise_label['text'] = f'От звезды с шумом:\t{star_flow}'
        self.noise_flow_label['text'] = f'От окружающего шума:\t{noise_flow}'
        self.star_flow_without_noise_label['text'] = f'От звезды без шума:\t{total_flow}'

    def update_variables(self, filepath: str, star_coord: tuple[int, int], radius: int) -> None:
        self.filepath = filepath
        self.star_coord = star_coord
        self.radius = radius

