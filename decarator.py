from abc import ABC,abstractmethod
def abstractclass(ABC):
    @abstractmethod
    def display(self):
        pass

def concrete(abstractclass):
    def display(self):
        print('hello, good morning')


ob=concrete()
