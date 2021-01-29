#Ler três números e determinar o maior e o menor.


primeiro = float(input("Digite o primeiro valor a ser comparado: "))
segundo = float(input("Digite o segundo valor a ser comparado: "))
terceiro = float(input("Digite o terceiro valor a ser comparado: "))

if primeiro > segundo:
  if primeiro < terceiro:
    print("O maior valor é %5.2f e o menor valor é %5.2f" % (terceiro,segundo))
  if terceiro > segundo:
    print("O maior valor é %5.2f e o menor valor é %5.2f" % (primeiro,segundo))
  print("O maior valor é %5.2f e o menor valor é %5.2f" % (primeiro,terceiro))
if segundo > terceiro:
  if terceiro > primeiro:
    print("O maior valor é %5.2f e o menor valor é %5.2f" % (segundo,primeiro))
  print("O maior valor é %5.2f e o menor valor é %5.2f" % (primeiro,terceiro))
print("O maior valor é %5.2f e o menor valor é %5.2f" % (terceiro,primeiro))
