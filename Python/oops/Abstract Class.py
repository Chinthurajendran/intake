from abc import ABC,abstractmethod

class coumputer(ABC):
    @abstractmethod
    def process(self):
        pass

class laptop(coumputer):
    def process(self):
        print("hai chinthu")

data = laptop()
data.process()