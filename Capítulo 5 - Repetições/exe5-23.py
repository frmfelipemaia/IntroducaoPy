#Verificar se o número é primo
while True:
    #Recebe o número e verifica se é válido
    try:
        numero_base = int(input('\nDigite o número que deseja saber se é primo: '))
    except:
        print("Digite um número inteiro válido.")
        continue
    
    x = numero_base
    
    #Vetor dos primos
    numero = 2
    impares = []
    while numero != numero_base:
        if ((numero % 2) == 0):
            numero = numero + 1
            continue
        else:
            impares.append(numero)
            numero = numero + 1
            continue
    
    #Verificação simples 
    while True:
        if x == 1:
            print("O número 1 não é primo.")
            break
        if x == 0:
            print("O número 0 não é primo.")
            break
        resto = x % 2 
        x = resto
        if resto == 1:
            while True:
                print(impares)
                for n in impares:
                    if numero_base % n == 0:
                        print(f'O número {numero_base} não é primo.')
                        break
                    print(f'O número {numero_base} é primo.')
                    break
                break
            break  
        elif resto == 0:
            print(f'O número {numero_base} não é primo.')
            break
    
    #Reinicia o programa
    print('\nDeseja verificar outro número?\n')
    try:
        escolha = int(input(" 1 - Sim \n 2 - Não \nDigite: "))
    except:
        print('\nOpção Inválida, fechando programa.\n')
    
    if escolha == 1:
        print("\nSeguindo então!\n")
    elif escolha == 2:
        print('\nEncerrando.\n')
        break