import json

class DicionarioModel:
    def __init__(self, arquivo='dicionario.json'):
        self.arquivo = arquivo
        self.dicionario = self.carregar_dicionario()