"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo."""

int1 = int(input("Digite o primeiro número inteiro: "))
int2 = int(input("Digite o segundo número inteiro: "))
numR = float(input("Agora digite o número real: "))

dobroint1 = int1**2
divint2 = (int2)/2
produto = dobroint1 * divint2
triploint1 = (int1*3) + numR
cubonumR = numR**3

print(f"{produto} é o produto do dobro do primeiro com metade do segundo.\n{triploint1} é a soma do triplo do primeiro com o terceiro.\n{cubonumR} é o cubo do terceiro")
