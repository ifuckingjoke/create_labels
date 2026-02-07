from tkinter import ttk
from tkinter import font


class ContentFrame(ttk.Frame):
    def __init__(self, master, focus_in, focus_out):
        super().__init__(master)

        self.create_fonts()

        self.focus_in = focus_in
        self.focus_out = focus_out

        self.entry = ttk.Entry(self)

        self.entry.insert(0, "Вставьте URL-адрес страницы из интернета")

        self.entry.bind("<FocusIn>", self.focus_in)
        self.entry.bind("<FocusOut>", self.focus_out)

        self.title_label = ttk.Label(
            self,
            text="CreateLables",
            font=self.title_font,
            foreground="black"
        )
        self.warning_label = ttk.Label(
            self,
            text='GIDE: вставьте или пропишите url (github.com), после чего нажмите кнопку "Создать" ',
            font=self.warning_font,
            foreground="red",
            wraplength=360,
            justify="center"
        )
        self.succes_label = ttk.Label(
            self,
            text="Успешно!",
            foreground="green",
            justify="center"
        )

        self.title_label.pack(pady=(50, 10))
        self.entry.pack(expand=True, fill="x", padx=20)
        self.warning_label.pack(pady=(10, 0), padx=20)
    
    def create_fonts(self):
        self.title_font = font.Font(size=16, weight="bold")
        self.warning_font = font.Font(size=10, weight="bold")

class BottomFrame(ttk.Frame):
    def __init__(self, master, on_create, exit_true):
        super().__init__(master)

        self.on_create = on_create
        self.exit_true = exit_true
        
        self.button_create = ttk.Button(
            self,
            text="Создать",
            command=self.on_create,
            style="Large.TButton",
            width=15
        )
        
        self.button_exit = ttk.Button(
            self,
            text="Отмена",
            command=self.exit_true,
            style="Large.TButton",
            width=15
        )

        self.button_exit.pack(side="right", padx=(0, 10), pady=10)
        self.button_create.pack(side="right")