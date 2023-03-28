class Carro:
    def __init__(self, nome):
        self.nome = nome    
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self,valor):
        self._motor = valor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self,valor):
        self._fabricante = valor
    

        
class Motor:
    def __init__(self, nome):
        self.nome = nome
        
class Fabricante:
    def __init__(self,nome):
        self.nome = nome

car = Carro('uno')
motor1 = Motor('xx')
fabricante1 = Fabricante('fiat')

car.motor = motor1
car.fabricante = fabricante1

print(car.nome, car.fabricante.nome, car.motor.nome )