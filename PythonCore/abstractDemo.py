from abc import ABC, abstractmethod
class polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass

class triangle(polygon):
    def noofsides(self):
        
