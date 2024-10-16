from selenium import webdriver      
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class Interagente:

    def __init__(self):
        pass

    def abrir_pagina_web(self, link):
        servico = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=servico)
        self.driver.get(link)
        self.driver.maximize_window()


    def interagir_pagina_web(self, xpath, acao, texto=""):
        while True:
            try:
                elemento = self.driver.find_element(By.XPATH, xpath)
                match acao:
                    case "Clicar":
                        elemento.click()
                    case "Escrever":
                        elemento.clear()
                        sleep(0.8)
                        elemento.send_keys(texto)
                    case "Retornar elemento":
                        return elemento
                    case "Esperar":
                        pass
                break
            except:
                sleep(1)


    def inserir_arquivos(self, xpath, xpath_de_espera, arquivo):
        self.interagir_pagina_web(xpath, acao="Escrever", texto=arquivo)
        self.interagir_pagina_web(xpath_de_espera, acao="Esperar")


    def migrar_ao_frame(self, acao, indice=0):
        match acao:
            case "ir":
                self.driver.switch_to.frame(indice)
            case "voltar":
                self.driver.switch_to.default_content()
            case "Aceitar alerta":
                WebDriverWait(self.driver, 15).until(EC.alert_is_present())
                alert = self.driver.switch_to.alert
                alert.accept()


    def interagir_javaScript(self, venctos_convertidos, indice, id):
        date_field = self.driver.find_element(By.ID, id)
        self.driver.execute_script("arguments[0].style.display = 'block';", date_field)
        self.driver.execute_script("""
            arguments[0].value = arguments[1];
            arguments[0].dispatchEvent(new Event('input'));
            arguments[0].dispatchEvent(new Event('change'));
        """, date_field, venctos_convertidos[indice])


    def fechar_driver(self):
        self.driver.quit()


