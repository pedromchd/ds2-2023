class Carro:
    __velocidade__ = 0
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano

    def acelerar(self, velocidade):
        self.__velocidade__ += velocidade