#Determinar se o motorista foi multado e qual o valor da multa

velocidade = float(input("Digite a velocidade em que você estava: "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("Você foi multado e deverá pagar: R$%5.2f." % multa)

if velocidade < 80:
    print("Você não foi multado, parabéns pelo minímo cidadão.")
