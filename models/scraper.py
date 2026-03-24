from selenium import webdriver
from selenium.webdriver.common.by import By

class SefazScraper:
    def __init__(self, browser_choice: int):
        """
        Initializes the WebDriver based on browser_choice.
        0: Firefox
        1: Chrome
        """
        self.browser_choice = browser_choice
        self.navegador = None

    def _start_browser(self):
        if self.browser_choice == 0:
            self.navegador = webdriver.Firefox()
        else:
            self.navegador = webdriver.Chrome()
        self.navegador.minimize_window()

    def _close_browser(self):
        if self.navegador:
            self.navegador.quit()
            self.navegador = None

    def execute_search(self, codes: list, cidades: list, tipodebusca: int) -> list:
        """
        Executes the search for the given codes and cities.
        tipodebusca: 0 == RaizCNPJ, 1 == CACEAL, 2 == CNPJ
        """
        result = list()
        
        try:
            self._start_browser()
            
            for text in codes:
                match tipodebusca:
                    case 0:
                        for cidade in cidades:
                            resultado = self.searchRaizCNPJ(text)
                            if cidade == resultado[2]:
                                result.append(resultado)
                    case 1:
                        for cidade in cidades:
                            resultado = self.searchCACEAL(text)
                            if cidade == resultado[2]:
                                result.append(resultado)
                    case 2:
                        for cidade in cidades:
                            resultado = self.searchCNPJ(text)
                            if cidade == resultado[2]:
                                result.append(resultado)
            
        except Exception as e:
            print(f"Error during scraping: {e}")
        finally:
            self._close_browser()
            
        return result

    def searchRaizCNPJ(self, text):
        nome, rasaosocial, local, contato1 = "Nome", "Razão social", "Cidade", "Email"
        try:
            self.navegador.get(
                f'https://cadsinc.sefaz.al.gov.br/VisualizarDadosContribuinte.do?opcao=raizcnpj&valor={str(text).zfill(8)}')
            self.navegador.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr/td[6]/a').click()
            try:
                nome = self.navegador.find_element(By.XPATH,
                                                   '/html/body/table[3]/tbody/tr/td/fieldset[1]/table[1]/tbody/tr[4]/td/b').text
            except:
                pass
            try:
                rasaosocial = self.navegador.find_element(By.XPATH,
                                                          '/html/body/table[3]/tbody/tr/td/fieldset[1]/table[1]/tbody/tr[6]/td').text
            except:
                pass
            try:
                local = self.navegador.find_element(By.XPATH,
                                                    '/html/body/table[3]/tbody/tr/td/fieldset[2]/table[2]/tbody/tr[2]/td[3]').text
            except:
                pass
            try:
                contato1 = self.navegador.find_element(By.XPATH,
                                                       '/html/body/table[3]/tbody/tr/td/fieldset[2]/table[3]/tbody/tr[2]/td[3]').text
            except:
                pass
        except:
            pass
        return [nome, rasaosocial, local, contato1, text]

    def searchCACEAL(self, text):
        nome, rasaosocial, local, contato1 = "Nome", "Razão social", "Cidade", "Contato"
        try:
            self.navegador.get(f'http://cadsinc.sefaz.al.gov.br/VisualizarDadosContribuinte.do?opcao=caceal&valor={text}')
            try:
                nome = self.navegador.find_element(By.XPATH, '/html/body/table[3]/tbody/tr/td/fieldset[1]/table[1]/tbody/tr[4]/td/b').text
            except:
                pass
            try:
                rasaosocial = self.navegador.find_element(By.XPATH, '/html/body/table[3]/tbody/tr/td/fieldset[1]/table[1]/tbody/tr[6]/td').text
            except:
                pass
            try:
                local = self.navegador.find_element(By.XPATH, '/html/body/table[3]/tbody/tr/td/fieldset[2]/table[2]/tbody/tr[2]/td[3]').text
            except:
                pass
            try:
                contato1 = self.navegador.find_element(By.XPATH, '/html/body/table[3]/tbody/tr/td/fieldset[2]/table[3]/tbody/tr[2]/td[3]').text
            except:
                pass
        except:
            pass
        return [nome, rasaosocial, local, contato1, text]

    def searchCNPJ(self, text):
        nome, rasaosocial, local, contato1 = "Nome", "Razão social", "Cidade", "Email"
        try:
            self.navegador.get(
                f'https://cadsinc.sefaz.al.gov.br/VisualizarDadosContribuinte.do?opcao=cnpj&valor={str(text).replace(".0", "").zfill(14)}')
            self.navegador.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr/td[6]/a').click()
            try:
                nome = self.navegador.find_element(By.XPATH,
                                                   '/html/body/table[3]/tbody/tr/td/fieldset[1]/table[1]/tbody/tr[4]/td/b').text
            except:
                pass
            try:
                rasaosocial = self.navegador.find_element(By.XPATH,
                                                          '/html/body/table[3]/tbody/tr/td/fieldset[1]/table[1]/tbody/tr[6]/td').text
            except:
                pass
            try:
                local = self.navegador.find_element(By.XPATH,
                                                    '/html/body/table[3]/tbody/tr/td/fieldset[2]/table[2]/tbody/tr[2]/td[3]').text
            except:
                pass
            try:
                contato1 = self.navegador.find_element(By.XPATH,
                                                       '/html/body/table[3]/tbody/tr/td/fieldset[2]/table[3]/tbody/tr[2]/td[3]').text
            except:
                pass
        except:
            pass
        return [nome, rasaosocial, local, contato1, text]
