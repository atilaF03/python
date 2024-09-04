from abc import ABC,abstractmethod
import os 

os.system("cls||clear")

class Funcionarios (ABC):
    def __init__ (self,nome:str ,salario:float)->None:
        self.nome = nome
        self.salario = salario
     
    @abstractmethod 
    def salario_final (self) ->float:
        pass 
        
    def __str__(self) -> str:
        return (
        f"\nnome:{self.nome}"    
        f"\nsalariio{self.salario }"
        f"\nacresccimo {self.salario_final()}"
        )
        
class Motoboy(Funcionarios):
    BONIFICACAO = 1.1
    def salario_final(self) -> float:
        resultado  = self.salario * self.BONIFICACAO
        return resultado
    pass


class Engenheiro(Funcionarios):
    BONIFICACAO = 1.2
    def __init__(self, nome: str, salario: float, crea :str ) -> None:
        super().__init__(nome, salario)
        self.crea = crea 
    def salario_final(self) -> float:
        resultado  = self.salario * self.BONIFICACAO
        return resultado
   
    def __str__(self) -> str:
        return f"{super().__str__()}"f"\ncrea:{self.crea}"


motoboy_1 = Motoboy("José",1000)
print(motoboy_1)

engenheiro =Engenheiro("Maria ", 1000,"45854")
print(engenheiro)