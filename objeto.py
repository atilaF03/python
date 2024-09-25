import os
os.system("cls||clear")

class Aluno:
    def __init__(self,nome: str ,idade : int, cpf : str) -> None:
        self. nome = nome 
        self.idade = idade
        self.cpf = cpf

    def __str__(self) -> str:
        return (f"\nnome: {self.nome}"
                f"\nidade: {self.idade}"
                f"\nCpf: {self.cpf}"
                )
    
aluno = Aluno("atila",15,"123213414")
print(aluno)