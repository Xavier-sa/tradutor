from model import DicionarioModel
from view import DicionarioView

class DicionarioController:
    def __init__(self):
        self.model = DicionarioModel()
        self.view = DicionarioView()

    def executar(self):
        while True:
            self.view.mostrar_menu()
            escolha = self.view.obter_entrada("Escolha uma opção (1, 2 ou 3): ")

            if escolha == '1':
                palavra_ingles, traducao_portugues = self.view.obter_palavra_e_traducao()
                sucesso = self.model.adicionar_palavra(palavra_ingles, traducao_portugues)
                if sucesso:
                    self.view.mostrar_mensagem(f"Palavra '{palavra_ingles}' adicionada com sucesso!")
                else:
                    self.view.mostrar_mensagem("Essa palavra já foi adicionada.")

            elif escolha == '2':
                busca = self.view.obter_entrada("Digite a palavra (em inglês ou português) para procurar: ")
                resultado = self.model.procurar_palavra(busca)
                self.view.mostrar_mensagem(resultado)

            elif escolha == '3':
                self.view.mostrar_mensagem("Saindo do programa.")
                break
            else:
                self.view.mostrar_mensagem("Opção inválida, tente novamente.")
