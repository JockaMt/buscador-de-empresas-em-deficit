import pandas as pd
import xlsxwriter

class DataHandler:
    @staticmethod
    def import_excel(filepath: str) -> list:
        """
        Reads the first column from an Excel file without headers.
        Returns a list of values (e.g., CNPJs/Codes).
        """
        try:
            src = pd.read_excel(filepath, header=None)
            lista = [i for i in src[0]]
            return lista
        except Exception as e:
            raise FileNotFoundError(f"Failed to read file: {e}")

    @staticmethod
    def export_excel(filepath: str, scores: list) -> bool:
        """
        Exports the scraping results to an Excel file.
        scores format: list of [Nome, Razão social, Cidade, Contato/Email, Code]
        """
        try:
            # Ensure filepath ends with .xlsx
            if not filepath.endswith(".xlsx"):
                filepath += ".xlsx"
                
            workbook = xlsxwriter.Workbook(filepath)
            worksheet = workbook.add_worksheet("Empresas")
            
            formatado = workbook.add_format()
            formatado.set_align("center")
            worksheet.set_column(2, 4, 25, formatado)
            worksheet.set_column(0, 1, 35)
            
            row = 0
            col = 0
            for pessoa, empresa, local, email, text in scores:
                worksheet.write(row, col, text)
                worksheet.write(row, col + 1, pessoa)
                worksheet.write(row, col + 2, empresa)
                worksheet.write(row, col + 3, local)
                worksheet.write(row, col + 4, email)
                row += 1
                
            workbook.close()
            return True
        except Exception as e:
            print(f"Error saving to Excel: {e}")
            return False
