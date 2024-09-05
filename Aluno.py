from enum import Enum

import os
os.system("cls||clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMINO = "Feminino"


class Aluno:
    def __init__(self, nome : str ,idade: int ,sexo: Sexo) -> None:
        self.nome = nome
        self.idade = idade
        self .sexo = sexo

    def __str__(self) -> str:
      return (f"\n nome: {self.nome}"
              f"\n idade: {self.idade}"
              f"\n Sexo: {self.sexo.value}"
              
             )
    

aluno = Aluno("Atila", 12, Sexo.MASCULINO )
print(aluno)

    