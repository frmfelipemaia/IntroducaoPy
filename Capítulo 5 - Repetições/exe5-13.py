#Cálculo de meses para pagar uma dívida baseado em pagamento mensal.

dívida = float(input("Digite o valor da dívida: R$"))
juros_mensal = float(input("Digite o valor do juros mensal: "))
meses = 0
resto = 0

while dívida > 0:
    depósito = float(input("Digite o valor do depósito para pagar a dívida: "))
    depósito = depósito - (depósito * juros_mensal / 100)
    dívida -= depósito
    meses += 1
    if dívida < 0:
        resto = dívida * -1
        dívida = 0
    print("Sua dívida atual é: R$%5.2f" % dívida ) 
print("Parábens você pagou a dívida em %d meses e aqui está o possível troco: R$%5.2f." % (meses,resto))