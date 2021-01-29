#Calculadora básica com if e elif

primeiro = float(input("Digite o primeiro valor: "))
segundo = float(input("Digite o segundo valor: "))
operação = input("Qual operação deseja fazer? Somar(1) - Subtrair(2) - Multiplicar(3) - Dividir(4) \n Escreva a opção numérica: ")

if operação == "1":
    print("O resultado da soma é: %5.2f" % (primeiro + segundo))
elif operação == "2":
    print("O resultado da subtração é: %5.2f" % (primeiro - segundo))
elif operação == "3":
    print("O resultado da multiplicação é: %5.2f" % (primeiro * segundo))
elif operação == "4":
    print("O resultado da divisão é: %5.2f" % (primeiro / segundo))