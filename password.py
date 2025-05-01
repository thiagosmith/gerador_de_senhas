# Script Password
# Python3
# Gera uma única senha por execução
# Criado em 01-05-2025 by 5M1TH - OffSec Team | Smith Braz

banner = """
#############################################
#                                           #
#    5M1TH - OffSec Team | Smith Braz       #
#                                           #
#############################################
"""

print(banner)

import random
import string

def gerar_senha():
    tamanho = random.randint(12, 16)

    # Garantindo que a senha contenha pelo menos um de cada tipo de caractere
    letras_minusculas = random.choice(string.ascii_lowercase)
    letras_maiusculas = random.choice(string.ascii_uppercase)
    numeros = random.choice(string.digits)
    caracteres_especiais = random.choice("!@#$%&*-+=")

    # Preenchendo o restante da senha com caracteres aleatórios
    todos_caracteres = string.ascii_letters + string.digits + "!@#$%&*-+="
    senha_restante = ''.join(random.choice(todos_caracteres) for _ in range(tamanho - 4))

    # Misturando a senha para evitar que os caracteres garantidos fiquem sempre no início
    senha = list(letras_minusculas + letras_maiusculas + numeros + caracteres_especiais + senha_restante)
    random.shuffle(senha)

    return ''.join(senha)

# Gerar uma senha aleatória
senha_aleatoria = gerar_senha()
print("Senha gerada:", senha_aleatoria)
