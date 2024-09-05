from enum import Enum

import os

os.system("cls||clear")

class Sexo(Enum):
    MASCULINO = "Masculino"

print(f"o sexo é: {Sexo.MASCULINO.value}")

