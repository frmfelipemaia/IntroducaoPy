#Exercício multípla escolha, modificar para aceitar letra maiuscúla.

pontos = 0
questão = 1

while questão <= 3:
    resposta = input("Digite a resposta da %d questão: " % questão)
    if questão == 1 and (resposta == "A" or resposta == "a"):
        pontos += 1
        questão += 1
    if questão == 2 and (resposta == "B" or resposta == "b"):
        pontos += 1
        questão += 1
    if questão == 3 and (resposta == "C" or resposta == "c"):
        pontos += 1
        questão += 1
print("Fim da prova, você obteve %d pontos." % pontos)