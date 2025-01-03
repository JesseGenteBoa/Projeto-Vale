from selenium import webdriver   
from selenium.webdriver.remote.webelement import WebElement   
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyautogui import press
from time import sleep


class Interagente:

    def __init__(self):
        pass

    def abrir_pagina_web(self, link):
        servico = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=servico)
        self.driver.get(link)
        self.driver.maximize_window()


    def interagir_pagina_web(self, xpath, acao, texto="", limitar_espera=False, limitar_retorno=False):
        aux = 0
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
                if limitar_espera == True:
                    aux+=1
                if limitar_retorno == True:
                    aux+=7.5
                if aux == 15:
                    break


    def inserir_arquivo(self, xpath, xpath_de_espera, arquivo):
        self.interagir_pagina_web(xpath, acao="Escrever", texto=arquivo)
        self.interagir_pagina_web(xpath_de_espera, acao="Esperar", limitar_espera=True)


    def migrar_ao_frame(self, acao, indice=0):
        match acao:
            case "ir":
                self.driver.switch_to.frame(indice)
            case "voltar":
                self.driver.switch_to.default_content()
            case "Aceitar alerta":
                try:
                    WebDriverWait(self.driver, 15).until(EC.alert_is_present())
                    alert = self.driver.switch_to.alert
                    alert.accept()
                    return True
                except:
                    return False


    def interagir_javaScript(self, venctos_convertidos, indice, id):
        date_field = self.driver.find_element(By.ID, id)
        self.driver.execute_script("arguments[0].style.display = 'block';", date_field)
        self.driver.execute_script("""
            arguments[0].value = arguments[1];
            arguments[0].dispatchEvent(new Event('input'));
            arguments[0].dispatchEvent(new Event('change'));
        """, date_field, venctos_convertidos[indice])


    def verificar_instabilidade(self, verificar):
        arquivo1_inserido = self.interagir_pagina_web(xpath="/html/body/main/div/div/div/div/form/div/div/div/div[1]/div/div[2]/div[1]/p/span/a", acao="Retornar elemento", limitar_retorno=True)
        arquivo2_inserido = self.interagir_pagina_web(xpath="/html/body/main/div/div/div/div/form/div/div/div/div[1]/div/div[2]/div[2]/p/span/a", acao="Retornar elemento", limitar_retorno=True)
        arquivo3_inserido = self.interagir_pagina_web(xpath="/html/body/main/div/div/div/div/form/div/div/div/div[1]/div/div[2]/div[3]/p/span/a", acao="Retornar elemento", limitar_retorno=True)
        if verificar == "Um de cada vez":   
            if any(isinstance(elemento, WebElement) for elemento in [arquivo1_inserido, arquivo2_inserido, arquivo3_inserido]):
                return False
            press("f5")
            return True
        elif verificar == "Todos de uma vez":
            if all(isinstance(elemento, WebElement) for elemento in [arquivo1_inserido, arquivo2_inserido, arquivo3_inserido]):
                return False
            press("f5")
            return True


    def fechar_driver(self):
        self.driver.quit()
 
