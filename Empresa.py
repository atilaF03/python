from enum import Enum

import os
os.system("cls||clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMINO = "Feminino"

class Setor(Enum):
    FINANCEIRO = "Finaiceiro"
    RECURSOS__HUMANOS = "Recursos Humanos"
    VENDAS ="Vendas"
    MARKETING="Marketing"


class Funcionario:
    def __init__(self, id: int , nome: str , salario : float, setor : Setor, sexo : Sexo, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.salario = salario
        self.id = id
        self.setor = setor

    def __str__(self) -> str:
        return(
               f"\n nome:{self.nome}"
               f"\n idade:{self.idade}"
               f"\n Sexo:{self.sexo.value}"
               f"\n setor:{self.setor.value}"
               f"\n id: {self.id}"
               f"\n salario:{self.salario}"
               ) 



funcioario = Funcionario(152,"atila",5000,Setor.MARKETING,Sexo.FEMINO,19)
print(funcioario)


    