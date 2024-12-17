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
        
    def salvar_dicionario(self):
        #Salva o dicionario no arquivo Json
        with open(self.arquivo,'w',encoding='utf-8') as arquivo:
            json.dump(self.dicionario,arquivo,ensure_ascii=False,indent=4)
            
    def adicionar_palavra(self, palavra_ingles, traducao_portugues):
        #Add uma palavra e sua tradução ao dicionario
        if palavra_ingles in self.dicionario:
            return False
        self.dicionario[palavra_ingles] = traducao_portugues
        self.salvar_dicionario()
        return True        
    
    def procurar_palavra(self,busca):
        #Procura uma palavra em ingles ou portugues no dicionario
        for palavra_ingles, traducao_portugues in self.dicionario.items():
            if busca.lower() == palavra_ingles.lower():
                return f"Tradução de '{palavra_ingles}':{traducao_portugues}"
            
            elif busca.lowe() == traducao_portugues.lower():
                return f"A palavra em inglês para '{traducao_portugues}' é: {palavra_ingles}"
        return "Palavra não encontrada."
    