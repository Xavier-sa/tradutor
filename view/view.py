class DicionarioView:
    @staticmethod
    def mostrar_menu():
        print("\nMenu")
        print("2.Procudar tradução")
        print("3.SAIR")
        
    @staticmethod
    def obter_entrada(mensagem):
        return input(mensagem).strip()
    
    @staticmethod
    def mostrar_mensagem(mensagem):
        print(mensagem)
        
    @staticmethod
    def obter_palvra_e_traducao():
        palavra_ingles = input("Digite a palavra em inglês:").strip()
        traducao_portugues =input("Digite a tradução em português:").strip()
        return palavra_ingles,traducao_portugues