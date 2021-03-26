from selenium import webdriver
from translate import Translator
from time import sleep
import csv


class Tradutor:
    def traduzir(self, idioma_origem='pt', idioma_destino='en', texto_original=''):
        idiomas = self.localizar_idiomas(idioma_origem, idioma_destino)
        tradutor = Translator(to_lang=idiomas[1], from_lang=idiomas[0])
        try:
            traducao = tradutor.translate(texto_original)
        except:
            return ''
        else:
            return traducao

    def detectar(self, texto=''):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.chrome = webdriver.Chrome(executable_path=r"C:\Users\User\Documents\chrome_driver\chromedriver.exe", options=options)
        self.url_tradutora = f'https://translate.google.com.br/?hl=pt-BR&tab=TT&sl=auto&tl=pt&text={texto}&op=translate'
        self.chrome.get(self.url_tradutora)
        sleep(1)
        idioma_detectado = self.chrome.find_element_by_xpath('//span[@class="VfPpkd-jY41G-V67aGc"]')
        return idioma_detectado.text

    def idiomas(self):
        arquivo_idiomas = 'C:/Users/User/PycharmProjects/Tradutor/idiomas.csv'
        with open(arquivo_idiomas, encoding='utf-8') as idiomas:
            return [idioma for idioma in csv.DictReader(idiomas)]

    def localizar_idiomas(self, idioma_origem, idioma_destino):
        lista_idiomas = self.idiomas()
        for idioma in lista_idiomas:
            if idioma['Idioma'] == idioma_origem:
                abreviacao_origem = idioma['Abreviacao']
            if idioma['Idioma'] == idioma_destino:
                abreviacao_destino = idioma['Abreviacao']
        return abreviacao_origem, abreviacao_destino
