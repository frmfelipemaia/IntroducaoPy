# Contagem de cédulas NÃO FUNCIONA DIREITO :(
valor = float(input("Digite o valor a pagar: "))
notas_cem = 0
notas_cinquenta = 0 
notas_vinte = 0 
notas_dez = 0 
notas_cinco = 0
notas_dois = 0
moedas_um = 0
moedas_cinquenta = 0
moedas_vinte_e_cinco = 0 
moedas_dez = 0 
moedas_cinco = 0
moedas_centena = 0
moedas_milhar = 0

while True:
    if valor >= 100:
        valor = valor - 100
        notas_cem += 1
        continue
    elif valor >= 50:
        valor = valor - 50 
        notas_cinquenta += 1
        continue
    elif valor >= 20:
        valor = valor - 20
        notas_vinte += 1
        continue
    elif valor >= 10:
        valor = valor - 10 
        notas_dez += 1
        continue
    elif valor >= 5:
        valor = valor - 5 
        notas_cinco += 1
        continue
    elif valor >= 2:
        valor = valor - 2 
        notas_dois += 1 
        continue
    elif valor >= 1:
        valor = valor - 1 
        moedas_um += 1
        continue
    elif valor >= (1/2):
        valor = valor - (1/2)
        moedas_cinquenta += 1
        continue
    elif valor >= (1/4):
        valor = valor - (1/4)
        moedas_vinte_e_cinco += 1
        continue
    elif valor >= (1/10):
        valor = valor - (1/10)
        moedas_dez += 1
        continue
    elif valor >= (1/20):
        valor = valor - (1/20)
        moedas_cinco += 1
        continue
    elif valor >= (1/100):
        valor = valor - (1/100)
        moedas_centena += 1
        continue
    # elif valor >= 0.001:
    #     valor = valor - 0.001
    #     moedas_milhar += 1
    #     continue
    if valor == 0 or valor < 0:
        break
    print(f'Valor caindo {valor}')
total_notas = notas_cem + notas_cinquenta + notas_vinte + notas_dez + notas_cinco + notas_dois
total_moedas = moedas_um + moedas_cinquenta + moedas_vinte_e_cinco + moedas_dez + moedas_centena + moedas_milhar
print(f'Foram necessárias:\n{notas_cem} nota(s) de R$100,00\n{notas_cinquenta} nota(s) de R$50,00\n{notas_vinte} nota(s) de R$20,00\n{notas_dez} nota(s) de R$10,00\n{notas_cinco} nota(s) de R$5,00\n{notas_dois} nota(s) de R$2,00\n{moedas_um} moeda(s) de R$1\n{moedas_cinquenta} moeda(s) de R$0,50\n{moedas_vinte_e_cinco} moeda(s) de R$0,25\n{moedas_dez} moeda(s) de R$0,10\n{moedas_cinco} moeda(s) de R$0,05\n{moedas_centena} moeda(s) de R$0,01\n{moedas_milhar} moeda(s) de R$0,001\nOu seja {total_notas} nota(s) e {total_moedas} moeda(s).')