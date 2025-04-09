# Crie um programa que use um laço for para imprimir os números de 1 a 5 no console.

for i in range(1, 6):
    print(i)

# Escreva um programa que declare uma lista com os números [10, 20, 30, 40, 50] e exiba o primeiro elemento.

print([i * 10 for i in range(1, 6)][0])

# Faça um programa que use um laço while para somar todos os números de 1 a 10 e exiba o resultado no console.

soma = 0
numero = 1

while numero <= 10:
    soma += numero
    numero += 1   

print(soma)


# Crie um programa que declare um dicionário com as seguintes chaves e valores: {"nome": "Ana", "idade": 25, "cidade": "Fortaleza"} e exiba o valor associado à chave "idade"

dic = {"nome": "Ana", "idade": 25, "cidade": "Fortaleza"}
print(dic['idade'])

# Escreva um programa que inverta uma string utilizando um laço for. Por exemplo, para a string "Python", o resultado deve ser "nohtyP".

str_atual = 'Python'
str_nova = ''
for letra in str_atual[::-1]:
    str_nova += letra
print(str_nova)

# Escreva um programa que calcule a frequência de cada caractere em uma string. Por exemplo, na string "banana", o programa deve exibir: {'b': 1, 'a': 3, 'n': 2}

texto = 'banana'
freq = {}

for c in texto:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
print(freq)



