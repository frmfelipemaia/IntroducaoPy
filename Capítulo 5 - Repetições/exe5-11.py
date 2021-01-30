#Calcular o juros de um depósito ao longo de 24 meses

depósitoInicial = float(input("Digite o valor para o depósito inicial: "))
taxaDeJuros = float(input("Digite a taxa de juros mensal: "))
meses = 1
total = 0

while meses <= 24:
    total += (depósitoInicial * taxaDeJuros / 100)
    print("%d mês, ganho com juros desses mês: %5.2f" % (meses,total))
    meses += 1
print("O total ganho com juros foi: %5.2f" % total)