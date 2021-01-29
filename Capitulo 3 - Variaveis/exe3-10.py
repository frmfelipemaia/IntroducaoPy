#Calculador de aumento salarial.

salarioAntigo = float(input("Digite o seu salário antes do aumento: "))
aumento = float(input("Digite a porcentagem de aumento salarial: "))
aumento = aumento*salarioAntigo/100
salarioNovo = salarioAntigo + aumento

print("Seu aumento é de: R$%5.2f" % aumento)
print("Seu novo salário é: R$%5.2f" % salarioNovo)
