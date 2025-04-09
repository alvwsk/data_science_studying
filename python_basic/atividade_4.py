# Pense em um código em Python com duas funções. Uma função para calcular a área de um quadrado e outra função para calcular a área de um retângulo.

def area_quadrado(lado):
    return lado ** 2

def area_retangulo(base, altura):
    return base * altura


lado = float(input("Digite o lado do quadrado: "))
print(f"Área do quadrado: {area_quadrado(lado)}")    
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
print(f"Área do retângulo: {area_retangulo(base, altura)}")
