import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

class Pesquisar:

    def __init__(self, driver, planilha):
        self.driver = driver
        self.planilha = planilha
        self.caminho = os.path.dirname(os.path.abspath(__file__)) # caminho do projeto
        self.arquivo_txt = open(os.path.join(self.caminho, 'resultado.txt'), 'w') # cria o arquivo
    
    def pesquisarDominio(self):

        # Acessando o site
        self.driver.get('https://registro.br/')

        for dominio in range(1,self.planilha.max_row + 1):
            #pesquisando no elemento
            pesquisar = self.driver.find_element(By.ID , 'is-avail-field')

            # limpando a barra de pesquisa
            pesquisar.clear()

            # pesquisa o dominio
            pesquisar.send_keys(self.planilha.cell(row=dominio, column=1).value)
            # Da o enter
            pesquisar.send_keys(Keys.RETURN)
            time.sleep(2)

            # pega o resultado 
            resultados = self.driver.find_element(By.XPATH , '/html/body/div/div/main/div/section/div[2]/div/p/span/strong').text
            time.sleep(2)
        
            # escreve no arquivo
            self.__escreverArquivo(self.__montarRetornoTexto(dominio, resultados))
            
        # Aguardando o carregamento da página
        time.sleep(2)

        #fecha o arquivo
        self.arquivo_txt.close()

    def __montarRetornoTexto(self, dominio, resultados):
        return f"O Dominio : {dominio} esta : {resultados}\n"
    
    def __escreverArquivo(self , texto):
        self.arquivo_txt.write(texto)