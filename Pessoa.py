from abc import ABC , abstractmethod

class Pessoa (ABC):
    def __init__(self, nome:str, idade:int, email:str) -> None:
        self.idade =idade
        self.nome= nome
        self.email= email
    

        
   