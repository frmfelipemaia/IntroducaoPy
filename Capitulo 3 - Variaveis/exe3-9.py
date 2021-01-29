#Contabilzador de dias, horas, minutos e segundos em segundos

dias = int(input("Insira o valor em dias: "))
horas = int(input("Insira o valor em horas: "))
minutos = int(input("Insira o valor em minutos: "))
segundos = int(input("Insira o valor em segundos: "))
totalEmSegundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (segundos * 60)

print("O total em segundos é: %ds" % totalEmSegundos)
