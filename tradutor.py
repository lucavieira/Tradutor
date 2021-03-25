from selenium import webdriver
from time import sleep
import csv


class Tradutor:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.chrome = webdriver.Chrome(executable_path=r"C:\Users\User\Documents\chrome_driver\chromedriver.exe", options=options)

    def traduzir(self, idioma_origem='pt', idioma_destino='en', texto_original=''):
        idiomas = self.localizar_idiomas(idioma_origem, idioma_destino)
        sleep(1.5)
        self.url_tradutora = f'https://translate.google.com.br/?hl=pt-BR&sl={idiomas[0]}&tl={idiomas[1]}&text={texto_original}&op=translate'
        sleep(2)
        self.chrome.get(self.url_tradutora)
        sleep(2)
        try:
            traducao = self.chrome.find_element_by_xpath('//span[@jsname="W297wb"]')
        except:
            return 'erro'
        else:
            sleep(2)
            return traducao.text

    def detectar(self, texto=''):
        sleep(2)
        self.url_tradutora = f'https://translate.google.com.br/?hl=pt-BR&tab=TT&sl=auto&tl=pt&text={texto}&op=translate'
        sleep(2)
        self.chrome.get(self.url_tradutora)
        sleep(2)
        idioma_detectado = self.chrome.find_element_by_xpath('//span[@class="VfPpkd-jY41G-V67aGc"]')
        sleep(1)
        return idioma_detectado.text

    def idiomas(self):
        with open('idiomas.csv') as idiomas:
            return [idioma for idioma in csv.DictReader(idiomas)]

    def localizar_idiomas(self, idioma_origem, idioma_destino):
        lista_idiomas = self.idiomas()
        for idioma in lista_idiomas:
            if idioma['Idioma'] == idioma_origem:
                abreviacao_origem = idioma['Abreviacao']
            if idioma['Idioma'] == idioma_destino:
                abreviacao_destino = idioma['Abreviacao']
        return abreviacao_origem, abreviacao_destino



#print(traducao.localizar_idiomas('Bielorusso', 'Inglês'))
#print(traducao.traduzir('Português', 'Inglês', 'Obrigado'))
#print(traducao.detectar(texto='ありがとう '))
