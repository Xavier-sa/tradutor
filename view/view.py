class DicionarioView:
    @staticmethod
    def mostrar_menu():
        print("\nMenu")
        print("1.Adicionar palavra")
        print("2.Procurar tradução")
        print("3.SAIR")
        
    @staticmethod
    def obter_entrada(mensagem):
        return input(mensagem).strip()
    
    @staticmethod
    def mostrar_mensagem(mensagem):
        print(f"{'-'*20}")
        print(mensagem)
        
    @staticmethod
    def obter_palavra_e_traducao():
        palavra_ingles = input("Digite a palavra em inglês:").strip()
        traducao_portugues =input("Digite a tradução em português:").strip()
        return palavra_ingles,traducao_portugues