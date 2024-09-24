import logging, os, json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Adicionando opções ao WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-maximized")

# Especificando o caminho do chromedriver usando o Service
chrome_driver = Service("C://webDriver//chromedriver.exe")

# Inicializando o WebDriver com o service e as opções
driver = webdriver.Chrome(service=chrome_driver, options=options)

# Acessando o site
driver.get('https://registro.br/')


#lista de dominos
dominios = ['roboscompython.com.br', 'dominio2.com.br', 'minhaempresa.com.br']

for dominio in dominios:
    #pesquisando no elemento
    pesquisar = driver.find_element(By.ID , 'is-avail-field')

    # limpando a barra de pesquisa
    pesquisar.clear()

    # pesquisa o dominio
    pesquisar.send_keys(dominio)
    # Da o enter
    pesquisar.send_keys(Keys.RETURN)
    time.sleep(2)

    # pega o resultado 
    resultados = driver.find_element(By.XPATH , '/html/body/div/div/main/div/section/div[2]/div/p/span/strong').text
    time.sleep(2)
    print(f"O Dominio : {dominio} esta : {resultados}")
# Aguardando o carregamento da página
time.sleep(2)

# Fechando o WebDriver
driver.close()
