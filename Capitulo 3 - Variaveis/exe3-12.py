# Calculador de tempo de viagem com a fração distância por tempo

distância = float(input("Digite em km a distância até o destino: "))
velocidadeMédia = float(input("Digite a velocidade média do percurso: "))
tempo = distância / velocidadeMédia
print("Para chegar ao seu destino ainda faltam %4.2f horas/minutos." % tempo)
