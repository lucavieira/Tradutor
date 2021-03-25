from tkinter import *
from funcoes.tradutor import Tradutor


class Interface:
    def __init__(self, master=None):
        self.fontePadrao = ('Arial', '10')

        self.primeirocontainer = Frame(master)
        self.primeirocontainer['pady'] = 10
        self.primeirocontainer.pack()

        self.segundocontainer = Frame(master)
        self.segundocontainer['padx'] = 20
        self.segundocontainer.pack()

        self.terceirocontainer = Frame(master)
        self.terceirocontainer['pady'] = 10
        self.terceirocontainer.pack()

        self.quartocontainer = Frame(master)
        self.quartocontainer['padx'] = 20
        self.quartocontainer.pack()

        self.quintocontainer = Frame(master)
        self.quintocontainer['pady'] = 10
        self.quintocontainer.pack()

        self.sextocontainer = Frame(master)
        self.sextocontainer['pady'] = 10
        self.sextocontainer.pack()

        self.setimocontainer = Frame(master)
        self.setimocontainer['pady'] = 10
        self.setimocontainer.pack()

        self.oitavocontainer = Frame(master)
        self.oitavocontainer['pady'] = 10
        self.oitavocontainer.pack()

        self.titulo = Label(self.primeirocontainer, text='Tradutor')
        self.titulo['font'] = ('Elephant', '25')
        self.titulo.pack()

        self.botao_traducao = Button(self.segundocontainer)
        self.botao_traducao['text'] = 'Tradução'
        self.botao_traducao['font'] = self.fontePadrao
        self.botao_traducao['width'] = 15
        self.botao_traducao['command'] = self.mostrar_labels_traducao
        self.botao_traducao.pack(side=LEFT)

        self.botao_detectar = Button(self.segundocontainer)
        self.botao_detectar['text'] = 'Detectar'
        self.botao_detectar['font'] = self.fontePadrao
        self.botao_detectar['width'] = 15
        self.botao_detectar['command'] = self.mostrar_labels_deteccao
        self.botao_detectar.pack(side=LEFT)

        # Traduzir
        self.tituloLabel = Label(self.terceirocontainer, text='', font=('Arial', '15', 'bold'))

        self.idioma_origem_label = Label(self.quartocontainer, text='De: ', font=self.fontePadrao)
        self.idioma_origem_campo = Entry(self.quartocontainer, width=20, font=self.fontePadrao)

        self.idioma_destino_label = Label(self.quartocontainer, text='Para: ', font=self.fontePadrao)
        self.idioma_destino_campo = Entry(self.quartocontainer, width=20, font=self.fontePadrao)

        self.texto = Label(self.quintocontainer, text='Texto', font=self.fontePadrao)
        self.campo_texto = Entry(self.quintocontainer, width=40, font=self.fontePadrao)

        self.botao = Button(self.sextocontainer)
        self.botao['text'] = ''
        self.botao['font'] = self.fontePadrao
        self.botao['width'] = 15
        self.botao['command'] = self.traducao

        self.resposta = Label(self.setimocontainer, text='', font=self.fontePadrao)
        self.resposta.pack()

        # Detectar

    def mostrar_labels_traducao(self):
        self.tituloLabel['text'] = 'Traduzir'
        self.tituloLabel.pack()

        self.idioma_origem_label.pack(side=LEFT)
        self.idioma_origem_campo.pack(side=LEFT)

        self.idioma_destino_label.pack(side=LEFT)
        self.idioma_destino_campo.pack(side=LEFT)

        self.texto.pack()
        self.campo_texto.pack()

        self.botao['text'] = 'Traduzir'
        self.botao.pack()

    def mostrar_labels_deteccao(self):
        self.tituloLabel['text'] = 'Detectar'
        self.tituloLabel.pack()

        self.idioma_origem_label.pack_forget()
        self.idioma_origem_campo.pack_forget()

        self.idioma_destino_label.pack_forget()
        self.idioma_destino_campo.pack_forget()

        self.texto.pack()
        self.campo_texto.pack()

        self.botao['text'] = 'Detectar'
        self.botao['command'] = self.detectar
        self.botao.pack()

    def traducao(self):
        tradutor = Tradutor()
        idioma_origem = str(self.idioma_origem_campo.get())
        idioma_destino = str(self.idioma_destino_campo.get())
        texto = str(self.campo_texto.get())
        traducao = tradutor.traduzir(idioma_origem, idioma_destino, texto)
        self.resposta['text'] = f'Tradução: {traducao}'

    def detectar(self):
        tradutor = Tradutor()
        texto = str(self.campo_texto.get())
        detectado = tradutor.detectar(texto)
        self.resposta['text'] = f'O texto está em {detectado}'
