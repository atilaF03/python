
from Pessoa import Pessoa


class Aluno (Pessoa):   
   def __init__(self, nome: str, idade: int, email: str,id:str) -> None:
      super().__init__(nome, idade, email)
      self.id= id

   def __str__(self):
        return(f"\no nome é:{self.nome}"
               f"\na idade é:{self.idade}"
               f"\no email é: {self.email}"
               f"\no id é {self.id}"
               )
      

aluno= Aluno("atila ",12,"atila@","123")

print(aluno)