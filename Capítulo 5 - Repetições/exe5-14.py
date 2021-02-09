#Pedir para o usuário digitar números para tirar uma média, interromper no 0.


controle = 0
base = 0

while True:
    n = int(input("Digite o valor a ser somado: "))
    base += n
    if n == 0:
        break
    controle += 1
print("Tiveram %d números e o resultado da média é: %d" % (controle, base/controle))
print(f"Tiveram {controle} números e o resultado da média é: {base/controle}")