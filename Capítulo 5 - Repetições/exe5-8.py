#Multiplicação utilizando soma

primeiro = int(input("Digite o valor que será multiplicado: "))
segundo = int(input("Digito o valor que irá multiplicar: "))
controle = 1
soma = primeiro

while controle < segundo:
    primeiro += soma
    controle += 1
print("O resultado da multiplicação é: %d" % primeiro)