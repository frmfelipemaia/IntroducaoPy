#Calcular o juros de depósitos ao longo de 24 meses.

taxa_de_juros = float(input("Digite o valor da taxa de juros dos 24 meses: "))
meses = 1
total = 0
controle = 0

while meses <= 24:
    depósito = float(input("Digite o depósito do %d mês: " % meses))
    controle += depósito
    total += depósito * taxa_de_juros / 100
    print("%s° mês foi depositado R$%5.2f e já foi cobrado R$%d em juros no total." % (meses,depósito,total))
    meses += 1
print("O total depositado nesses 24 meses foi R$%5.2f e o total de juros a ser pago é: R$%5.2f" % (controle, total))