class Copiador:
    def __init__(self):
        self.terminado = False

    def copia_pegar(self):
        print("Copiando y pegando...")
        print(f"Estado de la tarea: {self.terminado}")
        #Simulacion
        self.terminado = True
        print(f"Estado de la tarea: {self.terminado}")

    def cambiar_estado(self):
        print("Cambiando estado a False")
        self.terminado = False 
