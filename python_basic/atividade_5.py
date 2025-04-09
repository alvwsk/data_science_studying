# Escreva um código usando enumerate para exibir os índices e valores da lista ["maçã", "banana", "uva"].

lista = ["maçã", "banana", "uva"]
for i, value in enumerate(lista):
    print(f"{i}: {value}")

# Crie uma lista com os números pares de 1 a 10 usando List Comprehension.

print([i for i in range(1, 11) if i % 2 == 0])

# Escreva um programa que use map para multiplicar cada elemento da lista [1, 2, 3, 4] por 3.

print(list(map(lambda i: i*3, [1, 2, 3, 4])))

# Escreva um programa que use enumerate e List Comprehension para criar uma lista de tuplas com os índices e valores ao quadrado de [2, 4, 6]

lista = [(index, value ** 2) for index, value in enumerate([2, 4, 6])]
print(lista)
