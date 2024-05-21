class Usuario:
    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha
    def alterar_senha(self, nova_senha):
        if len(nova_senha) >= 8:
            self.__senha = nova_senha
            print("Senha alterada com sucesso!")
        else:
            print("A nova senha deve ter no mínimo 8 caracteres.")
usuario1 = Usuario("aninha", "gatinho1")
usuario1.alterar_senha("novasenha123")
usuario1.alterar_senha("joaninha")
