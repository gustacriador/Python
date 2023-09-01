"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
a) Para homens: (72.7*h) - 58
b) Para mulheres: (62.1*h) - 44.7"""

genero = input("Digite qual o seu gênero (M para Masculino ou F para Feminino): ")
altura = float(input("Digite qual é a sua altura: "))

if genero == "M" or genero == "m":
    pesoM = (72.7*altura) - 58
    print(f"O peso ideal para um homem de altura {altura} é {pesoM}")

elif genero == "F" or genero == "f":
    pesoF = (62.1*altura) - 44.7
    print(f"O peso ideal para uma mulher de altura {altura} é {pesoF}")
    
else:
     print("Gênero não reconhecido. Por favor, digite algo nos padrões solicitados.")