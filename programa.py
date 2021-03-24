from tradutor import Tradutor


tradutor = Tradutor()

print('Traduzir')
idioma_origem = str(input('De: ')).capitalize()
idioma_destino = str(input('Para: ')).capitalize()
texto = str(input('Texto: '))

# Traduzindo um texto
traducao = tradutor.traduzir(idioma_origem, idioma_destino, texto)
print(traducao)

print('Detectar')
texto_para_detectar = str(input('Texto: '))

# Detectando Idioma
detector = tradutor.detectar(texto_para_detectar)
print(f'O texto está em {detector}')
