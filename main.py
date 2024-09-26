import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from navegador import *
from planilha import *

# Obtém o diretório atual
caminho = os.path.dirname(os.path.abspath(__file__))

#cria o arquivo
arquivo_txt = open(os.path.join(caminho, 'resultado.txt'), 'w')

# ler o arquivo
sheet = Planilha().lerPlanilha()

# instancia o navegador
driver = Navegador().abrir()

# Acessando o site
driver.get('https://registro.br/')

for dominio in range(1,sheet.max_row + 1):
    #pesquisando no elemento
    pesquisar = driver.find_element(By.ID , 'is-avail-field')

    # limpando a barra de pesquisa
    pesquisar.clear()

    # pesquisa o dominio
    pesquisar.send_keys(sheet.cell(row=dominio, column=1).value)
    # Da o enter
    pesquisar.send_keys(Keys.RETURN)
    time.sleep(2)

    # pega o resultado 
    resultados = driver.find_element(By.XPATH , '/html/body/div/div/main/div/section/div[2]/div/p/span/strong').text
    time.sleep(2)
    #print(f"O Dominio : {dominio} esta : {resultados}")
    texto = f"O Dominio : {dominio} esta : {resultados}\n"
    arquivo_txt.write(texto)
# Aguardando o carregamento da página
time.sleep(2)

#fecha o arquivo
arquivo_txt.close()
# fecha o navegador
Navegador(driver).fechar()
