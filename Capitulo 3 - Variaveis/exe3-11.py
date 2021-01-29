#Solicitar e descontar o desconto em um produto

preço = float(input("Digite o preço do produto sem desconto: "))
desconto = float(input("Digite o valor do desconto: "))
desconto = desconto * preço / 100
preçofinal = preço - desconto

print("O valor do desconto foi: R$%5.2f" % desconto)
print("O valor a pagar é: R$%7.2f" % preçofinal)
