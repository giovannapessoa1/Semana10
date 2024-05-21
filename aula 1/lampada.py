class Lampada:
    def __init__(self):
        self.estado = False  # Começa desligada
       
    def alterar_estado(self):
        self.estado = not self.estado
        if self.estado:
            print("Desligada.")
        else:
            print("Ligada.")
        return self.estado

# Uso da classe
lampada = Lampada()
print(lampada.estado)  # Liga a lâmpada
novo_estado = lampada.alterar_estado()
print(novo_estado)
