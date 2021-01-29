# Calcular o valor de uma passagem

distância = float(input("Digite a distância em km: "))

if distância > 200:
    valor = distância * 0.45
    print("O valor da passagem é R$%4.2f" % valor)
else :
    valor = distância * 0.50
    print("O valor da passagem é R$%4.2f" % valor)