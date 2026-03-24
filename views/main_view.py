import tkinter as tk
from tkinter import font
import ttkbootstrap as ttk

class MainView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Setup view variables
        self.search_type_var = tk.IntVar(value=0) # 0: Raiz, 1: CACEAL, 2: CNPJ
        self.browser_var = tk.IntVar(value=0) # 0: Firefox, 1: Chrome
        
        # Checkbutton vars
        self.city_limoeiro = tk.BooleanVar(value=True)
        self.city_giral = tk.BooleanVar(value=True)
        self.city_taquarana = tk.BooleanVar(value=True)
        self.city_arapiraca = tk.BooleanVar(value=True)
        
        self._build_ui()

    def _build_ui(self):
        # Setup specific options mapped to integers
        self.listaOpt = ["Raiz do CNPJ", "CACEAL", "CNPJ"]
        self.value_inside = tk.StringVar(value=self.listaOpt[0])
        
        framePrincipal = tk.Frame(self)
        
        # Function to map string selection to int index
        def update_search_type(val):
            self.search_type_var.set(self.listaOpt.index(val))

        optbut = ttk.OptionMenu(self, self.value_inside, self.listaOpt[0], *self.listaOpt, style="success", command=update_search_type, direction="below")
        optbut.pack(fill="x")

        frameSide = tk.Frame(framePrincipal)
        ttk.Label(frameSide, text="Cidades:").pack(padx="3", pady=(0, 10))
        
        # City Checkbuttons
        limoeiro = ttk.Checkbutton(frameSide, text="Limoeiro de Anadia", variable=self.city_limoeiro, style="success")
        limoeiro.pack(pady=(0, 10), padx=5, fill="both")

        giral = ttk.Checkbutton(frameSide, text="Giral do Ponciano", variable=self.city_giral, style="success")
        giral.pack(pady=(0, 10), padx=5, fill="both")

        taquarana = ttk.Checkbutton(frameSide, text="Taquarana", variable=self.city_taquarana, style="success")
        taquarana.pack(pady=(0, 10), padx=5, fill="both")

        arapiraca = ttk.Checkbutton(frameSide, text="Arapiraca", variable=self.city_arapiraca, style="success")
        arapiraca.pack(padx=5, fill="both")

        ttk.Separator(frameSide).pack(pady=(15, 0), expand=1, fill="x")
        frameSide.pack(side="top", expand=1, fill="x")

        ttk.Label(framePrincipal, text="Status:").pack(pady=(5, 0))
        self.status_label = ttk.Label(framePrincipal, text="Importar Arquivo", justify=tk.CENTER)
        self.status_label.pack(pady="5", padx="5")

        # Browser choice
        frameRadials = ttk.LabelFrame(framePrincipal, text="Navegador")
        browser_ff = ttk.Radiobutton(frameRadials, text="Firefox", variable=self.browser_var, value=0, style="success")
        browser_ff.pack(side=tk.LEFT, padx=(5, 0))
        
        browser_ch = ttk.Radiobutton(frameRadials, text="Chrome", variable=self.browser_var, value=1, style="success")
        browser_ch.pack(side=tk.RIGHT, padx=(0, 5))
        frameRadials.pack(fill="x", ipadx="5", ipady="5", padx=5, pady=(5, 10))

        # Buttons
        self.btn_import = ttk.Button(framePrincipal, text="Importar", width=34, command=self.controller.handle_import, style="success-outline")
        self.btn_import.pack(pady="5", padx="5")

        self.btn_search = ttk.Button(framePrincipal, text="Buscar", width=34, command=self.controller.handle_search, style="success-outline")
        self.btn_search.pack(pady="5", padx="5")

        version = ttk.Label(framePrincipal, text="v2.0 (MVC)", foreground="#999", font=font.Font(size=8))
        version.pack()

        framePrincipal.pack(padx="10", pady="10", expand=1, fill="both")
        self.pack(expand=1, fill="both")

    def update_status(self, message: str, is_error: bool = False):
        color = "#ff1010" if is_error else "#00aa10"
        self.status_label.configure(text=message, foreground=color)
        self.update_idletasks() # Force UI update immediately

    def get_selected_cities(self) -> list:
        cities = []
        if self.city_limoeiro.get(): cities.append("LIMOEIRO DE ANADIA")
        if self.city_giral.get(): cities.append("GIRAL DO PONCIANO")
        if self.city_taquarana.get(): cities.append("TAQUARANA")
        if self.city_arapiraca.get(): cities.append("ARAPIRACA")
        return cities

    def get_search_type(self) -> int:
        return self.search_type_var.get()

    def get_browser_choice(self) -> int:
        return self.browser_var.get()
