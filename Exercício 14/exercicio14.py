"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas."""

peso = float(input("Digite a pesagem de sua pesca: "))
pesoL = 50
multaQ = 4.00

if peso <= 50:
    print("Sua pesca não excede o peso especificado pelo estado de SP. Você não precisará pagar multa.")
elif peso >= 50:
    pesoE = peso - pesoL
    multa = pesoE * multaQ
    print(f"A sua pesca pesa kg{peso} e excede o limite especificado pelo Estado de SP, sua multa será de R${multa}.")
    