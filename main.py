from navegador import *
from planilha import *
from pesquisar import *

def main():
    print("Projeto iniciado...")

    # ler o arquivo
    planilha = Planilha().lerPlanilha()

    # instancia o navegador
    driver = Navegador().abrir()

    # realiza a pesquisa
    Pesquisar(driver, planilha).pesquisarDominio()

    # fecha o navegador
    Navegador(driver).fechar()

    print("Projeto finalizado...")

if __name__ == '__main__':
    main()