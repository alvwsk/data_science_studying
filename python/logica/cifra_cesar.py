import os
import platform
import random

def clear():
    """Limpa a tela do terminal de acordo com o sistema operacional."""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def menu() -> int:
    """Exibe o menu e obtém a opção do usuário."""
    print('============\033[31mBEM-VINDO\033[0m============\n')
    op = input("Você está no codificador e decodificador da Cifra de César!\nDeseja continuar? [S/n] ").strip().lower()

    if op == 'n':
        print('Adeus... Encerrando o programa...')
        exit()

    while True:
        try:
            op = int(input('[1] - Codificar texto\n[2] - Decodificar texto\n:: '))
            if op in (1, 2):
                return op
            print("Opção inválida. Escolha 1 ou 2.")
        except ValueError:
            print("Entrada inválida. Digite um número (1 ou 2).")

def get_text(op: int) -> tuple[str, list | None]:
    """Obtém o texto e a chave de decodificação (se necessário)."""
    if op == 1:
        text = input('Digite o texto a ser codificado: ').lower()
    else:
        text = input('Digite o texto a ser decodificado: ').lower()

    if op == 2:
        while True:
            key = input('Digite a chave de decodificação (separe os números com vírgulas ou espaços): ').strip()
            key_list = key.replace(',', ' ').split()
            if all(num.isdigit() for num in key_list):
                return text, [int(num) for num in key_list]
            print('Entrada inválida! A chave deve conter apenas números separados por vírgulas ou espaços.')
    return text, None

def logic(text: str, keys: list = None) -> tuple[str, list | None]:
    """Criptografa ou descriptografa o texto utilizando uma cifra de César com múltiplas chaves."""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ciphered_text = ''
    total_keys = random.randint(26, 26)

    if keys is None:
        keys = []
        while len(keys) < total_keys:
            num = random.randint(1, 26)
            if num not in keys:
                keys.append(num)

        for i, letter in enumerate(text):
            if letter in alphabet:
                key = keys[i % len(keys)]
                index = alphabet.index(letter)
                new_index = (index + key) % 26
                ciphered_text += alphabet[new_index]
            else:
                ciphered_text += letter
    else:
        for i, letter in enumerate(text):
            if letter in alphabet:
                key = keys[i % len(keys)]
                index = alphabet.index(letter)
                new_index = (index - key) % 26 
                ciphered_text += alphabet[new_index]
            else:
                ciphered_text += letter
    return ciphered_text, keys

# Execução do programa
while True:
    clear()
    option = menu()
    text, keys = get_text(option)
    result_text, used_keys = logic(text, keys)

    if option == 1:
        print('\nTexto codificado:', result_text)
        print('Chaves para descriptografar:', used_keys)
    else:
        print('\nTexto decodificado:', result_text)

    op = input("\nDeseja continuar? [Y/n] ").lower()
    if op == 'n':
        break