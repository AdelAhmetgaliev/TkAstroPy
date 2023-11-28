import tkinter as tk
import tkinter.font as tkFont

from .input_page import InputPage


class TkApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.wm_title('Tkinter Astro App')
        self.wm_geometry(self._get_init_geometry())

        default_font = tkFont.nametofont('TkDefaultFont')
        default_font.configure(size=14)
        self.option_add('*Font', default_font)

        self.frame = InputPage(None, self)

    def _get_init_geometry(self) -> str:
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
    
        app_width = str(screen_width // 2)
        app_height = str(screen_height // 2)

        app_xcenter = str(screen_width // 4)
        app_ycenter = str(screen_height // 4)

        return f'{app_width}x{app_height}+{app_xcenter}+{app_ycenter}'

