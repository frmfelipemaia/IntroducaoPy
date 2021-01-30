#Tabuada de multiplicação

n = int(input("Digite o valor a ter sua tabuada de 10 gerada: "))
x = 1

while x <= 10:
    print("%d vezes %d é: %d" % (n,x,n*x))
    x += 1