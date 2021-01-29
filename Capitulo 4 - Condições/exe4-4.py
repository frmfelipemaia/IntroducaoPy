# Determinar um aumento para um funcionário referente ao seu salário

salario = float(input("Digite seu salario: "))

if salario > 1250.00:
  salario = salario * 1.1
  print("Seu novo salario é: R$%7.2f" % salario)
if salario <= 1250.00:
  salario = salario * 1.15
  print("Seu novo salario é: R$%7.2f" % salario)
  