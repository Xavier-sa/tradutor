import json

class DicionarioModel:
    def __init__(self, arquivo='dicionario.json'):
        self.arquivo = arquivo
        self.dicionario = self.carregar_dicionario()
        
    def carregar_dicionario(self):
        #Carrega o dicionario do arquivo JSON
        try:
            with open(self.arquivo,'r',encoding='utf-8') as arquivo:
                return json.load(arquivo)
            
        except FileNotFoundError:
            return{}
        