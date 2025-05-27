from abc import ABC, abstractmethod

class Dispositivo(ABC):
    
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
class Lampada(Dispositivo):
    def ligar(self):
        print('lâmpada ligada')
        
    def desligar