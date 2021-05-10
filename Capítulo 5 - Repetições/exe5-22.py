#Calculadora básica
while True:
    #Apresente o Menu
    print(' 1 - Adição \n 2 - Subtração \n 3 - Divisão \n 4 - Multiplicação \n 5 - Sair\n')
    
    #Recebe um número válido
    try:
        escolha = int(input('Escolha uma opção: '))
    except:
        print('\nDigite um número inteiro válido! \n\n')
        continue
    
    #Verifica a escolha
    if ((escolha < 1) and (escolha > 5)):
        print('\nEscolha uma opção válida. \n\n')
        continue
    
    #Escolhe dois valores e faz a adição até que o valor base seja 0.
    if escolha == 1:
        print('\nBem vindo a Adição, digite os valores para soma, ou 0 no primeiro valor para voltar ao menu. \n')
        while True:
            try:
                valor_base = int(input("Digite o primeiro valor: "))
                if valor_base == 0:
                    print('\nVoltando ao menu!\n')
                    break
                segundo_valor = int(input('Digite o segundo valor: '))
            except:
                print('Digite números válidos!\n')
                continue
            print(f'O valor da soma é {valor_base + segundo_valor}.\n Próxima Conta? Ou caso queira sair, digite 0! \n')
    
    #Escolhe dois valores e faz a subtração até que o valor base seja 0
    if escolha == 2:
        print('\nBem vindo a Subtração, digite os valores para soma, ou 0 no primeiro valor para voltar ao menu. \n')
        while True:
            try:
                valor_base = int(input("Digite o primeiro valor: "))
                if valor_base == 0:
                    print('\nVoltando ao menu!\n')
                    break
                segundo_valor = int(input('Digite o segundo valor: '))
            except:
                print('Digite números válidos!\n')
                continue
            print(f'O valor da subtração é {valor_base - segundo_valor}.\n Próxima Conta? Ou caso queira sair, digite 0! \n')
    
    #Escolhe dois valores e faz a divisão até que o valor base seja 0
    if escolha == 3:
        print('\nBem vindo a Divisão, digite os valores para soma, ou 0 no primeiro valor para voltar ao menu. \n')
        while True:
            try:
                valor_base = int(input("Digite o primeiro valor: "))
                if valor_base == 0:
                    print('\nVoltando ao menu!\n')
                    break
                segundo_valor = int(input('Digite o segundo valor: '))
            except:
                print('Digite números válidos!\n')
                continue
            print(f'O valor da divisão é {valor_base / segundo_valor}.\n Próxima Conta? Ou caso queira sair, digite 0! \n')
    
    #Escolhe dois valores e faz a multiplicação até que o valor base seja 0
    if escolha == 4:
        print('\nBem vindo a Multiplicação, digite os valores para soma, ou 0 no primeiro valor para voltar ao menu. \n')
        while True:
            try:
                valor_base = int(input("Digite o primeiro valor: "))
                if valor_base == 0:
                    print('\nVoltando ao menu!\n')
                    break
                segundo_valor = int(input('Digite o segundo valor: '))
            except:
                print('Digite números válidos!\n')
                continue
            print(f'O valor da multiplicação é {valor_base * segundo_valor}.\n Próxima Conta? Ou caso queira sair, digite 0! \n')
    
    #Encerra o Programa
    if escolha == 5:
        print("\nAté logo, encerrando a calculadora!\n")
        break