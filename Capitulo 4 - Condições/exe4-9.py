# Aprovamento Empréstimo Bancário baseado em renda

valorCasa = float(input("Digite o valor da casa: "))
salário = float(input("Digite o seu salário: R$"))
anos = int(input("Digite a quantidade anos desejada para quitar o imóvel: "))
prestação = valorCasa / (anos * 12)

if prestação > salário * 0.3:
    print("Empréstimo Recusado.")
else:
    print(("Empréstimo Aprovado."))