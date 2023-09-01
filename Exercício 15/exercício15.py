"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
a) quanto pagou ao INSS.
b)quanto pagou ao sindicato.
c) o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo"""

salHora = float(input("Digite o valor que você ganha por hora: "))
horaM = float(input("Digite quantas horas você trabalha no mês: "))

salario = salHora * horaM

imposto = 0.11
salario_ir = salario * imposto
inss = 0.08
salarios_inss = salario * inss
sindicato = 0.05
salario_sin = salario * sindicato

sliquido = salario * (imposto + inss + sindicato)
salarioL = salario - sliquido
print(f"Salário Bruto: R${salario}\nIR (11%): R${salario_ir}\nINSS (8%): R${salarios_inss}\nSindicato (5%): R${salario_sin}\nSalário Líquido: R${salarioL}")