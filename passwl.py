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

def gerar_lista_senhas(quantidade):
    nome_arquivo = "senhas_geradas.txt"
    senhas = []

    with open(nome_arquivo, "w") as arquivo:
        for _ in range(quantidade):
            senha = gerar_senha()
            senhas.append(senha)
            arquivo.write(senha + "\n")

    return senhas, nome_arquivo

# Perguntar ao usuário qual ação deseja realizar
opcao = input("Deseja gerar uma única senha (1) ou uma lista de senhas (2)? Digite 1 ou 2: ")

if opcao == "1":
    senha = gerar_senha()
    print(f"Senha gerada: {senha}")
elif opcao == "2":
    quantidade = int(input("Quantas senhas deseja gerar? "))
    senhas, nome_arquivo = gerar_lista_senhas(quantidade)
    
    if quantidade < 30:
        print("\nSenhas geradas:")
        for senha in senhas:
            print(senha)

    print(f"\nAs senhas foram salvas no arquivo: {nome_arquivo}")
else:
    print("Opção inválida. Execute o script novamente e escolha 1 ou 2.")
