from tkinter import filedialog as dlg
from models.data_handler import DataHandler
from models.scraper import SefazScraper

class MainController:
    def __init__(self):
        self.view = None
        self.codes = []

    def set_view(self, view):
        self.view = view

    def handle_import(self):
        try:
            arquivo = dlg.askopenfilename(filetypes=[("Planilha", "*.xlsx")])
            if not arquivo:
                return
                
            self.codes = DataHandler.import_excel(arquivo)
            self.view.update_status("Importado com sucesso!")
        except FileNotFoundError as e:
            if not self.codes:
                self.view.update_status("Não foi possivel importar\nTente novamente.", is_error=True)

    def handle_search(self):
        if not self.codes:
            self.view.update_status("Primeiro importe os CNPJs.", is_error=True)
            return

        cidades = self.view.get_selected_cities()
        if not cidades:
            self.view.update_status("Selecione pelo menos uma cidade.", is_error=True)
            return

        search_type = self.view.get_search_type()
        browser_choice = self.view.get_browser_choice()

        # Update UI to waiting state
        self.view.status_label.configure(text="Aguarde...", foreground="#cccc10")
        self.view.update_idletasks()

        # Run Scraper
        scraper = SefazScraper(browser_choice=browser_choice)
        scores = scraper.execute_search(self.codes, cidades, search_type)

        if not scores:
            self.view.update_status("Nenhuma empresa encontrada nos locais selecionados.", is_error=True)
            return

        # Save File
        save_path = dlg.asksaveasfilename(filetypes=[("Arquivo Excel", "*.xlsx")])
        if save_path:
            success = DataHandler.export_excel(save_path, scores)
            if success:
                self.view.update_status("Concluído!")
            else:
                self.view.update_status("Erro ao salvar o arquivo.", is_error=True)
        else:
            self.view.update_status("O arquivo não foi salvo.", is_error=True)
