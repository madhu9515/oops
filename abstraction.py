from abc import ABC,abstractmethod
class abscls(ABC):
    @abstractmethod
    def display(self):
        None

class conc(abscls):
    def display(self):
        print('hello, good morning')

ob=conc()
ob.display()
