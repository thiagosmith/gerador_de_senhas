# Script Wordlist
# Python3
# Cria uma lista de senhas de acordo com a quantidade de palavras informada pelo usuario
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

    # Misturando a senha para evitar padrões fixos
    senha = list(letras_minusculas + letras_maiusculas + numeros + caracteres_especiais + senha_restante)
    random.shuffle(senha)

    return ''.join(senha)

# Solicitar a quantidade de senhas a serem geradas
quantidade = int(input("Quantas senhas deseja gerar? "))

# Nome do arquivo onde as senhas serão salvas
nome_arquivo = "senhas.txt"

# Gerar e salvar as senhas no arquivo
with open(nome_arquivo, "w") as arquivo:
    for _ in range(quantidade):
        senha = gerar_senha()
        arquivo.write(senha + "\n")

# Exibir nome do arquivo na tela
print(f"As senhas foram salvas no arquivo: {nome_arquivo}")
