#Descobrir quantos dias de vida um fumante perdeu

cigarrosPorDia = int(input("Quantos cigarros você fuma por dia: "))
anosFumando = int(input("A quantos anos você fuma: "))

tempoPerdido = (anosFumando * 365) + (cigarrosPorDia * 10 / 360)

print("Você perdeu %d dias da sua vida." % tempoPerdido)
