import openpyxl

class Planilha:
    
    def __init__(self) -> None:
        self.arquivo = openpyxl.load_workbook('C://Users//ricar//OneDrive//Documentos//Projetos//Projetos em Python//pesquisa_dominio//dominio.xlsx')

    def lerPlanilha(self):
        return self.arquivo.worksheets[0]