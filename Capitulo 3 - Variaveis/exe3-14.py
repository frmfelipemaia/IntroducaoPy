#Descobrir o preço a pagar de um carro alugado sabendo que um dia vale R$60,00 e por km vale R$0,15

km = float(input("Digite o valor percorrido em km: "))
dias = int(input("Digite o número de dias com o veículo alugado: "))
total = (km * 0.15) + (dias * 60)

print("Valor total à pagar: R$%5.2f." % total)
