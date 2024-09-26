from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Navegador:
   
    def __init__(self, driver=None) -> None:
        self.driver = driver

    def abrir(self):
        # Especificando o caminho do chromedriver usando o Service
        chrome_driver = Service("C://webDriver//chromedriver.exe")
        # Inicializando o WebDriver com o service e as opções
        self.driver = webdriver.Chrome(service=chrome_driver, options=self.__opcoesChrome())
        self.driver.implicitly_wait(14)
        
        return self.driver

    def fechar(self):
        # Fechando o WebDriver
        self.driver.close()
        
    def __opcoesChrome(self):   
        options=Options()
        # Adicionando opções ao WebDriver
        options.add_argument("--no-sandbox")    
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--start-maximized")

        return options