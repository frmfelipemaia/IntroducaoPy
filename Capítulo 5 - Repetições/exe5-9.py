#Dividir os números somente subtraindo

primeiro = int(input("Digite o número que será dividido: "))
segundo = int(input("Digito o divisor: "))
resultado = 0

while primeiro >= segundo:
    primeiro = primeiro - segundo;
    resultado += 1
print("O resultado da divisão é: %d" % resultado)