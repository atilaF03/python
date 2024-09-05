import os;

os.system("cls||clear");

#Criando a classe endereco

class Endereco:
    def __init__(self, logradouro : str, numero : str):
        self.logradouro  = logradouro
        self.numero = numero
    
     
     
    def __str__(self) -> str:
            return (f"\nLogradouro{self.logradouro}"
                    f"\nLogradouro {self.numero}")

        
class Aluno:
    def __init__(self,nome: str, idade:int , endereco: Endereco) -> None:
        self.nome=nome
        self.idade= idade
        self.endereco= endereco
    
    def __str__(self) -> str:
      return (f"nome: {self.nome}\nidade:{self.idade}anos{self.endereco}")
  
  
  
endereco  = Endereco("rua Augusta ", "33")
aluno = Aluno("Matheus","10",endereco)
print(aluno)