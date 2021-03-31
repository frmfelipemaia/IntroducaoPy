# Pedir ao usuário digitar códigos para uma caixa registradora.

print('Bem vindo a máquina registradora, digite 10 para sair do programa. :) \n')
print('Os códigos dos produtos e seus valores são:\n  1 - 0,50R$\n  2 - 1,00R$\n  3 - 4,00R$\n  5 - 7,00R$\n  9 - 8,00R$\n')

total = 0

while True:
    codigo = int(input('Digite o código do produto ou 0 para saber o total atual: '))
    if codigo == 10:
        print(f'O valor final é {total}R$')
        break
    elif codigo == 0:
        print(f'O valor atual é {total}R$')
        continue
    try:
        valor = int(input('Digite a quantidade comprada: '))
        if valor < 0:
            print('Valor tem que ser positivo!')
            continue
    except:
        print('O valor deve ser inteiro!')
        continue
    if codigo == 1:
        total = total + (0.5 * valor)
    elif codigo == 2:
        total = total + (1 * valor)
    elif codigo == 3:
        total = total + (4 * valor)
    elif codigo == 5:
        total = total + (7 * valor)
    elif codigo == 9:
        total = total + (8 * valor)
    else:
        print('Código Inválido!')