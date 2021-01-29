# Cálculo de contas de energia para residência, comércio e indústria.

kWh = float(input("Digite em kWh o seu gasto mensal: "))
tipo = input("Digite o caráctere que te representa: I (Indústria) - R (Resiência) - C (Comércio) \n Sua escolha: ")

if tipo == "R":
    if kWh <= 500:
        print("Você deve pagar R$%5.2f" % (kWh * 0.40))
    else:
        print("Você deve pagar R$%5.2f" % (kWh * 0.65))
elif tipo == "C":
    if kWh <= 1000:
        print("Você deve pagar R$%5.2f" % (kWh * 0.55))
    else:
        print("Você deve pagar R$%5.2f" % (kWh * 0.60))
elif tipo == "I":
    if kWh <= 5000:
        print("Você deve pagar R$%5.2f" % (kWh * 0.55))
    else:
        print("Você deve pagar R$%5.2f" % (kWh * 0.60))