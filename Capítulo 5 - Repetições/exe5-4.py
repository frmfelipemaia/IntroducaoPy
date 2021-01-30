#Imprimir de 1 até onde for pedido, somente ímpares.

fim = int(input("Digite o valor para o fim da sequência: "))
x = 1

while x <= fim:
    print(x)
    x += 1
    if x % 2 == 0:
        x += 1
