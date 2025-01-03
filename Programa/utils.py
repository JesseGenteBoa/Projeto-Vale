import xmltodict
from time import sleep
import os
import shutil


def criar_pasta(pasta):
    try:
        os.mkdir(pasta)
    except FileExistsError:
        shutil.rmtree(pasta)
        os.mkdir(pasta)
    except PermissionError:
        return PermissionError
    return pasta


def ler_xml(arquivo):
    try:
        with open(arquivo) as fd:
            doc = xmltodict.parse(fd.read())
    except UnicodeDecodeError:
        with open(arquivo, encoding='utf-8') as fd:
            doc = xmltodict.parse(fd.read())
    except:
        with open(arquivo, encoding='utf-8') as fd:
            doc = xmltodict.parse(fd.read(), attr_prefix="@", cdata_key="#text")
    return doc


def retornar_caminho(diretorio_processo, arquivo, extensao=".pdf"):
    caminho_arquivo = str(diretorio_processo) + "\\" + arquivo + extensao
    return caminho_arquivo


def extrair_dados(conjunto_xml):
    numero_nf = conjunto_xml["Nfse"]["InfNfse"]["Numero"]
    observacoes_nfs = conjunto_xml["Nfse"]["InfNfse"]["DeclaracaoPrestacaoServico"]["InfDeclaracaoPrestacaoServico"]["Servico"]["Discriminacao"]
    rf = observacoes_nfs[observacoes_nfs.find("RF: N")+6:].strip()
    cc = observacoes_nfs[observacoes_nfs.find("CC: ")+4:observacoes_nfs.find(" - Tipo:")].strip()
    vencto = observacoes_nfs[observacoes_nfs.find("Venctos:")+9:observacoes_nfs.find(" / ")].strip()
    return numero_nf, rf, cc, vencto


def zerar_lista_controle(lista_controle):
    sleep(2)
    while not lista_controle.empty():
        lista_controle.get()
        lista_controle.task_done()
 
