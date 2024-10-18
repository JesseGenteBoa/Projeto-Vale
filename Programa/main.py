from selenium.webdriver.remote.webelement import WebElement
from datetime import datetime
from pyautogui import hotkey, press
from pyperclip import paste, copy
from time import sleep
from pathlib import Path
from pypdf import PdfReader, PdfWriter
import pandas as pd
import atuadorWeb
import xmltodict
import os
import shutil
import utils



def executar_automacao(nf_inicial, nf_final, pasta_rf, caminho_arq_excel):

    interagente = atuadorWeb.Interagente()

    
    interagente.abrir_pagina_web("https://tributacao.serra.es.gov.br:8080/tbserra/loginCNPJContribuinte.jsp#")
    
    
    interagente.interagir_pagina_web(xpath='/html/body/div/div[1]/div/form/div/div[3]/input', acao="Escrever", texto="***********")
    
    interagente.interagir_pagina_web(xpath='/html/body/div/div[1]/div/form/div/div[5]/input', acao="Escrever", texto="***********")
    press("tab")
    
    
    interagente.interagir_pagina_web(xpath='/html/body/div[2]/div/form/section[2]/div/div/div[2]/div[2]/div/div', acao="Clicar")
    
    pasta = utils.criar_pasta(pasta="NFS")
    
    
    interagente.interagir_pagina_web(xpath='/html/body/div[2]/div/form/section[2]/div/div/div[3]/div[2]/button', acao="Clicar")
    
    interagente.interagir_pagina_web(xpath='/html/body/div[2]/div/form/section[2]/div/div/div[3]/div[2]/div', acao="Clicar")
    
    interagente.interagir_pagina_web(xpath='/html/body/div[2]/div/form/section[2]/div/div/div[2]/div/div[1]/div[3]/div[1]/div/button[2]', acao="Clicar")
    
    interagente.interagir_pagina_web(xpath='/html/body/div[2]/div/form/section[2]/div/div/div[2]/div/div[1]/div[3]/div[1]/div/ul/li[8]', acao="Clicar")
    
    
    interagente.migrar_ao_frame(acao="ir")
    interagente.migrar_ao_frame(acao="ir", indice=1)
    
    
    interagente.interagir_pagina_web(xpath='/html/body/form/div/div/div[1]/div/div[2]/div/div[1]/div[1]/label', acao="Esperar")

    interagente.interagir_pagina_web(xpath='/html/body/form/div/div/div[1]/div/div[3]/div[2]/div/label/input', acao="Escrever", texto="300")

    interagente.interagir_pagina_web(xpath='/html/body/form/div/div/div[1]/div/div[2]/ul/li[2]/a', acao="Clicar")

    interagente.interagir_pagina_web(xpath='/html/body/form/div/div/div[1]/div/div[2]/div/div[2]/input[1]', acao="Escrever", texto=nf_inicial)

    interagente.interagir_pagina_web(xpath='/html/body/form/div/div/div[1]/div/div[2]/div/div[2]/input[2]', acao="Escrever", texto=nf_final)

    interagente.interagir_pagina_web(xpath='/html/body/form/div/div/div[2]/button[3]', acao="Clicar")
    
    
    interagente.migrar_ao_frame(acao="voltar")
    interagente.migrar_ao_frame(acao="voltar")
    
    sleep(2)
    
    
    interagente.interagir_pagina_web(xpath='/html/body/div[2]/div/form/section[2]/div/div/div[2]/div/div[1]/div[4]/div[1]/table/thead/tr/th[1]/input', acao="Clicar")
    
    interagente.interagir_pagina_web(xpath='/html/body/div[2]/div/form/section[2]/div/div/div[2]/div/div[1]/div[2]/button[1]', acao="Clicar")
    
    sleep(1)
    
    aux = 0
    while True:
        hotkey('alt', 'd', interval=0.3)
        hotkey('ctrl', 'c')
        endereco_de_pesquisa = paste()
        if 'serra' in endereco_de_pesquisa:
            sleep(1.5)
            break
        if aux == 12:
            hotkey('ctrl', 'w', interval=1)
            interagente.interagir_pagina_web(xpath='/html/body/div[2]/div/form/section[2]/div/div/div[2]/div/div[1]/div[2]/button[1]', acao="Clicar")
            sleep(1)
            aux = 0
        aux+=1
        sleep(1)
    
    hotkey('ctrl', 's')
    sleep(3)
    
    pasta = "NFS"
    caminho_absoluto = str(Path(pasta).resolve())
    arquivo_nfs = caminho_absoluto + "\\PDF_NFS.pdf"
    copy(arquivo_nfs)
    hotkey('ctrl', 'v', interval=0.5)
    press("tab", interval=0.5)
    hotkey('alt', 'l', interval=1)
    hotkey('ctrl', 'w', interval=0.5)
    
    
    numeracao_nf = int(nf_inicial)
    
    with open(arquivo_nfs, 'rb') as file:
        pdf = PdfReader(file)
        
        for pagina in range(len(pdf.pages)):
    
            criar_pdf = PdfWriter()
            criar_pdf.add_page(pdf.pages[pagina])
            nfs = caminho_absoluto + f'\\NFS {numeracao_nf}.pdf'
    
            with open(nfs, 'wb') as new_file:
                criar_pdf.write(new_file)
              
            numeracao_nf+=1
    
    
    os.remove(arquivo_nfs)
    
    interagente.interagir_pagina_web(xpath='/html/body/div[2]/div/form/section[2]/div/div/div[2]/div/div[1]/div[2]/button[6]', acao="Clicar")
    
    interagente.interagir_pagina_web(xpath='/html/body/div[2]/div/form/div[10]/div/div/div[2]/div/div/div/button', acao="Clicar")
    
    
    sleep(7)
    hotkey('ctrl', 'j', interval=0.5)
    sleep(1)
    
    press(["tab"]*3)
    press("enter", interval=0.3)
    press("down")
    press("enter", interval=0.8)
    press("tab")
    press("enter", interval=3)
    press("f2", interval=0.5)
    hotkey('ctrl', 'c', interval=0.5)
    
    nome_do_arquivo = paste()
    nome_do_arquivo = nome_do_arquivo + ".xml"
    
    press("esc")
    hotkey('ctrl', 'w', interval=0.5)
    interagente.fechar_driver()
    
    pasta_downloads = Path(os.path.join(Path.home(), "Downloads"))
    caminho_completo = pasta_downloads / nome_do_arquivo
    caminho_original = str(caminho_completo.resolve())
    
    pasta = utils.criar_pasta(pasta="XML")
    
    diretorio_destino = Path(pasta).resolve()
    novo_caminho = diretorio_destino / nome_do_arquivo
    shutil.move(caminho_original, novo_caminho)
    
    
    dict_venctos = {}
    dict_cc = {}
    nfs_canceladas = []
    lista_cc = []
    venctos = []
    
    xml = utils.ler_xml(novo_caminho)
    conjunto_xmls = xml["ConsultarNfseServicoPrestadoResposta"]["ListaNfse"]["CompNfse"]
    
    
    if len(conjunto_xmls) > 1:
        for xml in conjunto_xmls:
            
            numero_nf, rf, cc, vencto = utils.extrair_dados(xml)
            nome_do_arquivo = "NFS " + numero_nf + " - RF " + rf
            caminho_xml = "XML\\" + nome_do_arquivo + ".xml"
            dict_venctos[numero_nf] = vencto
            dict_venctos = dict(sorted(dict_venctos.items()))
            dict_cc[numero_nf] = cc
            dict_cc = dict(sorted(dict_cc.items()))
    
            xml_completo = {
                "ConsultarNfseServicoPrestadoResposta" : {
                    "@xmlns" : "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd", "ListaNfse" : {
                        "CompNfse" : xml
                    }
                }
            }
    
            with open(caminho_xml, 'w', encoding='utf-8') as arquivo_xml:
                nfs = xmltodict.unparse(xml_completo, pretty=True)
                if "NfseCancelamento" in nfs:
                    nfs_canceladas.append("NFS " + numero_nf)
                    del dict_venctos[numero_nf]
                    del dict_cc[numero_nf]
                else:
                    arquivo_xml.write(nfs)
            
        os.remove(novo_caminho)
        venctos = list(dict_venctos.values())
        lista_cc = list(dict_cc.values())
    
    else:
        numero_nf, rf, cc, vencto = utils.extrair_dados(conjunto_xmls)
        nome_do_arquivo = str(diretorio_destino) + "\\NFS " + numero_nf + " - RF " + rf + ".xml"
        nome_antigo = novo_caminho
        os.rename(nome_antigo, nome_do_arquivo)
        lista_cc.append(cc)
        venctos.append(vencto)
    
    
    venctos_convertidos = [datetime.strptime(data, "%d/%m/%y").strftime("%Y-%m-%d") for data in venctos]


    pasta = utils.criar_pasta(pasta="Processos")
    
    pdf_arquivos = sorted([arquivo for arquivo in os.listdir("NFS")])
    xml_arquivos = sorted([arquivo for arquivo in os.listdir("XML")])
    lista_rf = [arquivo[arquivo.find("RF")+3:-4] + ".pdf" for arquivo in xml_arquivos]
    
    
    for pdf_arquivo, xml_arquivo, rf_arquivo in zip(pdf_arquivos, xml_arquivos, lista_rf):
    
        numero_nfs = os.path.splitext(pdf_arquivo)[0]
        nome_pasta = os.path.splitext(xml_arquivo)[0]
    
        if numero_nfs not in nfs_canceladas:
            pasta_processo = "Processos\\" + nome_pasta
            pasta = utils.criar_pasta(pasta_processo)
    
            pdf_caminho = "NFS\\" + pdf_arquivo
            xml_caminho = "XML\\" + xml_arquivo
            rf_caminho = pasta_rf + "\\" + rf_arquivo
    
            shutil.copy(pdf_caminho, pasta_processo)
            shutil.copy(xml_caminho, pasta_processo)
            shutil.copy(rf_caminho, pasta_processo)
    
    
    df = pd.read_excel(caminho_arq_excel)
    lista_de_cc = df.iloc[4:, 1].tolist()
    lista_de_email = df.iloc[4:, 2].tolist()
    dicionario_de_emails = dict(zip(lista_de_cc, lista_de_email))
    
    
    
    interagente.abrir_pagina_web("https://vale.virtual360.io/users/sign_in")
    
    
    interagente.interagir_pagina_web(xpath='/html/body/div[1]/div[2]/div/div/div/a[1]', acao="Clicar")
    
    interagente.interagir_pagina_web(xpath='/html/body/div[1]/div[2]/div/div/form/div[2]/div/div/div/input', acao="Escrever", texto="**********")
    
    interagente.interagir_pagina_web(xpath='/html/body/div[1]/div[2]/div/div/form/div[3]/div/div/div/input', acao="Escrever", texto="**********")
    
    interagente.interagir_pagina_web(xpath='/html/body/div[1]/div[2]/div/div/form/input[3]', acao="Clicar")
    
    
    
    for i, pasta in enumerate(os.listdir("Processos")):
    
        interagente.interagir_pagina_web(xpath='/html/body/header/nav[2]/ul/li[5]/a', acao="Clicar")
        
        interagente.interagir_pagina_web(xpath='/html/body/header/nav[2]/ul/li[5]/div/a[1]/span', acao="Clicar")
        
    
        diretorio_processo = Path("Processos").resolve() / pasta
    
        caminho_pdf_nfs = utils.retornar_caminho(diretorio_processo, pasta[pasta.find("NFS"):pasta.find(" - RF")])
        caminho_pdf_rf = utils.retornar_caminho(diretorio_processo, pasta[pasta.find(" - RF")+6:])
        caminho_xml = utils.retornar_caminho(diretorio_processo, pasta, extensao=".xml")
    
    
        while True:
            interagente.inserir_arquivos(xpath='/html/body/main/div/div/div/div/form/div/div/div/div[1]/div/div[2]/div[1]/input', xpath_de_espera="/html/body/main/div/div/div/div/form/div/div/div/div[1]/div/div[2]/div[1]/p/span/a", arquivo=caminho_xml)
    
            interagente.inserir_arquivos(xpath='/html/body/main/div/div/div/div/form/div/div/div/div[1]/div/div[2]/div[2]/input', xpath_de_espera="/html/body/main/div/div/div/div/form/div/div/div/div[1]/div/div[2]/div[2]/p/span/a", arquivo=caminho_pdf_nfs)
    
            interagente.inserir_arquivos(xpath='/html/body/main/div/div/div/div/form/div/div/div/div[1]/div/div[2]/div[3]/input', xpath_de_espera="/html/body/main/div/div/div/div/form/div/div/div/div[1]/div/div[2]/div[3]/p/span/a", arquivo=caminho_pdf_rf)
            
            arquivo1_inserido = interagente.interagir_pagina_web(xpath="/html/body/main/div/div/div/div/form/div/div/div/div[1]/div/div[2]/div[1]/p/span/a", acao="Retornar elemento")
            arquivo2_inserido = interagente.interagir_pagina_web(xpath="/html/body/main/div/div/div/div/form/div/div/div/div[1]/div/div[2]/div[2]/p/span/a", acao="Retornar elemento")
            arquivo3_inserido = interagente.interagir_pagina_web(xpath="/html/body/main/div/div/div/div/form/div/div/div/div[1]/div/div[2]/div[3]/p/span/a", acao="Retornar elemento")
            if all(isinstance(elemento, WebElement) for elemento in [arquivo1_inserido, arquivo2_inserido, arquivo3_inserido]):
                break
            else:
                press("f5")
                sleep(3)
    
    
        interagente.interagir_pagina_web(xpath='/html/body/main/div/div/div/div/form/div/div/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/input', acao="Escrever", texto=dicionario_de_emails[lista_cc[i]])
    
        interagente.interagir_javaScript(venctos_convertidos, i, id= 'tax_document_net_due_date')
    
        interagente.interagir_pagina_web(xpath='/html/body/main/div/div/div/div/form/div/div/div/div[1]/div/div[7]/div/div/div[2]/div/div/div/div/div[2]/span/span[1]/span', acao="Clicar")
    
    
        pdf = PdfReader(caminho_pdf_rf)
    
        pag = pdf.pages[0]
        texto = pag.extract_text()
    
        informacao_bruta = texto[texto.find("(Cod. Município/Descrição Município/Estado)")+57:]
    
        informacao_bruta = informacao_bruta.replace('\n', ' ').strip()
        partes = informacao_bruta.split(' / ')
        cidade = partes[0].strip()
        estado = partes[1].strip()
    
        municipio_prest_serv = f"{estado}, {cidade}"
        interagente.interagir_pagina_web(xpath='/html/body/span/span/span[1]/input', acao="Escrever", texto=municipio_prest_serv)
        sleep(3)
        press("enter", interval=1)
    
    
        elemento_municipio = interagente.interagir_pagina_web(xpath='/html/body/main/div/div/div/div/form/div/div/div/div[1]/div/div[7]/div/div/div[2]/div/div/div/div/div[2]/span/span[1]/span/span[1]', acao="Retornar elemento")
        municipio_no_campo = elemento_municipio.get_attribute('title')
        while municipio_no_campo != cidade:
            elemento_municipio = interagente.interagir_pagina_web(xpath='/html/body/main/div/div/div/div/form/div/div/div/div[1]/div/div[7]/div/div/div[2]/div/div/div/div/div[2]/span/span[1]/span/span[1]', acao="Retornar elemento")
            municipio_no_campo = elemento_municipio.get_attribute('title')
            sleep(1)
            
    
        interagente.interagir_pagina_web(xpath='/html/body/main/div/div/div/div/form/div/div/div/div[2]/div/div/button', acao="Clicar")
    
        interagente.migrar_ao_frame(acao="Aceitar alerta")
    
        interagente.interagir_pagina_web(xpath='/html/body/main/div/div[4]/div/div/div[1]/div[1]/ul/li[1]/a', acao="Esperar")
    
        
    sleep(10)
    
    
