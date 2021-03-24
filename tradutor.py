from selenium import webdriver
from time import sleep


class Tradutor:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.chrome = webdriver.Chrome(executable_path=r"C:\Users\User\Documents\chrome_driver\chromedriver.exe", options=options)

    def traduzir(self, idioma_origem='pt', idioma_destino='en', texto_original=''):
        self.url_tradutora = f'https://translate.google.com.br/?hl=pt-BR&sl={idioma_origem}&tl={idioma_destino}&text={texto_original}&op=translate'
        sleep(2)
        self.chrome.get(self.url_tradutora)
        sleep(2)
        try:
            traducao = self.chrome.find_element_by_xpath('//span[@jsname="W297wb"]')
        except:
            return 'Teste'
        else:
            sleep(2)
            return f'Texto em {idioma_origem} > {texto_original}\n' \
                   f'Texto em {idioma_destino} > {traducao.text}'

    def detectar(self, idioma_destino='pt', texto=''):
        sleep(2)
        self.url_tradutora = f'https://translate.google.com.br/?hl=pt-BR&sl=auto&tl={idioma_destino}&text={texto}&op=translate'
        sleep(2)
        self.chrome.get(self.url_tradutora)
        sleep(2)
        idioma_detectado = self.chrome.find_element_by_xpath('//span[@class="VfPpkd-jY41G-V67aGc"]')
        sleep(1)
        return idioma_detectado.text


traducao = Tradutor()
print(traducao.traduzir('pt', 'ja', 'Obrigado'))
print(traducao.detectar(texto='ありがとう '))
