#Tabuada montada pelo usuário

n = int(input("Digite o número que será multiplicado na taboada: "))
inicio = int(input("Digite o primeiro número da taboada: "))
fim = int(input("Digite o fim da taboada: "))

while inicio <= fim:
    print("%d multiplicado por %d é: %d." % (n, inicio, n*inicio))
    inicio += 1